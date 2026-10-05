import json
from pathlib import Path

from strands import tool


DATA_FILE = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "inventory.json"
)


@tool
def check_inventory(item: str) -> dict:
    """
    Check whether an equipment item is available.

    Args:
        item: Equipment item such as laptop, monitor, keyboard, or mouse.

    Returns:
        Inventory details for the requested item.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            inventory = json.load(file)

        for record in inventory:
            if record["item"].lower() == item.lower():
                return record

        return {
            "error": f"Item '{item}' was not found in inventory."
        }

    except Exception as exc:
        return {
            "error": f"Unable to read inventory data: {exc}"
        }