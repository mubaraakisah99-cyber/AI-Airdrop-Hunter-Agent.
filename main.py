
import json

json_data = '''
[
    {"name": "Alpha", "stars": 1200, "safety_score": 85},
    {"name": "Beta", "stars": 850, "safety_score": 60},
    {"name": "Gamma", "stars": 2500, "safety_score": 90}
]
'''

projects = json.loads(json_data)


def rank_projects(projects):
    return sorted(
        projects,
        key=lambda project: project["stars"],
        reverse=True
    )


def recommend_project(project):
    if project["stars"] >= 1000 and project["safety_score"] >= 80:
        return "Recommended"
    else:
        return "Not Recommended"


def analyze_projects(projects):
    print("AI AIRDROP HUNTER AGENT")
    print("=======================")

    ranked_projects = rank_projects(projects)

    for project in ranked_projects:
        name = project["name"]
        stars = project["stars"]
        score = project["safety_score"]

        if stars >= 20000:
            priority = "High"
        else:
            priority = "Normal"

        if score >= 80:
            safety = "Safe Indicator"
        else:
            safety = "Low Indicator"

        recommendation = recommend_project(project)

        print("Project:", name)
        print("Stars:", stars)
        print("Priority:", priority)
        print("Safety Score:", score)
        print("Safety:", safety)
        print("Recommendation:", recommendation)
        print("-----------------------")


analyze_projects(projects)


