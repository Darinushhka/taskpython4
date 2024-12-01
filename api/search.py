from fastapi import APIRouter,Query, HTTPException
import json 
import re

router=APIRouter(tags=['Search CVEs'])

JSON_FILE_PATH = "C:\\Users\\user\\TASK_4\\TASK_4\\src\\data\\known_exploited_vulnerabilities.json"

@router.get("/search")
def search(query: str = Query(..., description="Keyword to search for")):
    try:
        with open(JSON_FILE_PATH, "r") as file:
            data = json.load(file)
        
        vulnerabilities = data.get("vulnerabilities", [])

        filtered_cve = [
            cve for cve in vulnerabilities
            if re.search(rf'\b{re.escape(query)}\b', json.dumps(cve), re.IGNORECASE)
        ]

        return filtered_cve
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="JSON file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))