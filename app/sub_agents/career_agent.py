from google.adk.agents import Agent

career_agent = Agent(
    name="career_agent",
    model="gemini-2.5-flash",
    description="Provides career planning and roadmap guidance for students.",
    instruction="""
You are a Career Strategist Agent.

Your responsibilities:
- Create personalized career roadmaps
- Recommend skills to learn
- Suggest learning resources
- Provide milestone-based growth plans

Always give structured and actionable advice.
"""
)
description="Handles career planning, skill roadmaps and long-term professional growth."