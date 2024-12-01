from fastapi import APIRouter, HTTPException
import json 

router=APIRouter(tags=['Known Ransomware СVEs'])

JSON_FILE_PATH = "C:\\Users\\user\\TASK_4\\TASK_4\\src\\data\\known_exploited_vulnerabilities.json"

@router.get("/get/known")
def get_known():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            data = json.load(file)
        
        vulnerabilities = data.get("vulnerabilities", [])

        known_cve = [
            cve for cve in vulnerabilities
            if cve.get("knownRansomwareCampaignUse") == "Known"
        ]

        return known_cve[:10]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="JSON file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))