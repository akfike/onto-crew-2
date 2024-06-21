import os
import sys
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

load_dotenv(verbose=True)

project_root = os.getenv('PROJECT_ROOT')

print(project_root)

# Add the project root to sys.path
if project_root:
    sys.path.insert(0, project_root)
else:
    raise EnvironmentError("PROJECT_ROOT environment variable not set in .env file")

from agents import OntoAgents
from tasks import OntoTasks

OpenAIModel = ChatOpenAI(
    model="gpt-4-turbo"
)

print(OpenAIModel)

# Function to read unique items from the text file
def read_unique_items_from_file(file_path):
    with open(file_path, 'r') as file:
        unique_items = file.readlines()
    unique_items = [item.strip() for item in unique_items]  # Remove newline characters
    return unique_items

class ERCrew:

    def __init__(self):
        self.questions = read_unique_items_from_file('/Volumes/T7Shield/onto-crew-2/long_descriptions.txt')  # Load questions from the text file

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()

        entity_expert = agents.entity_identifier()
        qa_agent = agents.quality_assurance()

        id_tasks = []
        for idx, question in enumerate(self.questions):
            er_identification_task = tasks.entity_identification(entity_expert, question, idx)
            qa_task = tasks.ensure_proper_format(qa_agent, idx, er_identification_task)
            id_tasks.append(er_identification_task)
            id_tasks.append(qa_task)

        crew = Crew(
            agents=[entity_expert],
            tasks=id_tasks,
            verbose=True,
            process=Process.hierarchical,
            manager_llm=OpenAIModel,
            max_rpm=60
        )
        results = crew.kickoff()

        return results


if __name__ == "__main__":

    onto_crew = ERCrew()
    result = onto_crew.run()
    for res in result:
        print(res)
