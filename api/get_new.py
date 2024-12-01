from fastapi import APIRouter, HTTPException
import json 

router=APIRouter(tags=['10 Latest CVEs'])

JSON_FILE_PATH = "C:\\Users\\user\\TASK_4\\TASK_4\\src\\data\\known_exploited_vulnerabilities.json"

@router.get("/get/new")

def get_new():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            data = json.load(file)
        
        vulnerabilities = data.get("vulnerabilities", [])

        sorted_cve = sorted(
            vulnerabilities,
            key=lambda x: x.get("dateAdded", ""),
            reverse=True
        )

        return sorted_cve[:10]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="JSON file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))