def generate_career_blueprint(
    target_role:str,
    current_year:str,
    current_skills:str,
    weekly_hours:str,
    current_projects:str
) -> str:

    return f"""
==================================================
🚀 CAREEROS INTELLIGENCE REPORT
==================================================

TARGET ROLE
{target_role}

ACADEMIC YEAR
{current_year}

CURRENT SKILLS
{current_skills}

WEEKLY LEARNING HOURS
{weekly_hours}

CURRENT PROJECTS
{current_projects}

==================================================
⚠️ IMPORTANT
==================================================

Use the profile above and create:

1. ROLE DECOMPOSITION

- Core Knowledge Areas
- Core Skills
- Core Tools
- Portfolio Evidence Required

2. CAREER STAGE ANALYSIS

Classify as:
- Explorer
- Builder
- Competitive
- Internship Ready

Explain why.

3. READINESS SCORE

Score:
__/100

Explain reasoning.

4. TOP 3 BOTTLENECKS

Rank them by impact.

5. MISSING EVIDENCE

What proof is missing from the profile?

6. ROLE-SPECIFIC PROJECT ROADMAP

Beginner Project
Intermediate Project
Advanced Project
Flagship Project

7. DETAILED 7-DAY ACTION PLAN

For each day provide:

- Task
- Time Required
- Deliverable
- Why it matters

8. DETAILED 90-DAY EXECUTION PLAN

Month 1
Month 2
Month 3

Include measurable outcomes.

9. OPPORTUNITY STRATEGY

Recommend:
- Communities
- Hackathons
- Competitions
- Internships
- Open Source

10. FINAL RECOMMENDATION

Provide a realistic assessment of how far
the student currently is from becoming
a successful {target_role}.
"""