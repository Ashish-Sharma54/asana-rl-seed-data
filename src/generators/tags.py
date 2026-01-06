import uuid
import random

TAG_NAMES = ["urgent", "backend", "frontend", "qa", "blocked"]

def generate_tags(conn, task_ids):
    # Create tags
    tags = [(str(uuid.uuid4()), name) for name in TAG_NAMES]
    conn.executemany(
        "INSERT INTO tags VALUES (?, ?)",
        tags
    )

    # Assign tags to a subset of tasks
    for tid in task_ids[:1000]:
        conn.execute(
            "INSERT INTO task_tags VALUES (?, ?)",
            (tid, random.choice(tags)[0])
        )

    conn.commit()
