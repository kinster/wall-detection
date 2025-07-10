# VS Code for the Web
source .venv/bin/activate
deactivate
pip install -r requirements.txt
uvicorn app.legend_agent:app --reload --port 8000
uvicorn app.main:app --reload --port 8000
