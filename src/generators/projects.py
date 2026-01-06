import uuid
import random
from utils.dates import random_date

PROJECT_TYPES = ["Sprint", "Campaign", "Operations"]

def generate_projects(conn, team_ids, start, end):
    projects = []

    for tid in team_ids:
        for _ in range(random.randint(5, 8)):
            projects.append((
                str(uuid.uuid4()),
                tid,
                f"{random.choice(PROJECT_TYPES)} Project",
                random.choice(PROJECT_TYPES),
                random_date(start, end).isoformat()
            ))

    conn.executemany(
        "INSERT INTO projects VALUES (?,?,?,?,?)",
        projects
    )
    conn.commit()

    return [p[0] for p in projects]
