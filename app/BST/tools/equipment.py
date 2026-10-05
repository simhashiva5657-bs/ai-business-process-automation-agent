import json
from pathlib import Path
from datetime import datetime

from strands import tool


BASE_DIR = Path(__file__).resolve().parents[3]

EMPLOYEE_FILE = BASE_DIR / "data" / "employees.json"
INVENTORY_FILE = BASE_DIR / "data" / "inventory.json"
REQUEST_FILE = BASE_DIR / "data" / "equipment_requests.json"


@tool
def create_equipment_request(employee_id: str, item: str) -> dict:
    """
    Create an equipment request only when the employee exists
    and the requested equipment is available.

    Args:
        employee_id: Employee ID such as EMP001.
        item: Equipment item such as laptop or monitor.

    Returns:
        Created request details or an error.
    """

    try:
        # -----------------------------
        # 1. Validate employee
        # -----------------------------
        with open(EMPLOYEE_FILE, "r", encoding="utf-8") as file:
            employees = json.load(file)

        employee = None

        for record in employees:
            if record["employee_id"].upper() == employee_id.upper():
                employee = record
                break

        if employee is None:
            return {
                "error": f"Employee {employee_id} was not found. "
                         "No equipment request was created."
            }

        # -----------------------------
        # 2. Validate inventory
        # -----------------------------
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            inventory = json.load(file)

        equipment = None

        for record in inventory:
            if record["item"].lower() == item.lower():
                equipment = record
                break

        if equipment is None:
            return {
                "error": f"Item '{item}' was not found in inventory. "
                         "No equipment request was created."
            }

        # -----------------------------
        # 3. Check availability
        # -----------------------------
        if equipment["available"] <= 0:
            return {
                "error": f"Item '{item}' is currently unavailable. "
                         "No equipment request was created."
            }

        # -----------------------------
        # 4. Load existing requests
        # -----------------------------
        if REQUEST_FILE.exists():
            with open(REQUEST_FILE, "r", encoding="utf-8") as file:
                requests = json.load(file)
        else:
            requests = []

        # -----------------------------
        # 5. Create request
        # -----------------------------
        request_id = f"REQ-{len(requests) + 1:04d}"

        new_request = {
            "request_id": request_id,
            "employee_id": employee_id.upper(),
            "item": item.lower(),
            "status": "CREATED",
            "created_at": datetime.now().isoformat()
        }

        requests.append(new_request)

        with open(REQUEST_FILE, "w", encoding="utf-8") as file:
            json.dump(requests, file, indent=2)

        return new_request

    except Exception as exc:
        return {
            "error": f"Unable to create equipment request: {exc}"
        }