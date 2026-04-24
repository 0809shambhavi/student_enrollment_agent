# Student Enrollment Assistant Agent

## Overview

This project implements a **tool-augmented conversational AI agent** for a university admissions system.

The agent follows an **agentic loop**:
**Thought → Action → Observation → Response**, enabling structured reasoning, tool usage, and multi-turn context handling.

---

## Problem Statement

Build a conversational AI agent that helps prospective students with:

* Program information
* Application deadlines
* Application status tracking
* Document requirements

The agent must:

* Use **tools (not hardcoded answers)**
* Maintain **context across multiple turns**
* Gracefully **handle unsupported queries**

---

## Architecture

```
User Input
   ↓
Agent (Reasoning + Intent Detection)
   ↓
Memory (Context Storage)
   ↓
Tool Layer (Mock APIs)
   ↓
Response Generation
   ↓
User Output
```

### Components:

* **Agent (`agent.py`)** → reasoning + decision making
* **Memory (`memory.py`)** → stores conversation context
* **Tools (`tools.py`)** → mock backend APIs
* **Runner (`main.py`)** → simulates conversation

---

## Tools Definition

### 1. `get_program_info(program_name: str)`

Returns:

* Program name
* Duration
* Tuition
* Prerequisites

---

### 2. `get_deadlines(program_name: str)`

Returns:

* Application deadline
* Document submission deadline
* Decision date

---

### 3. `check_application_status(applicant_id: str)`

Returns:

* Applicant name
* Program applied
* Status
* Next steps

---

## Memory Handling

The agent maintains session-level memory:

| Key            | Purpose                         |
| -------------- | ------------------------------- |
| `program`      | Last discussed program          |
| `applicant_id` | User’s application ID           |
| `last_status`  | Last fetched application status |

### Why it matters:

* Enables **multi-turn conversations**
* Resolves references like *“that”*
* Avoids asking repeated questions

---

## Agent Flow

1. Receive user input
2. Extract entities (program, applicant ID)
3. Store in memory
4. Detect user intent
5. Select appropriate tool
6. Execute tool
7. Generate response
8. Handle unsupported queries gracefully

---

## Key Features

* Tool-based reasoning (no hardcoded answers)
* Multi-turn conversation with memory
* Context-aware responses
* ReAct-style reasoning logs (Thought → Action → Observation)
* Graceful fallback for unsupported queries

---

## Sample Run

```
Turn 1 USER: Hi, what programs do you offer in computer science?

[THOUGHT] Processing user input...
[OBSERVATION] Detected program: computer science
[THOUGHT] Detected intent: program_info
[ACTION] Calling get_program_info
[OBSERVATION] Program info retrieved

AGENT:
We offer BSc Computer Science which is 4 years long. Tuition is $40,000/year. Prerequisites include: High School Math, Basic Programming.


Turn 2 USER: What's the application deadline for that?

[THOUGHT] Detected intent: deadlines
[ACTION] Calling get_deadlines
[OBSERVATION] Deadline info retrieved

AGENT:
For Computer Science, the application deadline is June 30, documents must be submitted by July 15, and decisions are announced on August 10.


Turn 3 USER: I already applied. My ID is APP-1042. What's my status?

[OBSERVATION] Detected applicant ID: APP-1042
[THOUGHT] Detected intent: application_status
[ACTION] Calling check_application_status
[OBSERVATION] Application status retrieved

AGENT:
Hi John Doe, your application for Computer Science is currently 'Documents Pending'. Next step: Submit transcripts and recommendation letter.


Turn 4 USER: Can I get a fee waiver?

[THOUGHT] Unsupported query → escalate

AGENT:
I can't help with fee waivers directly, but I can connect you to an enrollment counselor. Would you like that?


Turn 5 USER: What documents do I still need to submit?

[OBSERVATION] Using previous application status

AGENT:
You still need to: Submit transcripts and recommendation letter.
```

---

## Setup

```bash
conda create -n enrollment-agent python=3.11 -y
conda activate enrollment-agent
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## requirements.txt

```
python-dotenv
```

---

## Design Note

This implementation uses a **rule-based planner** to simulate an agentic workflow.

It can be extended to:

* LLM-based reasoning (ReAct)
* OpenAI function calling
* LangChain agents

---

## Future Improvements

* Integrate LLM-based tool calling
* Replace mock data with database
* Build REST API (FastAPI)
* Add UI (Streamlit / React)

---

## Project Structure

```
student_enrollment_agent/
│── agent.py
│── tools.py
│── memory.py
│── main.py
│── requirements.txt
│── README.md
```

---

## Author

Built as part of an **Agentic AI case study** demonstrating tool-based reasoning, memory handling, and modular design.
