
projects = [
    {
        "name": "Alpha",
        "stars": 1200,
        "safety_score": 85
    },
    {
        "name": "Beta",
        "stars": 850,
        "safety_score": 60
    },
    {
        "name": "Gamma",
        "stars": 2500,
        "safety_score": 90
    }
]


def analyze_projects(projects):
    print("AI AIRDROP HUNTER AGENT")
    print("=======================")

    for project in projects:
        name = project["name"]
        stars = project["stars"]
        score = project["safety_score"]

        if stars >= 1000:
            priority = "High"
        else:
            priority = "Normal"

        if score >= 80:
            safety = "Safe Indicator"
        else:
            safety = "Low Indicator"

        print("Project:", name)
        print("Stars:", stars)
        print("Priority:", priority)
        print("Safety Score:", score)
        print("Safety:", safety)
        print("-----------------------")


analyze_projects(projects)
