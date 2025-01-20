# RagPdf Crew

Welcome to the RagPdf Crew project, powered by [crewAI](https://crewai.com). This project set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.


## Running the Project

To initialize the crew of AI agents and begin task execution, run the following command from the root folder of the project:
'python .\src\rag_pdf\main.py'

This command initializes the rag-pdf Crew, assembling the agents and assigning them tasks as defined in the configuration.


## Understanding Your Crew

The rag-pdf Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


## Final Results

This will create a `RAG_Summary.md` file with the output of a news report on given question in the root folder.
