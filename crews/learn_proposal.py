from crewai import Crew, Process
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import sys

load_dotenv()

project_root = os.getenv('PROJECT_ROOT')

# Add the project root to sys.path
if project_root:
    sys.path.insert(0, project_root)
else:
    raise EnvironmentError("PROJECT_ROOT environment variable not set in .env file")

from agents import OntoAgents
from tasks import OntoTasks

OpenAIModel = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL_NAME")
)

class ProposalCrew:

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()

        proposal_agent = agents.proposal_expert_agent()

        proposal_tasks = []
        directory = "output_documents/ExtractTextInfoFromPDF"
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    proposal_chunk = file.read()

                    understand_proposal_task = tasks.understand_proposal(proposal_agent, proposal_chunk)
                    proposal_tasks.append(understand_proposal_task)

        crew = Crew(
            agents=[proposal_agent],
            tasks=proposal_tasks,
            verbose=True,
            process=Process.hierarchical,
            manager_llm=OpenAIModel,
            max_rpm=60
        )
        results = crew.kickoff()
        

        return results


if __name__ == "__main__":

    onto_crew = ProposalCrew()
    result = onto_crew.run()
    for res in result:
        print(res)