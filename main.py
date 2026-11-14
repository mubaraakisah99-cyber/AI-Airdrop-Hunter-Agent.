
import json
import urllib.request
import urllib.error
import socket

# 1. Fallback data idan API bai yi aiki ba
fallback_projects = [
    {"name": "Alpha", "stars": 1200,
     "safety_score": 85},
    {"name": "Beta", "stars": 850,
     "safety_score": 60},
    {"name": "Gamma", "stars": 25000,
     "safety_score": 90}
]


# 2. Samo projects daga API
def discover_projects():
    url = (
        "https://api.github.com/search/repositories"
        "?q=airdrop&sort=stars&order=desc&per_page=5"
    )

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "AirdropHunter"}
        )

        with urllib.request.urlopen(
            request, timeout=15
        ) as response:
            data = json.loads(
                response.read().decode("utf-8")
            )

        projects = []

        for item in data["items"]:
            projects.append({
                "name": item["full_name"],
                "stars": item["stargazers_count"],
                "safety_score": None
            })

        print("API Discovery Successful!")
        return projects

    except (
        urllib.error.HTTPError,
        urllib.error.URLError,
        json.JSONDecodeError,
        socket.timeout,
        KeyError
    ) as error:

        print("API Error:", error)
        print("Using fallback data...")

        return fallback_projects


# 3. Rank projects
def rank_projects(projects):
    return sorted(
        projects,
        key=lambda project: (
            project["safety_score"]
            if project["safety_score"] is not None
            else -1,
            project["stars"]
        ),
        reverse=True
    )


# 4. Recommendation
def recommend_project(project):
    score = project["safety_score"]

    if score is not None and (
        project["stars"] >= 1000
        and score >= 80
    ):
        return "Recommended for further review"

    return "Not Verified - Review Required"


# 5. Analyze projects
def analyze_projects(projects):

    print("\nAI AIRDROP HUNTER AGENT")
    print("=======================")
    print("Total Projects:", len(projects))
    print("-----------------------")

    ranked = rank_projects(projects)

    for project in ranked:

        print("Project:", project["name"])
        print("Stars:", project["stars"])

        if project["stars"] >= 20000:
            print("Priority: High")
        else:
            print("Priority: Normal")

        score = project["safety_score"]

        if score is None:
            print("Safety Score: Not Verified")
            print("Safety: Unknown")
        elif score >= 80:
            print("Safety: Passed Screening")
        else:
            print("Safety: Needs Review")

        print(
            "Recommendation:",
            recommend_project(project)
        )

        print("-----------------------")


# 6. Start Agent
projects = discover_projects()
analyze_projects(projects)
