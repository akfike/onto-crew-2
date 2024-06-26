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
    
    def research_dataset(self, agent, text):
        description = (
            f"""
                Search the internet for any information regarding {text}.
                Provide a summary of the dataset, what its purpose is, what data is collected, and list all critical concepts in the domain.
            """
        )
        expected_output = "Summary: <summary of dataset>\n Purpose: <purpose of dataset> \n Primary concepts: <primary concepts of dataset>"

        return Task(
            description=description,
            expected_output=expected_output,
            tools=[search_tool],
            agent=agent,
            context=[],
            output_file=f"output_documents/{text}_research.md"
        )
    
    def entity_identification(self, agent, text, i):
        return Task(
            description=f"Please parse this question for the main entities and relationships: {text}",
            expected_output="(Entity_name)->[relation_name]->(Entity_name)",
            agent=agent,
            output_file=f"entity_relations_{i}.md"
        )
    
    def ensure_proper_format(self, agent, i, context):
        return Task(
            description="Please edit the output from the previous task if necessary to ensure it is in the proper format. Make sure any spaces between words are replaced with underscores.",
            expected_output="(Entity_1)->[relation_name]->(Entity_2), (Entity_3)->[relation_name]->(Entity_4)",
            agent=agent,
            context=[context],
            output_file=f"final_er_{i}.md"
        )
    
    def ontology_generation(self, agent, text):
        return Task(
            description=f"Read the following text and create a general ontology: {text}",
            expected_output="Represent the ontology in RDF or OWL format",
            agent=agent,
            output_file="onto.owl"
        )
