## This script is used to query the database
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

CONNECTION = os.getenv('CONNECTION_STRING')



# === RUN QUERIES ===
with psycopg2.connect(CONNECTION) as conn:
    
    pass
