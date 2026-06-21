def analyze_student_profile(
    academic_year: str,
    branch: str,
    target_role: str,
    current_skills: str,
    current_projects: str,
    github_status: str,
    resume_status: str,
    weekly_hours: str
) -> str:

    return f"""
==================================================
 CAREEROS PROFILE ANALYZER
==================================================

ACADEMIC YEAR
{academic_year}

BRANCH
{branch}

TARGET ROLE
{target_role}

CURRENT SKILLS
{current_skills}

CURRENT PROJECTS
{current_projects}

GITHUB STATUS
{github_status}

RESUME STATUS
{resume_status}

WEEKLY LEARNING HOURS
{weekly_hours}

==================================================
 CAREER STAGE
==================================================

Explorer
→ Learning fundamentals

Builder
→ Building projects

Competitive
→ Developing portfolio

Internship Ready
→ Ready for opportunities

Career Ready
→ Strong professional profile

Based on your profile,
you are currently progressing toward becoming a
{target_role}.

==================================================
 STRENGTH ANALYSIS
==================================================

Potential strengths include:

✓ Existing technical skills

✓ Interest in career development

✓ Learning commitment

✓ Project-building potential

==================================================
 WEAKNESS ANALYSIS
==================================================

Common growth areas:

• Portfolio depth

• Real-world projects

• GitHub visibility

• Resume quality

• Industry exposure

==================================================
 BOTTLENECK DETECTION
==================================================

Your highest priority bottleneck is the area
creating the greatest gap between your current
profile and your target role.

Focus on fixing ONE bottleneck at a time.

==================================================
 RECOMMENDED AGENT
==================================================

Career Agent
→ If direction is unclear

Research Agent
→ If projects are missing

Internship Agent
→ If employability is the focus

==================================================
 NEXT 30-DAY PRIORITY
==================================================

Week 1
• Profile assessment

Week 2
• Build or improve projects

Week 3
• Improve GitHub and resume

Week 4
• Apply skills in real opportunities

==================================================
 CAREEROS SUMMARY
==================================================

Current Goal:
{target_role}

Current Focus:

Learn
↓
Build
↓
Publish
↓
Apply

Execution creates opportunities.
"""