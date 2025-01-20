#!/usr/bin/env python
import sys
import warnings

from crew import RagPdf

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """

    user_input = input("Enter any question on AgentOps: ")

    inputs = {
        'input': user_input
    }

    result = RagPdf().crew().kickoff(inputs=inputs)
    print(result)


if __name__ == "__main__":
    run()