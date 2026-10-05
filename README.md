# 🤖 AI Business Process Automation Agent

An AI-powered business automation system that processes employee equipment requests using **Strands Agents, MCP, Ollama, FastAPI, and Streamlit**.

## 🚀 Features

* AI agent powered by **Llama 3.2 3B**
* Local LLM inference with **Ollama**
* **MCP Server & Client** for tool integration
* Employee verification
* Equipment inventory checking
* Automatic equipment request creation
* IT team notification
* FastAPI backend
* Streamlit frontend

## 🏗️ Architecture

```text
Streamlit
    ↓
FastAPI
    ↓
Strands Agent
    ↓
Ollama (Llama 3.2:3b)
    ↓
MCP Client
    ↓
MCP Server
    ↓
Business Tools
 ├── employee_lookup
 ├── inventory_check
 ├── equipment_request
 └── it_notification
```

## 📁 Project Structure

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

## ⚙️ Requirements

* Python 3.13
* Ollama
* Llama 3.2 3B
* uv

## ▶️ Setup

Install dependencies:

```powershell
uv sync --project .\app\BST
```

Install the Ollama model:

```powershell
ollama pull llama3.2:3b
```

## ▶️ Run

### FastAPI

```powershell
uv run --project .\app\BST --active uvicorn api.main:app --reload --port 8080
```

### Streamlit

```powershell
uv run --project .\app\BST --active streamlit run app\BST\app.py
```

Open:

```text
http://localhost:8501
```

## 🔄 Workflow

```text
Employee Request
      ↓
Verify Employee
      ↓
Check Inventory
      ↓
Create Request
      ↓
Notify IT
      ↓
Completed
```

## 🧪 MCP Tools

| Tool                | Purpose                      |
| ------------------- | ---------------------------- |
| `employee_lookup`   | Verify employee              |
| `inventory_check`   | Check equipment availability |
| `equipment_request` | Create request               |
| `it_notification`   | Notify IT                    |

## 🎯 Example

Input:

```text
Employee: EMP001
Equipment: laptop
```

Result:

```text
Employee verified
Laptop available
Request created
IT notified
```

## 🛠️ Tech Stack

**Python · Strands Agents · MCP · Ollama · Llama 3.2 · FastAPI · Streamlit · uv**

## 📌 Project Status

✅ AI Agent
✅ MCP Server
✅ MCP Client
✅ Business Tools
✅ FastAPI API
✅ Streamlit UI
✅ End-to-End Workflow
