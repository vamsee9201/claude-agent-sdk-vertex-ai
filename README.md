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

## Project Structure

```
.
├── weather_agent.py    # Main agent implementation
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
python weather_agent.py
```

The demo agent includes a simple weather tool that responds to weather queries. This serves as a starting point for building more complex agents with real API integrations.

## Extending the Agent

Replace the dummy `get_weather` tool with a real weather API (like OpenWeatherMap) or add additional tools to create more sophisticated agents for your use case.

## Contact

**Vamsee Krishna Kotha**
- Email: vamseekrishna9201@gmail.com
- LinkedIn: [linkedin.com/in/vamseekrishnakotha](https://www.linkedin.com/in/vamseekrishnakotha/)
