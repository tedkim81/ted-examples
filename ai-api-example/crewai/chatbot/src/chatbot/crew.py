from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

@CrewBase
class Chatbot():
    """Chatbot crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def chatbot(self) -> Agent:
        return Agent(
            config=self.agents_config['chatbot'],
            verbose=True,
        )

    # @agent
    # def faq_responder(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['faq_responder'],
    #         verbose=True,
    #     )

    # @agent
    # def inquiry_router(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['inquiry_router'],
    #         verbose=True,
    #     )

    @task
    def chat_with_user(self) -> Task:
        return Task(
            config=self.tasks_config['chat_with_user'],
        )

    # @task
    # def respond_to_faq(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['respond_to_faq'],
    #     )

    # @task
    # def route_to_inquiry(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['route_to_inquiry'],
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the Chatbot crew"""

        text_source = TextFileKnowledgeSource(
            file_paths=["faq.txt"],
        )
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[text_source],
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
