from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, timedelta
import json

router = APIRouter(tags=['Last N Days CVEs'])

JSON_FILE_PATH = "C:\\Users\\user\\TASK_4\\TASK_4\\src\\data\\known_exploited_vulnerabilities.json"

@router.get("/get/all")
def get_recent_cve(timespan: int = Query(10, description="Number of days to look back (default: 10 days)")):
    try:
        with open(JSON_FILE_PATH, "r") as file:
            data = json.load(file)
        
        vulnerabilities = data.get("vulnerabilities", [])
        start_date = datetime.now() - timedelta(days=timespan)

        recent_cve = [
            cve for cve in vulnerabilities
            if datetime.strptime(cve["dateAdded"], "%Y-%m-%d") >= start_date
        ]


        return recent_cve[:40]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="JSON file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
