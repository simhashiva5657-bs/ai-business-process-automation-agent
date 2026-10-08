# AI Business Process Automation Agent

An AI-powered business automation application that processes employee equipment requests using an AI agent, MCP-based tool integration, a local LLM, and a web interface.

The application takes an employee's equipment request, verifies the employee, checks equipment availability, creates the request, and notifies the IT team.

## What This Project Does

The goal of this project is to demonstrate how an AI agent can be connected to business tools and used to automate a complete workflow.

For example, an employee can request a laptop. The agent can:

1. Verify the employee
2. Check the inventory
3. Create the equipment request
4. Notify the IT team
5. Return the result to the user

The workflow is handled through tools exposed by an MCP server.

## Architecture

```text
                    User
                     |
                     v
               Streamlit UI
                     |
                     v
                FastAPI
                     |
                     v
              Strands Agent
                     |
                     v
              Ollama LLM
            (Llama 3.2 3B)
                     |
                     v
                MCP Client
                     |
                     v
                MCP Server
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Employee   Inventory   Equipment
       Lookup      Check       Request
                                |
                                v
                         IT Notification
```

## Workflow

```text
Employee Equipment Request
            |
            v
     Verify Employee
            |
            v
     Check Inventory
            |
            v
     Create Request
            |
            v
       Notify IT
            |
            v
        Completed
```

## Key Features

* AI agent powered by Llama 3.2 3B
* Local LLM inference using Ollama
* MCP server and client for tool integration
* Employee verification
* Equipment inventory checking
* Automated equipment request creation
* IT team notification
* FastAPI backend
* Streamlit frontend
* End-to-end business workflow

## MCP Tools

| Tool                | Purpose                       |
| ------------------- | ----------------------------- |
| `employee_lookup`   | Verifies employee information |
| `inventory_check`   | Checks equipment availability |
| `equipment_request` | Creates an equipment request  |
| `it_notification`   | Notifies the IT team          |

## Project Structure

```text
app/BST/
├── agent/
├── api/
├── mcp_client/
├── mcp_server/
├── model/
├── tools/
├── app.py
├── pyproject.toml
└── README.md
```

## Technologies

* Python 3.13
* Strands Agents
* Model Context Protocol (MCP)
* Ollama
* Llama 3.2 3B
* FastAPI
* Streamlit
* uv

## Requirements

Before running the project, install:

* Python 3.13
* Ollama
* uv

The project uses the Llama 3.2 3B model through Ollama.

## Setup

Clone the repository and navigate to the project.

Install the project dependencies:

```powershell
uv sync --project .\app\BST
```

Pull the required Ollama model:

```powershell
ollama pull llama3.2:3b
```

## Running the Application

### Start FastAPI

```powershell
uv run --project .\app\BST --active uvicorn api.main:app --reload --port 8080
```

### Start Streamlit

```powershell
uv run --project .\app\BST --active streamlit run app\BST\app.py
```

The Streamlit application will be available at:

```text
http://localhost:8501
```

## Example

### Input

```text
Employee: EMP001
Equipment: laptop
```

### Workflow

```text
Employee verified
        ↓
Laptop availability checked
        ↓
Equipment request created
        ↓
IT team notified
```

### Result

```text
Equipment request processed successfully.
```

## Project Status

The current implementation includes:

* AI Agent
* MCP Server
* MCP Client
* Business Tools
* FastAPI Backend
* Streamlit Interface
* End-to-End Equipment Request Workflow

## Future Improvements

Possible future improvements include:

* Persistent database integration
* Authentication and authorization
* More business workflows
* Better error handling and validation
* Cloud-based LLM deployment
* Production deployment on AWS
* Monitoring and observability
