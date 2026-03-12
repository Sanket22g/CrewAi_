# demo_1 — CrewAI Blog & Report Generator

## What This Project Does

This is a **CrewAI** project that uses two AI agents working sequentially to:
1. **Generate a research report** on a given topic
2. **Write a blog post** based on that topic

The final blog post is saved automatically to `blog_output.txt`.

---

## Four Pillars of CrewAI

CrewAI is built on four core concepts. Every project you build will revolve around these four pillars:

### 1. Agent
An **Agent** is an autonomous AI unit with a specific **role**, **goal**, and **backstory**.
It knows what it is supposed to do and acts accordingly.

```python
@agent
def blog_writer_agent(self) -> Agent:
    return Agent(config=self.agents_config["blog_writer_agent"])
```

- **Role** — what the agent is (e.g., "Expert Blog Writer")
- **Goal** — what the agent wants to achieve
- **Backstory** — gives the agent personality and context so it behaves more accurately

In this project: `report_generator_agent` and `blog_writer_agent` are the two agents.

---

### 2. Task
A **Task** is a specific piece of work assigned to an agent.
It defines **what needs to be done**, the **expected output**, and **which agent** should do it.

```python
@task
def blog_task(self) -> Task:
    return Task(
        config=self.tasks_config["blog_task"],
        output_file="blog_output.txt"
    )
```

- **Description** — the instructions for the task
- **Expected Output** — what a completed task looks like
- **Agent** — which agent is responsible
- **output_file** *(optional)* — saves the result directly to a file

In this project: `report_task` and `blog_task` are the two tasks.

---

### 3. Crew
A **Crew** is the **team** — it groups agents and tasks together and manages how they work.
It is the central coordinator of the whole pipeline.

```python
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True
    )
```

- Holds the list of all **agents** and **tasks**
- Decides the **process** (sequential or hierarchical)
- `verbose=True` prints step-by-step execution logs

---

### 4. Process
A **Process** defines the **order and strategy** in which tasks are executed by the crew.

| Process | How it works |
|---|---|
| `Process.sequential` | Tasks run one after another in order |
| `Process.hierarchical` | A manager agent delegates tasks to other agents |

In this project, `Process.sequential` is used — the **report is generated first**, then the **blog post is written**.

```python
process=Process.sequential
```

---

## Project Structure

```
demo_1/
├── knowledge/
│   └── user_preference.txt       # User context (name, role, interests)
├── src/demo_1/
│   ├── crew.py                   # Defines agents, tasks, and the crew
│   ├── main.py                   # Entry point — runs the crew via kickoff()
│   └── config/
│       ├── agents.yaml           # Agent roles, goals, and backstories
│       └── tasks.yaml            # Task descriptions and expected outputs
├── blog_output.txt               # Auto-generated output file
└── pyproject.toml                # Project dependencies
```

---

## Agents Defined (`agents.yaml`)

| Agent | Role | Goal |
|---|---|---|
| `report_generator_agent` | Expert report generator | Creates a 1000–1500 word structured report on the topic |
| `blog_writer_agent` | Expert blog writer | Writes an 800–1200 word SEO-optimized blog post on the topic |

---

## Tasks Defined (`tasks.yaml`)

| Task | Agent | Output |
|---|---|---|
| `report_task` | `report_generator_agent` | A well-structured report with intro, body, and conclusion |
| `blog_task` | `blog_writer_agent` | An engaging blog post saved to `blog_output.txt` |

---

## What is `kickoff()`?

`kickoff()` is the **CrewAI method that starts the entire crew execution**.

```python
Demo1().crew().kickoff(inputs=inputs)
```

- It takes an `inputs` dictionary (e.g. `{'topic': 'AI agents for brain computer interfaces'}`)
- It passes those inputs to all agents and tasks that use `{topic}` as a placeholder
- It runs all tasks **sequentially** (one after another) as defined by `Process.sequential`
- Once done, it returns the final output and saves `blog_output.txt` to disk

Think of `kickoff()` as pressing the **"Start"** button for your multi-agent pipeline.

---

## Changes Made in This Project

### 1. Added Two Custom Agents (`crew.py`)
- `report_generator_agent` — generates a detailed research report
- `blog_writer_agent` — writes a blog post based on the same topic

### 2. Added Two Custom Tasks (`crew.py`)
- `report_task` — assigned to the report agent
- `blog_task` — assigned to the blog agent, with `output_file="blog_output.txt"` so the result is saved to disk automatically

### 3. Sequential Process
- Set `process=Process.sequential` so the report is generated **first**, then the blog post is written in order

### 4. Dynamic Topic via `inputs`
- In `main.py`, the topic is passed dynamically:
  ```python
  inputs = {'topic': 'AI agents for brain computer interfaces with writing code'}
  ```
- The `{topic}` placeholder in `agents.yaml` and `tasks.yaml` is replaced at runtime
- You can change the topic without editing any config files

### 5. Knowledge File (`knowledge/user_preference.txt`)
- Added user context so agents are aware of who they are working for:
  ```
  User name is John Doe.
  User is an AI Engineer.
  User is interested in AI Agents.
  User is based in San Francisco, California.
  ```

---

## How to Run

```bash
# Step 1 — Activate the virtual environment
.venv\Scripts\Activate.ps1

# Step 2 — Add your OpenAI API key to .env
# OPENAI_API_KEY=your_key_here

# Step 3 — Run the crew
crewai run
```

The blog post output will be saved to `blog_output.txt`.

---

## How to Change the Topic

Edit the `inputs` dictionary in `src/demo_1/main.py`:

```python
inputs = {
    'topic': 'Your new topic here',
}
```

---

## Requirements

- Python >= 3.10
- [crewai](https://github.com/joaomdmoura/crewai)
- OpenAI API key (set in `.env` as `OPENAI_API_KEY`)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
