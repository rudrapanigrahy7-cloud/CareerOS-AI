from google.adk.agents import Agent

internship_agent = Agent(
    name="internship_agent",
    model="gemini-2.5-flash",
    description="Evaluates internship readiness.",
    instruction="""
You are an Internship Agent.

Your responsibilities:
- Evaluate internship readiness
- Identify skill gaps
- Recommend improvements
- Suggest projects and learning paths

Provide structured and actionable feedback.
"""
)
description="Handles internships, resumes, placement preparation and internship readiness."