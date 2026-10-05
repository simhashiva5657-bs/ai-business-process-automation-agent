from fastapi import APIRouter

from agent.workflow import process_equipment_request


router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Business Agent"
    }


@router.post("/equipment-request")
def equipment_request(employee_id: str, item: str):
    return process_equipment_request(
    employee_id.strip(),
    item.strip().lower(),
)