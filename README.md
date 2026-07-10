# Google ADK Multi-Agent Systems

This repository contains multi-agent orchestration projects built using the **Google Agent Development Kit (ADK)** and the Gemini generative models API. It showcases parent-subagent architectures, workflow agents (sequential, parallel, loop), and custom tool integrations.

## Repository Structure

- [parent_and_subagents/](file:///c:/Users/gamez/Documents/GoogleADK/adk-workspace/adk_multiagent_systems/parent_and_subagents): A travel assistant implementation demonstrating subagent routing.
  - **Steering Agent (Root)**: Assesses user intent and routes them dynamically.
  - **Travel Brainstormer (Subagent)**: Recommends target countries based on preferences.
  - **Attractions Planner (Subagent)**: Builds customized sightseeing itineraries and persists selections via state-saving tools.
- [workflow_agents/](file:///c:/Users/gamez/Documents/GoogleADK/adk-workspace/adk_multiagent_systems/workflow_agents): A movie-pitch generator utilizing structured execution patterns (`SequentialAgent`, `ParallelAgent`, `LoopAgent`).
- [adk_utils/](file:///c:/Users/gamez/Documents/GoogleADK/adk-workspace/adk_multiagent_systems/adk_utils): Core helper modules and agent plugins (e.g., fallback rate-limiting adapters).
- [movie_pitches/](file:///c:/Users/gamez/Documents/GoogleADK/adk-workspace/adk_multiagent_systems/movie_pitches): Target output folder containing persisted results from the movie pitch generator.

## Getting Started

### 1. Prerequisites
Ensure you are inside your virtual environment (`.venv`) and install the required Langchain and helper libraries:
```bash
pip install langchain-core langchain-community wikipedia
```

### 2. Configure Environment Variables
Place a `.env` file in your workspace or target agent subdirectory:
```env
GOOGLE_API_KEY=your_gemini_api_key
MODEL=gemini-2.5-flash
```
*Note: Do NOT set `GOOGLE_GENAI_USE_VERTEXAI` if you intend to use standard API keys instead of Google Cloud Service Account/OAuth credentials.*

### 3. API Quotas & Billing
For workflow-based executions utilizing simultaneous `ParallelAgent` processes or iterative `LoopAgent` operations, we recommend upgrading to a **Gemini Tier 1 Billing Account (Pay-As-You-Go)** to avoid standard Free Tier rate limits (`429 RESOURCE_EXHAUSTED`).

## Telemetry & Logging
Execution is integrated with [callback_logging.py](file:///c:/Users/gamez/Documents/GoogleADK/adk-workspace/adk_multiagent_systems/callback_logging.py) to inspect queries and responses before and after API interactions without side effects.
