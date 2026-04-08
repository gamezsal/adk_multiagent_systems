# Google ADK Multi-Agent Systems

This repository contains multi-agent orchestration projects designed to run natively on the Google Agent Development Kit (ADK).

_This project was originally developed as part of a Google Cloud Skills Lab._

## Project Structure

- `workflow_agents/`: A complex movie-pitch simulation utilizing Langchain tools and advanced execution handlers (`SequentialAgent`, `ParallelAgent`, `LoopAgent`).
- `movie_pitches/`: Artifact directory that persistently stores outputs from the movie workflow agents.

## Environment Setup

To ensure these agents run robustly in your local `adk-workspace` environment, there are a few critical steps to follow since the orchestration depends heavily on dynamically injected variables and external Python tools.

### 1. Install Required Dependencies

ADK requires specific native Python bindings to orchestrate external tasks (like accessing Wikipedia via Langchain or intercepting 429 API errors securely).

Ensure you operate inside your active virtual environment (`.venv`) and install these specific modules:

```bash
# Core Langchain bindings used by the movie-pitch Workflow Agents
pip install langchain-core langchain-community

# Dedicated external application hooks
pip install wikipedia
```

### 2. Configure Authentication (.env)

It interacts directly with the Google GenAI SDK. You must structure your `.env` correctly to prevent Vertex AI intercepts.

Inside each agent directory, place your `.env` file formatted strictly as follows:

```env
# CRITICAL: Do NOT define 'GOOGLE_GENAI_USE_VERTEXAI'. Including it forces standard application credentials (OAuth) instead of your raw API keys.

GOOGLE_API_KEY=your_gemini_developer_key
MODEL=gemini-2.5-flash
```

_(Note: The codebase now intelligently falls back to `gemini-2.5-flash` natively to prevent Pydantic validation crashes during runtime, but explicitly defining your API key is mandatory)._

### 3. Launching

You can run any of these orchestrated agents natively via the ADK web interface. Navigate to the agent's folder structure through your ADK dashboard or execute standard Python triggers natively.
