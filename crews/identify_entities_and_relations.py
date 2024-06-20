from crewai import Crew, Process
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import sys

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
    model="ft:gpt-3.5-turbo-0125:sailua::9budwaOP"
)

print(OpenAIModel)

class ERCrew:

    questions = [
        "During the past 12 months, have you driven a vehicle while you were under the influence of alcohol?",
        "During the past 12 months, have you driven a vehicle while you were under the influence of marijuana?",
        "During the past 12 months, have you driven a vehicle while you were under the influence of cocaine?",
        "During the past 12 months, have you driven a vehicle while you were under the influence of heroin?",
        "During the past 12 months, have you driven a vehicle while you were under the influence of hallucinogens?",
        "During the past 12 months, have you driven a vehicle while you were under the influence of inhalants?",
        "During the past 12 months, have you driven a vehicle while you were under the influence of methamphetamines?",
        "Compared to when you first started smoking, you need to smoke a lot more now in order to be satisfied.",
        "Some people who use prescription pain relievers try to cut down or stop but find they can't. Was there more than one time in the past 12 months when you tried but were unable to cut down or stop using any prescription pain relievers?"
    ]

    def run(self):
        agents = OntoAgents()
        tasks = OntoTasks()

        entity_expert = agents.entity_identifier()

        id_tasks = []
        for idx, question in enumerate(ERCrew.questions):
            er_identificaiton_task = tasks.entity_identification(entity_expert, question, idx)
            id_tasks.append(er_identificaiton_task)

        crew = Crew(
            agents=[entity_expert],
            tasks=id_tasks,
            verbose=True,
            # process=Process.hierarchical,
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