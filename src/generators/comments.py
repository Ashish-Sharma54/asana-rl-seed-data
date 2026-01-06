import uuid
from utils.dates import random_date

def generate_comments(conn, task_ids, user_ids, start, end):
    # Add comments to a subset of tasks
    for tid in task_ids[:1000]:
        conn.execute(
            "INSERT INTO comments VALUES (?, ?, ?, ?, ?)",
            (
                str(uuid.uuid4()),
                tid,
                user_ids[0],
                "Please review this task.",
                random_date(start, end).isoformat()
            )
        )
    conn.commit()
