"""
Weather Agent using Claude Agent SDK with VertexAI

This agent uses a dummy weather tool that returns 69F for any location.
Later, we can replace it with a real weather API.

To use VertexAI, set these environment variables before running:
    export CLAUDE_CODE_USE_VERTEX=1
    export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id
    export CLOUD_ML_REGION=us-east5  # or your preferred region

Make sure you're authenticated with GCP:
    gcloud auth application-default login
"""

import os
import anyio
from claude_agent_sdk import (
    tool,
    create_sdk_mcp_server,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    AssistantMessage,
    TextBlock,
)


# Define the dummy weather tool
@tool("get_weather", "Get the current weather for a given location", {"location": str})
async def get_weather(args: dict) -> dict:
    """
    Dummy weather tool that always returns 69F.
    Replace this with a real weather API call later.
    """
    location = args.get("location", "unknown")
    return {
        "content": [
            {
                "type": "text",
                "text": f"The weather in {location} is 69F (nice and comfortable!)"
            }
        ]
    }


# Create the MCP server with our weather tool
weather_server = create_sdk_mcp_server(
    name="weather-tools",
    version="1.0.0",
    tools=[get_weather]
)


async def run_weather_agent(query: str) -> None:
    """Run the weather agent with the given query."""

    # Configure the agent options
    options = ClaudeAgentOptions(
        system_prompt="You are a helpful weather assistant. Use the get_weather tool to check weather for any location the user asks about.",
        mcp_servers={"weather": weather_server},
        allowed_tools=["mcp__weather__get_weather"],
        max_turns=5,
    )

    print(f"\n{'='*50}")
    print(f"Query: {query}")
    print('='*50)

    async with ClaudeSDKClient(options=options) as client:
        await client.query(query)

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"\nAssistant: {block.text}")


async def main():
    # Check if VertexAI is configured
    if os.environ.get("CLAUDE_CODE_USE_VERTEX") == "1":
        print("Using VertexAI backend")
        project_id = os.environ.get("ANTHROPIC_VERTEX_PROJECT_ID", "not set")
        region = os.environ.get("CLOUD_ML_REGION", "not set")
        print(f"  Project ID: {project_id}")
        print(f"  Region: {region}")
    else:
        print("Using default Anthropic API backend")
        print("To use VertexAI, set CLAUDE_CODE_USE_VERTEX=1")

    # Run some weather queries
    await run_weather_agent("What's the weather like in San Francisco?")
    await run_weather_agent("How's the weather in Tokyo?")


if __name__ == "__main__":
    anyio.run(main)
