
projects = [
    {"name": "Alpha", "stars": 1200},
    {"name": "Beta", "stars": 850},
    {"name": "Gamma", "stars": 2500}
]

def analyze_projects(projects):
    print("AI AIRDROP HUNTER AGENT")
    print("----------------------")

    for project in projects:
        name = project["name"]
        stars = project["stars"]

        print("Project:", name)
        print("Stars:", stars)

        if stars >= 1000:
            print("Priority: High")
        else:
            print("Priority: Normal")

        print("----------------------")

analyze_projects(projects)
