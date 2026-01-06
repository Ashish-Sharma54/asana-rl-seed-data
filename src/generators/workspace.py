import uuid

def generate_workspace(conn):
    wid = str(uuid.uuid4())
    conn.execute(
        "INSERT INTO workspaces VALUES (?, ?)",
        (wid, "Acme SaaS Corp")
    )
    conn.commit()
    return wid
