from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class Demo1():
    
    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def report_generator_agent(self) -> Agent: 
        return Agent(config=self.agents_config["report_generator_agent"])  # type: ignore[index]
    
    @agent
    def blog_writer_agent(self) -> Agent:
        return Agent(config=self.agents_config["blog_writer_agent"])  # type: ignore[index]
    
    @task
    def report_task(self) -> Task:
        return Task(config=self.tasks_config["report_task"])  # type: ignore[index]
    
    @task
    def blog_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_task"],  # type: ignore[index]
            output_file="blog_output.txt"
        )
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )