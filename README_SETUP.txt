# AI Airdrop Hunter Agent — Flask Web App

## Files
- `app.py`: Flask web dashboard
- `requirements.txt`: Python dependencies
- `Procfile`: production start command for compatible hosts

## Important: prepare main.py
At the bottom of your existing `main.py`, find the code that starts the agent:
```python
projects = discover_projects()
analyze_projects(projects)
show_ranking(projects)
read_report()
show_dashboard(projects)
```
Replace it with this guarded block (indent every line under the `if` by four spaces):
```python
if __name__ == "__main__":
    projects = discover_projects()
    analyze_projects(projects)
    show_ranking(projects)
    read_report()
    show_dashboard(projects)
```
This prevents the command-line program from running automatically when `app.py` imports `main.py`.

## Render settings
- Service type: Web Service
- Runtime: Python
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Choose Free if available.

The app currently displays the existing agent's data and sample fallback. It does not connect wallets or perform transactions. Evidence scores are preliminary indicators only, not security audits.
