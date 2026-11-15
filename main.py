
import json
import urllib.request
import urllib.error
import urllib.parse


# 1. SAMPLE PROJECT DATA

projects = [
    {
        "name": "Alpha",
        "stars": 1200,
        "safety_score": 85,
        "official_website": True,
        "website_url": "",
        "official_x": True,
        "documentation": True,
        "security_review": False
    },
    {
        "name": "Beta",
        "stars": 850,
        "safety_score": 60,
        "official_website": False,
        "website_url": "",
        "official_x": True,
        "documentation": False,
        "security_review": False
    },
    {
        "name": "Gamma",
        "stars": 25000,
        "safety_score": 90,
        "official_website": True,
        "website_url": "",
        "official_x": True,
        "documentation": True,
        "security_review": True
    },
    {
        "name": "Delta",
        "stars": 5000,
        "safety_score": 95,
        "official_website": True,
        "website_url": "",
        "official_x": False,
        "documentation": True,
        "security_review": False
    }
]


# 2. DISCOVER PROJECTS

def discover_projects():

    url = (
        "https://api.github.com/search/repositories"
        "?q=airdrop+blockchain"
        "&sort=stars&order=desc&per_page=10"
    )

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Airdrop-Hunter"}
    )

    try:
        with urllib.request.urlopen(
            request, timeout=12
        ) as response:

            data = json.loads(
                response.read().decode("utf-8")
            )

        new_projects = []

        for item in data.get("items", []):

            new_projects.append({
                "name": item.get("full_name", "Unknown"),
                "stars": item.get("stargazers_count", 0),
                "safety_score": 0,
                "official_website": False,
                "website_url": item.get("homepage") or "",
                "official_x": False,
                "documentation": False,
                "security_review": False
            })

        if not new_projects:
            raise ValueError("No projects found")

        print("API Discovery Successful!")

        return new_projects

    except Exception as error:

        print("API Error:", error)
        print("Using existing sample projects...")

        return projects


# 3. VERIFY PROJECT EVIDENCE

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


# 4. SHOW EVIDENCE DETAILS

def show_evidence_details(project):

    checks = {
        "Official Website": "official_website",
        "Official X": "official_x",
        "Documentation": "documentation",
        "Security Review": "security_review"
    }

    print("\nEVIDENCE VERIFICATION")
    print("---------------------")

    for name, key in checks.items():

        if project.get(key) is True:
            print(name + ": Marked Available")

        else:
            print(name + ": Needs Verification")


# 5. RECOMMENDATION

def recommend_project(project):

    score = project.get("safety_score", 0)

    evidence, status = verify_project(project)

    if score >= 80 and evidence >= 75:

        return "Candidate for Further Review"

    return "Not Recommended Yet"


# 6. DETECT EVIDENCE GAPS

def detect_risk(project):

    risks = []

    checks = {
        "official_website": "No Official Website Evidence",
        "official_x": "No Official X Evidence",
        "documentation": "No Documentation",
        "security_review": "No Security Review"
    }

    for key, message in checks.items():

        if project.get(key) is not True:
            risks.append(message)

    return risks


# 7. EVIDENCE GAP LEVEL

def get_risk_level(project):

    risks = detect_risk(project)

    if len(risks) >= 3:
        return "Many Evidence Gaps"

    elif len(risks) >= 1:
        return "Some Evidence Gaps"

    return "No Listed Evidence Gaps"


# 8. WEBSITE CHECKER

def check_website(project):

    url = project.get("website_url", "")

    if not url:
        return "No Website URL Provided"

    parsed = urllib.parse.urlparse(url)

    if parsed.scheme != "https" or not parsed.netloc:
        return "Invalid Website URL"

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Airdrop-Hunter"}
    )

    try:

        with urllib.request.urlopen(
            request, timeout=10
        ) as response:

            return "Website Responding"

    except urllib.error.HTTPError as error:

        return "HTTP Error: " + str(error.code)

    except urllib.error.URLError as error:

        if isinstance(error.reason, TimeoutError):
            return "Connection Timeout - Cannot Verify"

        return "Network Unavailable - Cannot Verify"

    except TimeoutError:

        return "Connection Timeout - Cannot Verify"


# 9. FINAL REPORT

def generate_report(project):

    evidence, status = verify_project(project)

    risks = detect_risk(project)

    print("\n========== FINAL REPORT ==========")

    print("Project:", project["name"])

    print("Evidence Score:", evidence)

    print("Evidence Status:", status)

    print("Website Status:", check_website(project))

    show_evidence_details(project)

    print("Evidence Gaps:", risks)

    print("Gap Level:", get_risk_level(project))

    print("Recommendation:", recommend_project(project))

    print("=================================")


# 10. SAVE REPORT

def save_report(projects):

    reports = []

    for project in projects:

        evidence, status = verify_project(project)

        report = {
            "name": project["name"],
            "evidence_score": evidence,
            "evidence_status": status,
            "gap_level": get_risk_level(project),
            "recommendation": recommend_project(project)
        }

        reports.append(report)

    with open("/tmp/airdrop_report.json", "w") as file:

        json.dump(reports, file, indent=4)

    print("\nReports saved successfully!")


# 11. READ REPORT

def read_report():

    try:

        with open("/tmp/airdrop_report.json", "r") as file:

            data = json.load(file)

        print("\nSAVED REPORT")
        print("================")

        for project in data:

            print("Project:", project["name"])

            print("Gap Level:", project["gap_level"])

            print("Recommendation:", project["recommendation"])

            print("----------------")

    except (OSError, json.JSONDecodeError) as error:

        print("Report Read Error:", error)


# 12. DASHBOARD

def show_dashboard(projects):

    few_gaps = 0
    some_gaps = 0
    many_gaps = 0
    recommended = 0

    for project in projects:

        gap = get_risk_level(project)

        if gap == "No Listed Evidence Gaps":
            few_gaps += 1

        elif gap == "Some Evidence Gaps":
            some_gaps += 1

        elif gap == "Many Evidence Gaps":
            many_gaps += 1

        if recommend_project(project) == "Candidate for Further Review":
            recommended += 1

    print("\nAI AIRDROP DASHBOARD")
    print("====================")

    print("Total Projects:", len(projects))

    print("No Listed Gaps:", few_gaps)

    print("Some Evidence Gaps:", some_gaps)

    print("Many Evidence Gaps:", many_gaps)

    print("Candidates for Further Review:", recommended)


# 13. PROJECT RANKING

def rank_projects(projects):

    return sorted(
        projects,
        key=lambda project: (
            verify_project(project)[0],
            project.get("stars", 0)
        ),
        reverse=True
    )


def show_ranking(projects):

    ranked = rank_projects(projects)

    print("\nAI AIRDROP PROJECT RANKING")
    print("==========================")

    for number, project in enumerate(ranked[:3], start=1):

        score, status = verify_project(project)

        print(
            number,
            project["name"],
            "- Evidence Score:",
            score
        )

    if ranked:

        print("\nTOP PROJECT:", ranked[0]["name"])


# 14. MAIN ANALYSIS

def analyze_projects(projects):

    print("AI AIRDROP HUNTER AGENT")
    print("=======================")

    print("Total Projects:", len(projects))

    ranked = rank_projects(projects)

    for project in ranked:

        evidence, status = verify_project(project)

        print("\nProject:", project["name"])

        print("Stars:", project.get("stars", 0))

        print("Safety Score:", project.get("safety_score", 0))

        print("Evidence Score:", evidence)

        print("Evidence Status:", status)

        print("Recommendation:", recommend_project(project))

        print("Evidence Gaps:", detect_risk(project))

        print("Gap Level:", get_risk_level(project))

        generate_report(project)

    save_report(projects)


# 15. START AGENT

projects = discover_projects()

analyze_projects(projects)

show_ranking(projects)

read_report()

show_dashboard(projects)
