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

class OntoCrew:

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()

        ontology_expert = agents.ontology_expert()

        learn_onto_pipeline = tasks.research_ontology_creation(ontology_expert)

        crew = Crew(
            agents=[ontology_expert],
            tasks=[learn_onto_pipeline],
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