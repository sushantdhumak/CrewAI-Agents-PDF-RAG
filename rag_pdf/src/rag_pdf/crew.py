from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Get the directory where this pdf is located
directory = Path(__file__).parent
pdf_file_path = str(directory) + "/AgentOps.pdf"

# Create the PDFSearchTool object
pdf_search_tool = PDFSearchTool(pdf=pdf_file_path)

@CrewBase
class RagPdf():
	"""RagPdf crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def pdf_rag_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['pdf_rag_writer'],
			tools=[pdf_search_tool],
			verbose=True
		)

	@agent
	def rag_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['rag_summarizer'],
			verbose=True
		)


	@task
	def pdf_rag_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['pdf_rag_writing_task'],
		)

	@task
	def rag_summarizing_task(self) -> Task:
		return Task(
			config=self.tasks_config['rag_summarizing_task'],
			output_file='RAG_Summary.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the RagPdf crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
