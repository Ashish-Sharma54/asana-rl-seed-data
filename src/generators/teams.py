import uuid
import random

TEAM_NAMES = ["Backend", "Frontend", "AI", "Marketing", "Operations"]

def generate_teams(conn, user_ids, workspace_id):
    teams = []
    memberships = []

    per_team = len(user_ids) // len(TEAM_NAMES)

    for name in TEAM_NAMES:
        tid = str(uuid.uuid4())
        teams.append((tid, workspace_id, name))

        members = random.sample(user_ids, per_team)
        for uid in members:
            memberships.append((tid, uid))

    conn.executemany(
        "INSERT INTO teams VALUES (?,?,?)",
        teams
    )
    conn.executemany(
        "INSERT INTO team_memberships VALUES (?,?)",
        memberships
    )
    conn.commit()

    return [t[0] for t in teams]
