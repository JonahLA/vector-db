## This script is used to create the tables in the database

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

CONNECTION = os.getenv('CONNECTION_STRING')

# need to run this to enable vector data type
CREATE_EXTENSION = "CREATE EXTENSION IF NOT EXISTS vector"

CREATE_PODCAST_TABLE = """
CREATE TABLE IF NOT EXISTS podcast (
    podcast_id TEXT,
    title TEXT,
    PRIMARY KEY (podcast_id)
)
"""
CREATE_SEGMENT_TABLE = """
CREATE TABLE IF NOT EXISTS segment (
    segment_id TEXT,
    start_time TIME,
    end_time TIME,
    content TEXT,
    embedding VECTOR,
    podcast_id TEXT,
    PRIMARY KEY (segment_id),
    FOREIGN KEY (podcast_id) REFERENCES podcast (podcast_id)
)
"""

with psycopg2.connect(CONNECTION) as conn:
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(CREATE_EXTENSION)
    cursor.execute(CREATE_PODCAST_TABLE)
    cursor.execute(CREATE_SEGMENT_TABLE)

    conn.commit()
