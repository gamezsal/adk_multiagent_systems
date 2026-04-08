# Parent and Subagents - Google ADK Travel Assistant

This project demonstrates a multi-agent system built using the Google Agent Development Kit (ADK). It orchestrates a cohesive user experience for travel planning by routing users through specialized generative AI subagents.

*This project was developed as part of the Skills lab by Google Cloud.*

## Agent Architecture

This orchestration utilizes a **Parent Agent** handling the foundational routing, and two specialized **Subagents** executing distinct creative and utility goals.

### 1. Steering Agent (Root)
- **Description:** Start a user on a travel adventure.
- **Instruction:** Functions as the primary hub. It assesses whether the user already knows their destination or if they need inspiration.
- **Subagent Routing:** Automatically directs undecided users to the `travel_brainstormer` and routes users with a chosen destination to the `attractions_planner`. 

### 2. Travel Brainstormer (Subagent)
- **Description:** Help a user decide what country to visit.
- **Instruction:** Solicits the user's primary travel goals (such as adventure, leisure, learning, shopping, or art) and suggests popular countries tailored to those core priorities.

### 3. Attractions Planner (Subagent)
- **Description:** Build a list of attractions to visit in a country.
- **Instruction:** Provides specific recommendations for attractions within a selected country. It asks the user what stands out to them and utilizes tools to persist their final selections.
- **Tools Included:** 
  - `save_attractions_to_state`: Intercepts user choices and commits the selected attractions directly into the application's persistent state dictionary.
  
## Execution Hooks & Callbacks
The agents natively weave into `callback_logging.py` infrastructure, safely triggering `before_model_callback` and `after_model_callback` telemetry without impeding primary ADK operations. Additionally, the system employs an overarching `Graceful429Plugin` to elegantly catch and handle Vertex/Gemini rate-limit exceptions without dropping the conversation.
