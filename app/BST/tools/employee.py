import json
from pathlib import Path

from strands import tool


DATA_FILE = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "employees.json"
)


@tool
def get_employee(employee_id: str) -> dict:
    """
    Look up an employee by employee ID.

    Args:
        employee_id: Employee ID such as EMP001.

    Returns:
        Employee details if found, otherwise an error message.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            employees = json.load(file)

        for employee in employees:
            if employee["employee_id"].upper() == employee_id.upper():
                return employee

        return {
            "error": f"Employee {employee_id} was not found."
        }

    except Exception as exc:
        return {
            "error": f"Unable to read employee data: {exc}"
        }
