import os
from dotenv import load_dotenv

load_dotenv()

COMPANY_SIZE = int(os.getenv("COMPANY_SIZE", 5000))
START_DATE = os.getenv("START_DATE")
END_DATE = os.getenv("END_DATE")
DB_PATH = os.getenv("DB_PATH", "output/asana_simulation.sqlite")
