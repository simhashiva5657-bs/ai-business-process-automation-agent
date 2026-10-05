from fastapi import FastAPI
from bedrock_agentcore.runtime import BedrockAgentCoreApp

from api.routes import router
from agent.agent import create_agent


api = FastAPI(
    title="AI Business Process Automation Agent",
    version="1.0.0",
)

api.include_router(router)


agentcore_app = BedrockAgentCoreApp()
agent = create_agent()


@agentcore_app.entrypoint
def invoke(payload):
    user_message = payload.get("prompt", "")

    if not user_message:
        return {
            "status": "ERROR",
            "message": "Missing 'prompt' in request."
        }

    response = agent(user_message)

    return {
        "status": "SUCCESS",
        "response": str(response)
    }


if __name__ == "__main__":
    agentcore_app.run()
