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

file_path = 'incident_types.md'

# Read the content of the markdown file
with open(file_path, 'r') as file:
    file_content = file.read()

class OntoCrew:

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()

        onto_expert = agents.ontology_expert()

        onto_task = tasks.ontology_generation(onto_expert, file_content)

        crew = Crew(
            agents=[onto_expert],
            tasks=[onto_task],
            verbose=True,
            process=Process.hierarchical,
            manager_llm=OpenAIModel,
            max_rpm=60
        )
        results = crew.kickoff()

        return results


if __name__ == "__main__":

    onto_crew = OntoCrew()
    result = onto_crew.run()
    for res in result:
        print(res)
