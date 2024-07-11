import pandas as pd
import requests
import json
import glob
from config import PAGERDUTY_API_KEY, SERVICE_FIELDS

# Use the API key from the config module
api_key = PAGERDUTY_API_KEY

# Base URL for the API
base_url = "https://api.pagerduty.com"

# Headers for authentication
headers = {
    "Authorization": f"Token token={api_key}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.pagerduty+json;version=2"
}

# Function to get the list of escalation policies
def get_escalation_policies():
    url = f"{base_url}/escalation_policies"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        policies = response.json().get('escalation_policies', [])
        if policies:
            return policies[0]['id']  # Return the first escalation policy ID
    print(f"Error fetching escalation policies: {response.status_code} - {response.text}")
    return None

# Get the default escalation policy ID
default_escalation_policy_id = get_escalation_policies()

if not default_escalation_policy_id:
    print("No escalation policy found.")
    exit(1)

# Function to create a service
def create_service(service_data):
    url = f"{base_url}/services"
    
    # Create the payload from the service data
    payload = {"service": {}}

    for field in SERVICE_FIELDS:
        if field in service_data and pd.notna(service_data[field]):
            if field == "incident_urgency_rule":
                payload["service"][field] = {
                    "type": "use_support_hours",
                    "during_support_hours": {
                        "type": "constant",
                        "urgency": service_data.get("incident_urgency_rule", "high")
                    },
                    "outside_support_hours": {
                        "type": "constant",
                        "urgency": service_data.get("incident_urgency_rule", "low")
                    }
                }
            elif field == "escalation_policy":
                payload["service"][field] = {"id": default_escalation_policy_id, "type": "escalation_policy_reference"}
            else:
                payload["service"][field] = service_data[field]
    
    # Set default values for required fields if not provided
    payload["service"].setdefault("escalation_policy", {"id": default_escalation_policy_id, "type": "escalation_policy_reference"})
    payload["service"].setdefault("status", "active")
    payload["service"].setdefault("acknowledgement_timeout", 600)

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print(f"Service '{service_data['name']}' created successfully.")
    else:
        print(f"Error creating service '{service_data['name']}']: {response.status_code} - {response.text}")

# Find all CSV files in the directory
csv_files = glob.glob("*.csv")
if not csv_files:
    print("No CSV files found in the directory.")
    exit(1)

# Process each CSV file individually
for csv_file in csv_files:
    print(f"Processing file: {csv_file}")
    services_df = pd.read_csv(csv_file)
    for index, row in services_df.iterrows():
        create_service(row)

print("All services from all files have been processed.")
