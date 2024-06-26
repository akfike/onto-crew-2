from crewai import Agent
from langchain_openai import ChatOpenAI


OpenAIModel = ChatOpenAI(
    model="gpt-4-turbo"
)

class OntoAgents():

    def proposal_expert_agent(self):
        return Agent(
            role='Proposal Expert',
            goal='To understand fully what our research objectives are and the purpose of our project.',
            verbose=True,
            memory=True,
            backstory=(
                "You are the expert on the research proposal. You can answer any question regarding its purpose, background, methods, and proposed final product."
            ),
            tools = [],
            allow_delegation=True,
        )
    
    def existing_ontology_researcher(self):
        return Agent(
            role='Researcher of Existing Ontologies',
            goal='Identify reusable existing ontologies that can be used for our project to avoid redundant efforts to make a new ontology.',
            verbose=True,
            memory=True,
            backstory=(
                "With a keen eye for detail, you specialize in exploring and identifying existing ontologies made by reputable organizations to streamline development efforts."
            ),
            tools=[],
            allow_delegation=True
        )
    
    def ontology_expert(self):
        return Agent(
            role="Ontology Expert",
            goal="You are an expert in ontologies in terms of what they are, how they are created, what they should consist of, and how they should be formatted.",
            backstory=(
                "You specialize in researching topics on what ontologies are, ontology development, and ontology development pipelines."
            ),
            verbose=True,
            memory=True,
            tools=[],
            allow_delegation=True
        )
    
    def ontology_evaluator(self):
        return Agent(
            role='Ontology Evaluator',
            goal='Your aim is to identify and correct given list of concepts/entities as relevant to our research proposal so that in the end our ontology has only relevant variables for our research project.',
            verbose=True,
            memory=True,
            backstory=('Decisive and critical, you can decide whether or not each class listed is needed or not in our ontology.'),
            tools=[],
            allow_delegation=True
        )
    
    def dataset_expert(self):
        return Agent(
            role="Dataset Expert",
            goal="Your aim is research on the internet any and all information regarding the dataset introduced in the task.",
            backstory=('You have intimate knowledge of what the dataset is, what data is collected, and the purposes for which the data is to be used.'),
            verbose=True,
            memory=True,
            allow_delegation=True
        )
    
    def ontology_developer(self):
        return Agent(
            role="Ontology Developer",
            goal="Your aim is to be able to identify and define the highest level of classes/concepts of an ontology of a specific domain.",
            backstory=("You are able to generalize and aggregate concepts well in order to form topmost level classes of ontologies."),
            verbose=True,
            memory=True,
            allow_delegation=True
        )
    
    def ontology_subclass_developer(self):
        return Agent(
            role="Ontology Subclass Developer",
            goal="Your aim is to define subclasses of a class in an ontology, considering that a class can have multiple subclasses and a subclass can have multiple superclasses.",
            backstory=("You are able to breakdown classes and concepts into more specific classes and concepts."),
            verbose=True,
            memory=True,
            allow_delegation=True,
        )
    
    def owl_expert(self):
        return Agent(
            role="OWL Expert",
            goal="To research and understand what the Web Ontology Language (OWL) structure is and how to use it to formalize ontologies.",
            backstory=("You are highly knowledge in what OWL is and how it should look. You can generate a correctly formatted OWL file if you needed to."),
            verbose=True,
            memory=True,
            allow_delegation=True,
        )
    
    def owl_conversion_agent(self):
        return Agent(
            role="OWL Conversion Agent",
            goal="Your aim is to represent the classes and subclasses gathered in a formal language, specifically the Web Ontology Language (OWL), that allows automated reasoning.",
            backstory=("You are knowledgeable about the OWL structure and how to convert an ontology into OWL format."),
            verbose=True,
            memory=True,
            allow_delegation=True,
        )
    
    def topic_researcher(self, topic):
        return Agent(
            role=f"{topic} expert",
            goal=f"Your goal is to search on the internet and in research literature the topic of {topic}.",
            backstory=f"Diligently and exhaustively, you search the internet and aggregate information on {topic}",
            verbose=True,
            memory=True,
            tools=[],
            allow_delegation=True,
        )
    
    def entity_identifier(self):
        return Agent(
            role="Entity-relation Detector Assistant",
            goal="Identifying entities and their corresponding relationships in sentences in the efforts to construct an ontology.",
            backstory="You are diligent and thorough and know a lot about ontologies and knowledge graphs.",
            llm=OpenAIModel,
            verbose=True,
            memory=True,
            allow_delegation=False,
        )
    
    def quality_assurance(self):
        return Agent(
            role="Quality Assurance Agent",
            goal="Ensuring the output of the previous task is in the proper format: (Entity 1)->[relation]->(Entity 2), (Entity 2)->[relation]->(Entity 3), (Entity 4)->[relation]->(Entity 1), etc",
            backstory="You are familiar with ontologies and knowledge graphs so you know the importance of structure",
            llm=OpenAIModel,
            verbose=True,
            memory=True,
            allow_delegation=False,
        )
    
    def onto_generator(self):
        return Agent(
            role="Ontology Expert",
            goal="You are to develop an ontology with the given information.",
            backstory="You are intent on making the ontology coherent, general, and simple.",
            llm=OpenAIModel,
            verbose=True,
            memory=True,
            allow_delegation=False
        )
   