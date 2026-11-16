
from flask import Flask, render_template_string
import main as agent

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Airdrop Hunter Agent</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    background: #0b1220;
    color: #edf2ff;
    font-family: Arial, sans-serif;
}

main {
    max-width: 1050px;
    margin: auto;
    padding: 24px 16px;
}

header { padding: 20px 0; }

h1 {
    font-size: clamp(27px, 5vw, 42px);
    margin: 10px 0;
}

.muted {
    color: #aab6cc;
    line-height: 1.5;
}

.pill {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 20px;
    background: #23314c;
    color: #cfe0ff;
    font-size: 12px;
}

.stats, .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 14px;
}

.stat, .card {
    background: #131f33;
    border: 1px solid #293750;
    border-radius: 14px;
    padding: 16px;
}

.stat strong {
    display: block;
    font-size: 28px;
    margin-top: 8px;
}

.cards { margin-top: 14px; }

.card h2 {
    font-size: 20px;
    margin: 0 0 12px;
    overflow-wrap: anywhere;
}

.line {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin: 9px 0;
    color: #c6d1e3;
}

.score {
    font-size: 24px;
    font-weight: bold;
    color: #9ed5ff;
}

.warning {
    border-left: 3px solid #d6a84c;
    padding: 12px;
    margin-top: 18px;
    background: #1b2638;
    color: #dce5f3;
}

footer {
    margin-top: 26px;
    color: #93a3bd;
    font-size: 13px;
}
</style>
</head>

<body>
<main>

<header>
<span class="pill">EARLY DEMO</span>
<h1>AI Airdrop Hunter Agent</h1>
<p class="muted">
A preliminary evidence-screening dashboard.
It organizes public project information; it does not certify projects as safe.
</p>
</header>

<section class="stats">

<div class="stat">
Projects scanned
<strong>{{ projects|length }}</strong>
</div>

<div class="stat">
No listed evidence gaps
<strong>{{ no_gaps }}</strong>
</div>

<div class="stat">
Some evidence gaps
<strong>{{ some_gaps }}</strong>
</div>

<div class="stat">
Many evidence gaps
<strong>{{ many_gaps }}</strong>
</div>

<div class="stat">
Unverified Projects
<strong>{{ unverified_projects }}</strong>
</div>

</section>

<h2 style="margin-top:28px">Project ranking</h2>

<section class="cards">

{% for p in projects %}

<article class="card">

<h2>{{ p.name }}</h2>

<div class="line">
<span>Evidence score</span>
<span class="score">{{ p.score }}/100</span>
</div>

<div class="line">
<span>GitHub stars</span>
<span>{{ p.stars }}</span>
</div>

<div class="line">
<span>Evidence gaps</span>
<span>{{ p.gap_count }}</span>
</div>

<div class="line">
<span>Gap level</span>
<span>{{ p.gap_level }}</span>
</div>

<div class="line">
<span>Recommendation</span>
<span>{{ p.recommendation }}</span>
</div>

<p class="muted">
<strong>Evidence Gaps:</strong>
{{ p.gaps|join(", ") if p.gaps else "No confirmed evidence gaps" }}
</p>

<p class="muted">
<strong>Unverified Evidence:</strong>
{{ p.unverified_evidence|join(", ") if p.unverified_evidence else "All listed items checked" }}
</p>

</article>

{% endfor %}

</section>

<div class="warning">
<strong>Important:</strong>
Evidence scores are not security audits.
GitHub stars measure popularity, not trustworthiness.
Unverified information does not prove a project is fraudulent.
Never share wallet recovery phrases or private keys.
</div>

<footer>
AI Airdrop Hunter Agent · Demo build ·
Data may use sample projects if the GitHub API is unavailable.
</footer>

</main>
</body>
</html>
"""


@app.route("/")
def home():

    source_projects = agent.discover_projects()
    ranked = agent.rank_projects(source_projects)

    rows = []

    for project in ranked:

        score, _ = agent.verify_project(project)
        gaps = agent.detect_risk(project)
        unverified = agent.get_unverified_evidence(project)

        rows.append({
            "name": project.get("name", "Unknown"),
            "stars": project.get("stars", 0),
            "score": score,
            "gaps": gaps,
            "gap_count": len(gaps),
            "unverified_evidence": unverified,
            "unverified_count": len(unverified),
            "gap_level": agent.get_risk_level(project),
            "recommendation": agent.recommend_project(project),
        })

    return render_template_string(
        PAGE,
        projects=rows,
        no_gaps=sum(
            1 for p in rows if p["gap_count"] == 0
        ),
        some_gaps=sum(
            1 for p in rows if 1 <= p["gap_count"] <= 2
        ),
        many_gaps=sum(
            1 for p in rows if p["gap_count"] >= 3
        ),
        unverified_projects=sum(
            1 for p in rows if p["unverified_count"] > 0
        ),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
