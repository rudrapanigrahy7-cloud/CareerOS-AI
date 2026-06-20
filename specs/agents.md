# CareerOS AI - Agent Architecture

## Overview

CareerOS AI uses a multi-agent architecture built with Google ADK.

A central Orchestrator Agent receives user requests and routes them to specialized agents based on the task.

---

# 1. Orchestrator Agent

## Responsibility

Acts as the central coordinator of the system.

## Input

User query

## Output

Routes request to the appropriate agent.

## Example

User:
"I want internship guidance."

Action:
Route → Internship Agent

---

# 2. Career Strategist Agent

## Responsibility

Create personalized career roadmaps.

## Input

* Student profile
* Skills
* Interests
* Career goals

## Output

* Career roadmap
* Skill recommendations
* Learning plan

## Example

Input:
"I want to become an AI Engineer."

Output:
90-day AI learning roadmap.

---

# 3. Research-to-Project Agent

## Responsibility

Convert research content into practical projects.

## Input

* Research paper
* Article
* Technical documentation

## Output

* Project idea
* Tech stack
* Implementation roadmap
* Milestones

## Example

Input:
Research paper on AI Agents.

Output:
CareerOS AI project blueprint.

---

# 4. Hackathon Agent

## Responsibility

Assist students with hackathon participation.

## Input

* Student profile
* Interests
* Skill level

## Output

* Project ideas
* Team role suggestions
* Execution plan

## Example

Input:
"Suggest a GenAI hackathon project."

Output:
Project concept with roadmap.

---

# 5. Scholarship Agent

## Responsibility

Identify scholarships and assess eligibility.

## Input

* Academic information
* Profile details

## Output

* Scholarship recommendations
* Eligibility assessment
* Application checklist

## Example

Input:
First-year engineering student.

Output:
Matching scholarship opportunities.

---

# 6. Internship Agent

## Responsibility

Evaluate internship readiness.

## Input

* Resume
* Skills
* Projects

## Output

* Readiness score
* Skill gap analysis
* Improvement recommendations

## Example

Input:
Student resume.

Output:
Internship readiness assessment.

---

# Routing Logic

Career Planning
→ Career Strategist Agent

Research Papers
→ Research-to-Project Agent

Hackathons
→ Hackathon Agent

Scholarships
→ Scholarship Agent

Internships
→ Internship Agent

---

# Future Expansion

Additional agents can be added through ADK without modifying existing agents because orchestration is centralized.
