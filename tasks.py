# ontology_tasks.py
from crewai import Task
from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

load_dotenv()
serper_api_key = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()

class OntoTasks:

    # def understand_proposal_first(self, agent, chunk, chunk_number):
    #     description = (
    #         f"Read the following chunk of the proposal text and understand the domain and scope of the proposed ontology. "
    #         f"Proposal text: {chunk}"
    #     )
    #     expected_output = 'A paragraph or two explaining the domain and scope of the research project.'

    #     return Task(
    #         description=description,
    #         expected_output=expected_output,
    #         tools=[], 
    #         agent=agent,
    #         output_file=f"proposal_summary_{chunk_number}.md"
    #     )
    
    def understand_proposal(self, agent, chunk, chunk_number, context):
        description = (
            f"Read the following chunk of the proposal text and understand the domain and scope of the proposed ontology. "
            f"Proposal text: {chunk}"
        )
        expected_output = 'A paragraph or two explaining the domain and scope of the research project.'

        return Task(
            description=description,
            expected_output=expected_output,
            tools=[],  # Ensure this is a list
            agent=agent,
            context=[context],  # Ensure this is properly formatted, e.g., a dictionary or list
            output_file=f"proposal_summary_{chunk_number}.md"
        )

    def research_existing_ontologies(self, agent, text):
        return Task(
            description=(
                f""" Given the context from the previous tasks implemented to 
                understand the research proposal, this task involves searching the internet and research literature
                for existing ontologies that relate to our research topic on social determinants of health
                and justice.
                
                Context: {text}"""
            ),
            expected_output='A report on existing ontologies that can be reused. For each presented ontology the format should be like this: Name: Example Ontology, Link: www.exampleonto.com, Summary: This ontology includes concepts such as a, b, c,. ',
            tools=[search_tool],
            agent=agent,
            output_file="existing_ontologies_report.md"
        )

    def research_ontology_development(self, agent):
        return Task(
            description=(
                """ Research what an ontology is on the internet and in research literature. Learn the common practices of developing
                ontologies, what they are supposed to convey, and how they are supposed to be formatted. Also view existing reputable ontologies for examples
                of good ontologies.
            """
            ),
            expected_output="A report on what an ontology is, a list of steps to develop and ontology, and an example of how an ontology should be formatted.",
            agent=agent,
            output_file="ontology_report.md"
        )
    
    def develop_ontology_from_codebook(self, agent, chunk, chunk_number):
        return Task(
            description=(
                f"Given a part of the codebook for a particular dataset, identify what elements would make up the topmost level of an ontology made for this dataset. Codebook part: {chunk}"
            ),
            expected_output='A list of potential topmost level concepts or entities',
            tools=[],
            agent=agent,
            output_file=f"ontology_top_level_{chunk_number}.txt"
        )
    
    def evaluate_ontology(self, agent, proposal_chunk, proposal_chunk_number, ontology_chunk):
        return Task(
            description = (
                f"Given a summary of the research proposal, identify if the listed concepts are relevant for our ontology. "
                f"If they aren't, either propose a similar concept that fits better or just remove it completely. "
                f"Research proposal summary: {proposal_chunk} "
                f"Ontology: \n {ontology_chunk}"
            ),
            expected_output='A finalized list of potential topmost level concepts or entities',
            tools=[],
            agent=agent,
            output_file=f"ontology_top_level_{proposal_chunk_number}.txt"
        )
    
    def understand_ontology_domain(self, agent):
        return Task(
            description = (
                "Research online and in research literature about the National Survey on Drug Use and Health regarding its domain, scope, what data it collects, and how the data is used. Also, you need to have a general idea of the variables that appear in the datasets in terms of what they represent."
            ),
            expected_output="A paragraph or two that summarizes the domain and scope of the National Survey on Drug Use and Health as well as a list of the main concepts covered in the datasets.",
            tools=[search_tool],
            agent=agent,
            output_file="NSDUH_research.md"
        )
    
    def identify_and_define_classes(self, agent, context):
        return Task(
            description = (
                "Identify the highest level of classes based on the domain and the scope of the ontology. For this, create an ontology built off of the National Survey on Drug Use and Health concepts, topics, and data."
            ),
            expected_output='A list of classes (top 5) with a short description in this format: 1. ClassABC - This class refers to abc and is derived from NSDUH questions regarding abc.',
            tools=[search_tool],
            agent=agent,
            context=context,
            output_file="highest_level_classes_ontology.md"
        )
    
    def identify_and_define_subclasses(self, agent, context):
        return Task(
            description = (
                "Identify and define subclasses of the classes found previously based on the domain and the scope of the ontology. For context, we are creating an ontology built off of the National Survey on Drug Use and Health concepts, topics, and data."
            ),
            expected_output='A list of classes and their corresponding subclasses with a short description in this format: ClassABC/Subclass1 - This subclass refers to abc and is derived from NSDUH questions regarding abc.',
            tools=[search_tool],
            agent=agent,
            context=context,
            output_file="secondary_level_classes_ontology.md"
        )

    def research_owl(self, agent):
        return Task(
            description=("Research the internet to understand what the Web Ontology Language (OWL) is and how to create an ontology in this format."),
            expected_output="A paragraph summarizing your findings as well as a simple OWL formatted ontology (on any topic you choose).",
            tools=[search_tool],
            agent=agent,
            output_file="owl_research.md"
        )
    
    def convert_ontology_to_owl(self, agent, context):
        return Task(
            description=(
                "Formalize the ontology (represented by classes and subclasses) into the Web Ontology Language (OWL)."
            ),
            expected_output="""A correctly formatted, syntactically correct owl file that can be imported into Protegé""",
            tools=[search_tool],
            agent=agent,
            context=context,
            output_file="preliminary_ontology.owl"
        )
    
    def research_topic(self, agent, topic):
        return Task(
            description=(f"Research the topic of {topic} and how it is represented in the National Survey on Drug Use and Health (NSDUH). Can you flesh out this topic into major subtopics?"),
            expected_output="""A text file with a list of subtopics (i.e., 1. FirstTopic, 2. SecondTopic, 3. ThirdTopic, etc.)""",
            tools=[search_tool],
            agent=agent,
            output_file=f"{topic}_subtopics.md"
        )