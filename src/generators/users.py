from faker import Faker
import uuid
from utils.dates import random_date

fake = Faker()

ROLES = ["Engineer", "PM", "Designer", "Marketing", "Ops"]

def generate_users(conn, n, start, end):
    users = []
    for _ in range(n):
        uid = str(uuid.uuid4())
        users.append((
            uid,
            fake.name(),
            fake.email(),
            fake.random_element(ROLES),
            random_date(start, end).isoformat()
        ))

    conn.executemany(
        "INSERT INTO users VALUES (?,?,?,?,?)",
        users
    )
    conn.commit()
    return [u[0] for u in users]
