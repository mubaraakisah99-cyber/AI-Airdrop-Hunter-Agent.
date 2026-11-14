
import json

# 1. PROJECT DATA
projects = [
    {
        "name": "Alpha",
        "stars": 1200,
        "safety_score": 85,
        "official_website": True,
        "official_x": True,
        "documentation": True,
        "security_review": False
    },
    {
        "name": "Beta",
        "stars": 850,
        "safety_score": 60,
        "official_website": False,
        "official_x": True,
        "documentation": False,
        "security_review": False
    },
    {
        "name": "Gamma",
        "stars": 25000,
        "safety_score": 90,
        "official_website": True,
        "official_x": True,
        "documentation": True,
        "security_review": True
    },
    {
        "name": "Delta",
        "stars": 5000,
        "safety_score": 95,
        "official_website": True,
        "official_x": False,
        "documentation": True,
        "security_review": False
    }
]


# 2. PROJECT RANKING
def rank_projects(projects):
    return sorted(
        projects,
        key=lambda p: (
            p["safety_score"],
            p["stars"]
        ),
        reverse=True
    )


# 3. PROJECT VERIFICATION
def verify_project(project):

    score = 0

    checks = [
        "official_website",
        "official_x",
        "documentation",
        "security_review"
    ]

    for check in checks:
        if project.get(check) is True:
            score += 25

    if score >= 75:
        status = "More Evidence Available"
    elif score >= 50:
        status = "Needs More Review"
    else:
        status = "Insufficient Evidence"

    return score, status


# 4. RECOMMENDATION
def recommend_project(project):

    score = project["safety_score"]
    evidence, status = verify_project(project)

    if score >= 80 and evidence >= 75:
        return "Recommended for Further Review"

    return "Not Recommended Yet"


# 5. MAIN ANALYSIS
def analyze_projects(projects):

    print("AI AIRDROP HUNTER AGENT")
    print("=======================")

    print("Total Projects:", len(projects))
    print("-----------------------")

    ranked = rank_projects(projects)

    for project in ranked:

        evidence, status = verify_project(project)

        print("Project:", project["name"])
        print("Stars:", project["stars"])
        print("Safety Score:", project["safety_score"])
        print("Evidence Score:", evidence)
        print("Verification:", status)
        print(
            "Recommendation:",
            recommend_project(project)
        )
        print("-----------------------")


# 6. START AGENT
analyze_projects(projects)
