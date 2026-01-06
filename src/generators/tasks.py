import uuid
import random
from utils.dates import random_date

ACTIONS = ["Implement", "Fix", "Design", "Review"]

def generate_tasks(conn, project_ids, section_ids, user_ids, start, end):
    task_ids = []

    for pid in project_ids:
        # each project has exactly 3 sections
        project_sections = section_ids[:3]

        for _ in range(random.randint(20, 40)):
            created = random_date(start, end)
            completed = random.random() < 0.7

            tid = str(uuid.uuid4())
            task_ids.append(tid)

            conn.execute(
                "INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    tid,
                    pid,
                    random.choice(project_sections),
                    random.choice(user_ids),
                    f"{random.choice(ACTIONS)} feature",
                    random_date(start, end).date().isoformat(),
                    int(completed),
                    created.isoformat(),
                    created.isoformat() if completed else None
                )
            )

    conn.commit()
    return task_ids
