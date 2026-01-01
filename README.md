# Claude Agent SDK with Vertex AI

## About Claude Code

Claude Code is Anthropic's official CLI tool that has been receiving excellent reviews from developers. It provides an interactive command-line interface for working with Claude, enabling powerful software engineering workflows directly from your terminal.

The **Claude Agent SDK** is the framework that powers Claude Code under the hood. It allows developers to build their own AI agents with the same robust architecture that makes Claude Code so effective.

## What This Project Does

This project demonstrates how to build a Claude agent using the **Claude Agent SDK** with **Google Cloud Vertex AI** as the model provider.

### Why Vertex AI?

For enterprises working with Google Cloud Platform (GCP), using Vertex AI as the model provider offers several advantages:

- **Enterprise Compliance**: Keep all AI interactions within your GCP environment
- **Unified Billing**: Consolidate costs under your existing GCP billing
- **Data Residency**: Control where your data is processed with regional endpoints
- **IAM Integration**: Leverage existing GCP identity and access management
- **Audit Logging**: Full visibility through Cloud Audit Logs

This makes the Claude Agent SDK + Vertex AI combination ideal for organizations that are already invested in the Google Cloud ecosystem.

## What We're Building

This demo builds a **Weather Agent** - a conversational AI assistant that can answer questions about weather in any location.

### The Dummy Weather Tool

The agent uses a `get_weather` tool decorated with `@tool()`. This is a **dummy implementation** that always returns **69°F** regardless of the location. This approach makes it easy to:

- Test the agent flow without needing external API keys
- Demonstrate how tools work in the Claude Agent SDK
- Later swap in a real weather API (like OpenWeatherMap)

### How It Works

```
User asks: "What's the weather in San Francisco?"
    ↓
Agent calls get_weather(location="San Francisco")
    ↓
Tool returns: "The weather in San Francisco is 69F"
    ↓
Agent responds with a natural language answer
```

### Key Components

1. **Tool Definition** (`@tool` decorator) - Defines the tool name, description, and parameters
2. **MCP Server** - Packages the tool into a server the agent can use
3. **ClaudeAgentOptions** - Configures the agent with a system prompt and allowed tools
4. **ClaudeSDKClient** - Runs the agent and streams responses

## Project Structure

```
.
├── agent.py            # Main agent implementation
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
└── README.md           # This file
```

## Prerequisites

1. Python 3.10+
2. A Google Cloud account with Vertex AI enabled
3. `gcloud` CLI installed and configured

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd claude-agent-sdk-weather-demo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Authenticate with GCP**
   ```bash
   gcloud auth application-default login
   ```

5. **Set environment variables**
   ```bash
   export CLAUDE_CODE_USE_VERTEX=1
   export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id
   export CLOUD_ML_REGION=us-east5  # or your preferred region
   ```

## Running the Agent

```bash
python agent.py
```

The agent will run two sample queries asking about weather in San Francisco and Tokyo, demonstrating how the tool is invoked and responses are streamed back.

## Extending the Agent

Replace the dummy `get_weather` tool with a real weather API (like OpenWeatherMap) or add additional tools to create more sophisticated agents for your use case.

## Contact

**Vamsee Krishna Kotha**
- Email: vamseekrishna9201@gmail.com
- LinkedIn: [linkedin.com/in/vamseekrishnakotha](https://www.linkedin.com/in/vamseekrishnakotha/)
