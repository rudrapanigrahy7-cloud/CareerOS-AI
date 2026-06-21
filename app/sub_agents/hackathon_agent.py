from google.adk.agents import Agent

hackathon_agent = Agent(
    name="hackathon_agent",
    model="gemini-2.5-flash",
    description="Provides hackathon guidance and project ideas.",
    instruction="""
You are a Hackathon Agent.

Your responsibilities:
- Suggest innovative hackathon ideas
- Recommend technology stacks
- Create execution plans
- Define team roles
- Provide MVP roadmaps

Focus on practical and high-impact projects.
"""
)
description="Handles hackathons, competitions, project ideas, team formation and hackathon strategy."