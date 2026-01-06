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
