# Example: Research Crew for market analysis
from crewai import Agent, Crew, Process, Task
import os
import sys

if "MODEL" not in os.environ or "OPENAI_API_KEY" not in os.environ:
    print("환경 변수 MODEL 또는 OPENAI_API_KEY가 설정되지 않았습니다.")
    sys.exit(0)

# Create specialized agents
researcher = Agent(
    role="Market Research Specialist",
    goal="Find comprehensive market data on emerging technologies",
    backstory="You are an expert at discovering market trends and gathering data."
)

analyst = Agent(
    role="Market Analyst",
    goal="Analyze market data and identify key opportunities",
    backstory="You excel at interpreting market data and spotting valuable insights."
)

# Define their tasks
research_task = Task(
    description="Research the current market landscape for AI-powered healthcare solutions",
    expected_output="Comprehensive market data including key players, market size, and growth trends",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the market data and identify the top 3 investment opportunities",
    expected_output="Analysis report with 3 recommended investment opportunities and rationale",
    agent=analyst,
    context=[research_task]
)

# Create the crew
market_analysis_crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    process=Process.sequential,
    verbose=True
)

# Run the crew
result = market_analysis_crew.kickoff()

print(result)
