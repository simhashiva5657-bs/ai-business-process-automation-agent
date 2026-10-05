from agent.agent import create_agent


def process_equipment_request(employee_id: str, item: str) -> dict:
    """Process an equipment request using the AI agent."""

    agent = create_agent()

    prompt = f"""
Process an equipment request for employee {employee_id} for a {item}.

Follow the required workflow:
1. Verify the employee using employee_lookup.
2. Check equipment availability using inventory_check.
3. If the employee exists and the equipment is available,
   create the request using equipment_request.
4. Notify IT using it_notification.
5. Return a clear summary.

Do not invent any information.
"""

    response = agent(prompt)

    return {
        "status": "SUCCESS",
        "employee_id": employee_id,
        "item": item,
        "result": str(response),
    }