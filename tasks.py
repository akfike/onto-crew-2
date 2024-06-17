from crewai import Task
from crewai_tools import SerperDevTool

import os

from dotenv import load_dotenv
load_dotenv()

serper_api_key = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()

class OntoTasks:
    
    def understand_proposal(self, agent, text):
        description = (
            f"""
                Read the snippet of our research given below and understand the domain and scope of the project.
                Snippet: {text}
            """
        )
        expected_output = 'A paragraph or two explaining the domain and scope of the research project.'

        return Task(
            description=description,
            expected_output=expected_output,
            tools=[], 
            agent=agent,
            context=[],
            output_file="output_documents/SummarizeProposal/proposal_summary.md",
        )
    
    def research_ontology_creation(self, agent):
        description = (
            """Search the internet to find out information on how to create an ontology. In other words,
            what is the pipeline from a general idea for the ontology to the finished schema of the ontology and identified
            classes of the ontology.""")
        expected_output = "A numbered list that includes the pipeline from an idea to the full ontology in OWL or RDF format with triples."

        return Task(
            description=description,
            expected_output=expected_output,
            tools=[search_tool],
            agent=agent,
            context=[],
            output_file="output_documents/ontology_research.md"
        )