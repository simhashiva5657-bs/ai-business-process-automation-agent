from mcp.server.fastmcp import FastMCP

from tools.employee import get_employee
from tools.inventory import check_inventory
from tools.equipment import create_equipment_request
from tools.notification import notify_it_team


mcp = FastMCP("business-agent")


@mcp.tool()
def employee_lookup(employee_id: str) -> dict:
    """Look up an employee by employee ID."""
    return get_employee(employee_id)


@mcp.tool()
def inventory_check(item: str) -> dict:
    """Check equipment inventory."""
    return check_inventory(item)


@mcp.tool()
def equipment_request(employee_id: str, item: str) -> dict:
    """Create an equipment request."""
    return create_equipment_request(employee_id, item)


@mcp.tool()
def it_notification(request_id: str) -> dict:
    """Notify the IT team about an equipment request."""
    return notify_it_team(request_id)


if __name__ == "__main__":
    mcp.run()