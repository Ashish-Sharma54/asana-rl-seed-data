from datetime import datetime, timedelta
import random

def random_date(start, end):
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))
