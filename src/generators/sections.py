import uuid

SECTION_NAMES = ["To Do", "In Progress", "Done"]

def generate_sections(conn, project_ids):
    section_ids = []

    for pid in project_ids:
        for name in SECTION_NAMES:
            sid = str(uuid.uuid4())
            section_ids.append(sid)

            conn.execute(
                "INSERT INTO sections VALUES (?, ?, ?)",
                (sid, pid, name)
            )

    conn.commit()
    return section_ids
