from google.adk.agents import Agent

from app.sub_agents.profile_agent import profile_agent
from app.sub_agents.career_agent import career_agent
from app.sub_agents.research_agent import research_agent
from app.sub_agents.hackathon_agent import hackathon_agent
from app.sub_agents.scholarship_agent import scholarship_agent
from app.sub_agents.internship_agent import internship_agent

root_agent = Agent(
    name="careeros_orchestrator",
    model="gemini-2.5-flash",
    description="Main orchestrator for CareerOS AI",

    sub_agents=[
        profile_agent,
        career_agent,
        research_agent,
        hackathon_agent,
        scholarship_agent,
        internship_agent
    ],

    instruction="""
You are the CareerOS AI Orchestrator.

Route requests as follows:

Profile analysis, strengths, weaknesses,
career assessment, career stage,
student profile evaluation
→ profile_agent

Career planning, learning roadmap,
skill development, role transition,
90-day plans, career strategy
→ career_agent

Research papers, research topics,
research-to-project conversion,
portfolio project ideas
→ research_agent

Hackathons, competitions, project ideas
→ hackathon_agent

Scholarships, funding opportunities
→ scholarship_agent

Internships, resume review,
GitHub review, employability,
career readiness, internship preparation
→ internship_agent

Always route to the most relevant agent.
"""
)