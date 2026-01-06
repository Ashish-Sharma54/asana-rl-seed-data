import os
from utils.config import COMPANY_SIZE, START_DATE, END_DATE, DB_PATH
from utils.db import init_db

from generators.workspace import generate_workspace
from generators.users import generate_users
from generators.teams import generate_teams
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.subtasks import generate_subtasks
from generators.comments import generate_comments
from generators.tags import generate_tags

os.makedirs("output", exist_ok=True)

conn = init_db("schema.sql", DB_PATH)

wid = generate_workspace(conn)

print("Generating users...")
users = generate_users(conn, COMPANY_SIZE, START_DATE, END_DATE)

print("Generating teams...")
teams = generate_teams(conn, users, wid)

print("Generating projects...")
projects = generate_projects(conn, teams, START_DATE, END_DATE)

sections = generate_sections(conn, projects)

tasks = generate_tasks(
    conn,
    projects,
    sections,
    users,
    START_DATE,
    END_DATE
)

generate_subtasks(conn, tasks, users)
generate_comments(conn, tasks, users, START_DATE, END_DATE)
generate_tags(conn, tasks)

conn.close()
print("FULL Asana schema database created")
