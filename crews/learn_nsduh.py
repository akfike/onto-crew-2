from crewai import Crew, Process
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import sys

load_dotenv(verbose=True)

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

print(OpenAIModel)

class DatasetCrew:

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()

        dataset_expert = agents.dataset_expert()

        learn_dataset = tasks.research_dataset(dataset_expert, "National Survey on Drug Use and Health")

        crew = Crew(
            agents=[dataset_expert],
            tasks=[learn_dataset],
            verbose=True,
            process=Process.hierarchical,
            manager_llm=OpenAIModel,
            max_rpm=60
        )
        results = crew.kickoff()
        

        return results


if __name__ == "__main__":

    onto_crew = DatasetCrew()
    result = onto_crew.run()
    for res in result:
        print(res)