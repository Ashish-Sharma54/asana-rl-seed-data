import uuid
import random

def generate_subtasks(conn, task_ids, user_ids):
    # About ~30% tasks get subtasks
    selected_tasks = random.sample(
        task_ids,
        k=max(1, len(task_ids) // 3)
    )

    for tid in selected_tasks:
        for _ in range(random.randint(1, 3)):
            conn.execute(
                "INSERT INTO subtasks VALUES (?, ?, ?, ?, ?)",
                (
                    str(uuid.uuid4()),
                    tid,
                    random.choice(user_ids),
                    "Follow-up work",
                    random.choice([0, 1])
                )
            )

    conn.commit()
