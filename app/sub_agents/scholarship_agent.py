from google.adk.agents import Agent

scholarship_agent = Agent(
    name="scholarship_agent",
    model="gemini-2.5-flash",
    description="Finds scholarships and evaluates eligibility.",
    instruction="""
You are a Scholarship Agent.

Your responsibilities:
- Identify scholarships
- Assess eligibility
- Provide application guidance
- Create application checklists

Always explain eligibility clearly.
"""
)
description="Handles scholarships, grants, fellowships, financial aid, student funding and eligibility checks."