import json
from pathlib import Path
from datetime import datetime

from strands import tool


DATA_FILE = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "it_notifications.json"
)


@tool
def notify_it_team(request_id: str) -> dict:
    """
    Notify the IT team about an equipment request.

    Prevents duplicate notifications for the same request.

    Args:
        request_id: Equipment request ID such as REQ-0001.

    Returns:
        Notification details.
    """
    try:
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                notifications = json.load(file)
        else:
            notifications = []

        # Prevent duplicate notifications
        for notification in notifications:
            if notification["request_id"] == request_id:
                return {
                    "request_id": request_id,
                    "status": "ALREADY_NOTIFIED",
                    "message": (
                        f"IT has already been notified "
                        f"about request {request_id}."
                    )
                }

        notification = {
            "notification_id": f"NOT-{len(notifications) + 1:04d}",
            "request_id": request_id,
            "team": "IT",
            "message": (
                f"New equipment request {request_id} "
                f"requires processing."
            ),
            "status": "SENT",
            "sent_at": datetime.now().isoformat()
        }

        notifications.append(notification)

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(notifications, file, indent=2)

        return notification

    except Exception as exc:
        return {
            "error": f"Unable to notify IT team: {exc}"
        }