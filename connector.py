import json
import requests
import os
from fivetran_connector_sdk import Connector

# Load environment variables
FINCH_API_URL = "https://api.tryfinch.com"
FINCH_ACCESS_TOKEN = os.getenv("FINCH_ACCESS_TOKEN")

# Define Finch API headers
def finch_headers():
    return {
        "Authorization": f"Bearer {FINCH_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "Finch-API-Version": "2022-09-17"
    }

# Fetch data from Finch API
def fetch_employees():
    url = f"{FINCH_API_URL}/employer/directory"
    response = requests.get(url, headers=finch_headers())
    response.raise_for_status()
    return response.json()

# Schema definition
def schema(configuration=None):
    schema_output = [
        {
            "table": "employees",
            "primary_key": ["id"],
            "columns": {
                "id": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "middle_name": {"type": "string"},
                "department_name": {"type": "string"},
                "manager_id": {"type": "string"},
                "is_active": {"type": "string"}  # Previously boolean, now string
            }
        }
    ]
    print("\n🔍 DEBUG: Schema Before Returning to Fivetran:")
    print(json.dumps(schema_output, indent=2))
    return schema_output

# Update function
def update(state, records=None, **kwargs):
    if records is None:
        records = []
    
    print("\n📡 Syncing with Fivetran...")
    print(f"Previous State: {state}")
    
    # Simulate fetching data
    data = fetch_employees()
    new_records = []
    
    for employee in data.get("individuals", []):
        new_records.append({
            "id": employee["id"],
            "first_name": employee.get("first_name", ""),
            "last_name": employee.get("last_name", ""),
            "middle_name": employee.get("middle_name", ""),
            "department_name": employee.get("department", {}).get("name", ""),
            "manager_id": employee.get("manager", {}).get("id", ""),
            "is_active": str(employee.get("is_active", "false"))  # Ensure string
        })
    
    new_state = {"last_synced": "now"}
    print("\n🔍 DEBUG: new_state Before Returning:")
    print(json.dumps(new_state, indent=2))
    
    return {"state": new_state, "insert": new_records}

# Initialize the connector
connector = Connector(update=update, schema=schema)

if __name__ == "__main__":
    print("🚀 Running Fivetran Connector...")
    connector.run()
