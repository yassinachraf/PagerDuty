# Bulk Create Services

This repository contains a script to bulk create services in PagerDuty using CSV files. The script reads the CSV files, fetches necessary escalation policies, and creates services based on the provided data.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/)

## Setup

### 1. Clone the repository or download the files

Ensure you have the following files in the same directory:
- `bulk_create_services.py`
- `config.py`
- One or more CSV files with service data (e.g., `services1.csv`, `services2.csv`)

### 2. Open the directory in VS Code

1. Launch VS Code.
2. Open the directory containing the script files (`bulk_create_services.py`, `config.py`, and the CSV files) in VS Code.

### 3. Install required Python packages

1. Open the terminal in VS Code by clicking on `Terminal` > `New Terminal`.
2. Ensure you have Python installed. You can check by running:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```
   If Python is not installed, download and install it from [Python.org](https://www.python.org/downloads/).

3. Install the required Python packages by running:
   ```bash
   pip install pandas requests
   ```

### 4. Configure your API key

1. Open the `config.py` file.
2. Replace `'your_pagerduty_api_key_here'` with your actual PagerDuty API key.

### 5. Run the script

1. In the terminal, run the script:
   ```bash
   python bulk_create_services.py
   ```
   or
   ```bash
   python3 bulk_create_services.py
   ```

### Example CSV File (`services.csv`)

The CSV file should have the following structure:

```csv
type,name,description,auto_resolve_timeout,incident_urgency_rule,teams,alert_creation
service,My Web App,My cool web application that does things,14400,high,Engineering,create_alerts_and_incidents
service,Another Web App,This cool web application that does more things,10800,low,Support,create_alerts_and_incidents
service,My Best Web App,My cool web application that does all of the things,3600,high,Development,create_alerts_and_incidents
```

## Troubleshooting

- **Error: "No CSV files found in the directory"**:
  - Ensure that there are CSV files in the directory where you are running the script.

- **Error: "command not found: python"**:
  - Ensure you are using `python` or `python3` depending on your Python installation.
  - Ensure Python is installed and correctly configured in your PATH.

- **Error fetching escalation policies**:
  - Verify that your API key is correct and has the necessary permissions.

- **Error creating service**:
  - Ensure the CSV file is correctly formatted.
  - Verify that your API key is correct and has the necessary permissions.

If you encounter any other issues, please check the error messages for more details and ensure that your setup matches the prerequisites.

## Contact

For further assistance, please contact support@pagerduty.com.