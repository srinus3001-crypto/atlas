"""
Atlas Studio API
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from atlas.services.mission_launch_service import MissionLaunchService
from atlas.services.mission_service import MissionService
from atlas.services.research_service import ResearchService
from atlas.services.status_service import StatusService

app = FastAPI(title="Atlas Enterprise OS")

app.mount(
    "/static",
    StaticFiles(directory="atlas/static"),
    name="static",
)

templates = Jinja2Templates(directory="atlas/templates")

status_service = StatusService()


@app.get("/")
async def home(request: Request):
    missions = MissionService().list_missions()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "missions": missions,
        },
    )


@app.post("/launch")
async def launch(goal: str = Form(...)):
    MissionLaunchService().launch(goal)

    return RedirectResponse(
        url="/",
        status_code=303,
    )


@app.get("/status/{mission_id}")
async def mission_status(mission_id: str):
    status = status_service.load(mission_id)

    if status is None:
        return JSONResponse(
            status_code=404,
            content={
                "error": "Mission not found",
            },
        )

    return status


@app.get("/mission/{mission_id}", response_class=HTMLResponse)
async def mission_details(mission_id: str):
    report = ResearchService().load_json(mission_id)

    if not report:
        return HTMLResponse(
            "<h1>Research report not found.</h1>",
            status_code=404,
        )

    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Mission {mission_id}</title>

<link rel="stylesheet"
      href="/static/style.css">

<script src="/static/dashboard.js"></script>

</head>

<body onload="startStatusPolling('{mission_id}')">

<div class="content">

<a href="/">← Back to Dashboard</a>

<h1>Mission {mission_id}</h1>

<div class="status-card">

<h2>Progress</h2>

<div class="progress-container">

<div
id="progress"
class="progress-bar">
</div>

</div>

<p id="progressText">

0%

</p>

<h2>Current Stage</h2>

<p id="stage">

Loading...

</p>

<h2>Status</h2>

<p id="message">

Loading...

</p>

</div>

<h1>Research Report</h1>
"""

    titles = {
        "executive_summary": "📋 Executive Summary",
        "market_size": "📊 Market Size",
        "audience_analysis": "👥 Audience Analysis",
        "competitor_analysis": "⚔️ Competitor Analysis",
        "top_opportunities": "🚀 Top Opportunities",
        "revenue_strategy": "💰 Revenue Strategy",
        "risks": "⚠️ Risks",
        "recommended_next_actions": "✅ Recommended Next Actions",
    }

    for key, value in report.items():
        heading = titles.get(
            key,
            key.replace("_", " ").title(),
        )

        html += f"""
<div class="card">

<h2>{heading}</h2>

<p>{value}</p>

</div>
"""

    html += """

</div>

</body>

</html>

"""

    return HTMLResponse(html)
