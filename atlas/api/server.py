"""
Atlas Studio API
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from atlas.services.mission_service import MissionService
from atlas.services.research_service import ResearchService

app = FastAPI(title="Atlas Enterprise OS")

app.mount(
    "/static",
    StaticFiles(directory="atlas/static"),
    name="static",
)

templates = Jinja2Templates(directory="atlas/templates")


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


@app.get("/mission/{mission_id}", response_class=HTMLResponse)
async def mission_details(mission_id: str):
    report = ResearchService().load_markdown(mission_id)

    return f"""<!DOCTYPE html>
<html>
<head>
<title>{mission_id}</title>

<style>
body {{
    font-family: Arial, Helvetica, sans-serif;
    background: #111827;
    color: white;
    padding: 40px;
}}

h1 {{
    color: #60a5fa;
}}

pre {{
    white-space: pre-wrap;
    background: #1f2937;
    padding: 20px;
    border-radius: 10px;
}}

a {{
    color: #60a5fa;
}}
</style>

</head>

<body>

<a href="/">← Back</a>

<h1>Mission {mission_id}</h1>

<pre>{report}</pre>

</body>
</html>"""
