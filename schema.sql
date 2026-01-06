PRAGMA foreign_keys = ON;


-- WORKSPACE

CREATE TABLE workspaces (
    workspace_id TEXT PRIMARY KEY,
    name TEXT
);


-- USERS & TEAMS

CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    role TEXT,
    created_at TEXT
);

CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    workspace_id TEXT,
    name TEXT
);

CREATE TABLE team_memberships (
    team_id TEXT,
    user_id TEXT,
    PRIMARY KEY (team_id, user_id)
);


-- PROJECTS & SECTIONS

CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    team_id TEXT,
    name TEXT,
    type TEXT,
    created_at TEXT
);

CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT,
    name TEXT
);


-- TASKS & SUBTASKS

CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT,
    section_id TEXT,
    assignee_id TEXT,
    name TEXT,
    due_date TEXT,
    completed INTEGER,
    created_at TEXT,
    completed_at TEXT
);

CREATE TABLE subtasks (
    subtask_id TEXT PRIMARY KEY,
    parent_task_id TEXT,
    assignee_id TEXT,
    name TEXT,
    completed INTEGER
);


-- COMMENTS

CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT,
    user_id TEXT,
    body TEXT,
    created_at TEXT
);


-- CUSTOM FIELDS

CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    name TEXT,
    field_type TEXT
);

CREATE TABLE custom_field_values (
    field_id TEXT,
    task_id TEXT,
    value TEXT,
    PRIMARY KEY (field_id, task_id)
);


-- TAGS

CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    name TEXT
);

CREATE TABLE task_tags (
    task_id TEXT,
    tag_id TEXT,
    PRIMARY KEY (task_id, tag_id)
);
