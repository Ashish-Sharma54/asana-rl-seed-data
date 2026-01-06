# Asana RL Seed Data Generator

## Overview
This project generates a **high-fidelity synthetic dataset** that simulates a realistic **Asana workspace** for a large **B2B SaaS organization (≈5000–10000 employees)**.  
The dataset is designed to serve as **seed data for a Reinforcement Learning (RL) environment**, enabling the evaluation and fine-tuning of computer-use AI agents that interact with enterprise project management tools.

Unlike naive synthetic datasets (e.g., “Task 1”, “Task 2”), this project focuses on:
- Realistic organizational structure
- Temporal and relational consistency
- Enterprise-grade task workflows
- Avoidance of shortcuts exploitable by RL agents

---

## Key Features
- Complete Asana-like relational schema
- Realistic hierarchy: Workspace → Teams → Projects → Sections → Tasks → Subtasks
- Collaboration artifacts: comments, tags, custom fields
- Configurable company size and time range
- Fully runnable, modular Python pipeline
- SQLite output for easy inspection and portability

---

## Schema Coverage
The generated database includes the following entities:

- **Workspaces / Organizations**
- **Users**
- **Teams**
- **Team Memberships**
- **Projects**
- **Sections (workflow states)**
- **Tasks**
- **Subtasks**
- **Comments / Activity**
- **Tags & Task-Tag associations**
- **Custom Field Definitions & Values**

This schema mirrors real Asana usage patterns in enterprise environments.

---

## Project Structure
The repository is organized to clearly separate schema definition, data generation logic, utilities, and final outputs. This modular design improves readability, extensibility, and reproducibility.
```asana-rl-seed-data/
├── README.md # Project overview, setup, and usage
├── requirements.txt # Python dependencies
├── schema.sql # Complete SQLite DDL for Asana-like schema
├── .env.example # Example environment configuration
│
├── src/
│ ├── main.py # Entry point; orchestrates full data generation pipeline
│ │
│ ├── generators/ # Entity-wise data generation logic
│ │ ├── workspace.py # Workspace / organization generation
│ │ ├── users.py # Users and roles generation
│ │ ├── teams.py # Teams and team memberships
│ │ ├── projects.py # Projects under teams
│ │ ├── sections.py # Workflow sections (To Do / In Progress / Done)
│ │ ├── tasks.py # Core task generation logic
│ │ ├── subtasks.py # Hierarchical task breakdown
│ │ ├── comments.py # Task activity and collaboration
│ │ └── tags.py # Tags and task-tag associations
│ │
│ └── utils/ # Shared helper utilities
│ ├── config.py # Environment and configuration loader
│ ├── db.py # SQLite initialization and schema execution
│ └── dates.py # Temporal logic and realistic date generation
│
└── output/
└── asana_simulation.sqlite # Final generated SQLite database```

### Design Rationale
- **Separation of concerns:** Each generator handles exactly one entity.
- **Scalability:** New entities can be added without refactoring existing code.
- **Reproducibility:** Entire database can be regenerated using a single command.
- **RL readiness:** Clear entity boundaries simplify RL environment integration.

