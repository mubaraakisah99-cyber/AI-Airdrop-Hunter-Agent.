
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


# 2. VERIFY PROJECT
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


# 3. RECOMMENDATION
def recommend_project(project):
    score = project["safety_score"]
    evidence, status = verify_project(project)

    if score >= 80 and evidence >= 75:
        return "Recommended for Further Review"

    return "Not Recommended Yet"


# 4. DETECT RISK
def detect_risk(project):
    risks = []

    if not project["official_website"]:
        risks.append("No Official Website")

    if not project["official_x"]:
        risks.append("No Official X")

    if not project["documentation"]:
        risks.append("No Documentation")

    if not project["security_review"]:
        risks.append("No Security Review")

    return risks


# 5. RISK LEVEL
def get_risk_level(project):
    risks = detect_risk(project)

    if len(risks) >= 3:
        return "High Risk"
    elif len(risks) >= 1:
        return "Medium Risk"
    else:
        return "Low Risk"


# 6. FINAL REPORT
def generate_report(project):
    evidence, status = verify_project(project)
    risks = detect_risk(project)

    print("\n========== FINAL REPORT ==========")
    print("Project:", project["name"])
    print("Evidence Score:", evidence)
    print("Verification:", status)
    print("Risk Alerts:", risks)
    print("Risk Level:", get_risk_level(project))
    print("Recommendation:", recommend_project(project))
    print("=================================")


# 7. SAVE REPORT
def save_report(projects):
    reports = []

    for project in projects:
        evidence, status = verify_project(project)

        report = {
            "name": project["name"],
            "evidence_score": evidence,
            "risk_level": get_risk_level(project),
            "recommendation": recommend_project(project)
        }

        reports.append(report)

    with open("/tmp/airdrop_report.json", "w") as file:
        json.dump(reports, file, indent=4)

    print("\nReports saved successfully!")


# 8. READ REPORT
def read_report():
    with open("/tmp/airdrop_report.json", "r") as file:
        data = json.load(file)

    print("\nSAVED REPORT")
    print("================")

    for project in data:
        print("Project:", project["name"])
        print("Risk Level:", project["risk_level"])
        print("Recommendation:", project["recommendation"])
        print("----------------")


# 9. DASHBOARD
def show_dashboard(projects):
    low_risk = 0
    medium_risk = 0
    high_risk = 0
    recommended = 0

    for project in projects:
        risk = get_risk_level(project)

        if risk == "Low Risk":
            low_risk += 1
        elif risk == "Medium Risk":
            medium_risk += 1
        elif risk == "High Risk":
            high_risk += 1

        if recommend_project(project) == "Recommended for Further Review":
            recommended += 1

    print("\nAI AIRDROP DASHBOARD")
    print("====================")
    print("Total Projects:", len(projects))
    print("Low Risk:", low_risk)
    print("Medium Risk:", medium_risk)
    print("High Risk:", high_risk)
    print("Recommended:", recommended)


# 10. PROJECT RANKING
def rank_projects(projects):
    return sorted(
        projects,
        key=lambda project: (
            verify_project(project)[0],
            project["safety_score"],
            project["stars"]
        ),
        reverse=True
    )


def show_ranking(projects):
    ranked = rank_projects(projects)

    print("\nAI AIRDROP PROJECT RANKING")
    print("==========================")

    for number, project in enumerate(ranked[:3], start=1):
        score, status = verify_project(project)

        print(number, project["name"], "- Evidence Score:", score)

    if ranked:
        print("\nTOP PROJECT:", ranked[0]["name"])


# 11. MAIN ANALYSIS
def analyze_projects(projects):
    print("AI AIRDROP HUNTER AGENT")
    print("=======================")
    print("Total Projects:", len(projects))

    ranked = rank_projects(projects)

    for project in ranked:
        evidence, status = verify_project(project)

        print("\nProject:", project["name"])
        print("Stars:", project["stars"])
        print("Safety Score:", project["safety_score"])
        print("Evidence Score:", evidence)
        print("Verification:", status)
        print("Recommendation:", recommend_project(project))
        print("Risk Alerts:", detect_risk(project))
        print("Risk Level:", get_risk_level(project))

        generate_report(project)

    save_report(projects)


# 12. START AGENT
analyze_projects(projects)
show_ranking(projects)
read_report()
show_dashboard(projects)

