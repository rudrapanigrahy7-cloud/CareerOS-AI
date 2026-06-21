def analyze_internship_readiness(
    target_role: str,
    current_skills: str,
    projects: str,
    github_status: str,
    resume_status: str
) -> str:

    return f"""
==================================================
 CAREEROS INTERNSHIP READINESS ENGINE
==================================================

Target Role:
{target_role}

==================================================
 CURRENT PROFILE
==================================================

Skills:
{current_skills}

Projects:
{projects}

GitHub:
{github_status}

Resume:
{resume_status}

==================================================
 READINESS ASSESSMENT
==================================================

Current Stage:

BEGINNER
→ Learning fundamentals

DEVELOPING
→ Building projects

COMPETITIVE
→ Applying actively

INTERVIEW READY
→ Strong candidate profile

Based on your provided profile,
you are progressing toward becoming
a competitive {target_role} candidate.

==================================================
 GAP ANALYSIS
==================================================

Areas evaluated:

✓ Technical Skills
✓ Projects
✓ GitHub Presence
✓ Resume Quality
✓ Professional Visibility

Potential Gaps:

1. Skill Gap
Are your skills aligned with the target role?

2. Project Gap
Do you have portfolio-worthy projects?

3. GitHub Gap
Can recruiters see your work?

4. Resume Gap
Can your resume communicate value?

5. Experience Gap
Do you have internships, hackathons,
research or open-source contributions?

==================================================
 BOTTLENECK DETECTION
==================================================

Most students do NOT fail because of
lack of courses.

They fail because of:

• No public portfolio
• Weak projects
• Generic resume
• Lack of applications

Identify and fix the biggest bottleneck first.

==================================================
 INTERNSHIP COMPETITIVENESS
==================================================

Recruiters typically look for:

✓ Relevant Skills
✓ Strong Projects
✓ GitHub Activity
✓ Resume Quality
✓ Communication Skills

Your goal is not to complete courses.

Your goal is to become demonstrably valuable.

==================================================
 PROJECT RECOMMENDATIONS
==================================================

Recommended Project Categories:

1. Portfolio Project
A project showcasing your strongest skills.

2. Real-World Problem Project
A project solving a practical problem.

3. Advanced Showcase Project
Something that demonstrates innovation.

Examples:

• Multi-Agent Systems
• Resume Analyzer
• CareerOS AI
• Research Assistant
• AI Productivity Tools

==================================================
 RESUME IMPROVEMENT CHECKLIST
==================================================

✓ Quantify achievements

✓ Add project impact

✓ Add GitHub links

✓ Highlight technical stack

✓ Highlight leadership experience

✓ Highlight hackathons

==================================================
 GITHUB IMPROVEMENT CHECKLIST
==================================================

✓ Public repositories

✓ Professional README

✓ Clear documentation

✓ Project screenshots

✓ Consistent commits

==================================================
 NEXT 30-DAY EXECUTION PLAN
==================================================

WEEK 1

• Assess current profile
• Identify biggest bottleneck
• Optimize GitHub

Deliverable:
Improved online presence

--------------------------------------------------

WEEK 2

• Build mini project
• Improve existing project

Deliverable:
Portfolio improvement

--------------------------------------------------

WEEK 3

• Update resume
• Create LinkedIn profile
• Publish project documentation

Deliverable:
Professional profile

--------------------------------------------------

WEEK 4

• Start internship applications
• Participate in hackathons
• Network with peers

Deliverable:
Application-ready profile

==================================================
 INTERNSHIP STRATEGY
==================================================

Focus Order:

1. Skills
2. Projects
3. GitHub
4. Resume
5. Applications

Many students reverse this order.

Do not apply first.

Become competitive first.

==================================================
 CAREEROS FINAL RECOMMENDATION
==================================================

Ask yourself:

"If a recruiter saw my GitHub,
resume and projects today,
would they be impressed?"

If the answer is no,

Build.
Document.
Publish.
Apply.

That is the fastest path toward your
first internship as a {target_role}.
"""