## This script is used to create the tables in the database

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

CONNECTION = os.getenv('CONNECTION_STRING')

# need to run this to enable vector data type
CREATE_EXTENSION = "CREATE EXTENSION vector"

CREATE_PODCAST_TABLE = """
CREATE TABLE IF NOT EXISTS Podcast (
    podcast_id INTEGER,
    title TEXT,
    PRIMARY KEY (podcast_id)
)
"""
CREATE_SEGMENT_TABLE = """
CREATE TABLE Segment (
    segment_id INTEGER,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    content TEXT,
    embedding VECTOR,
    podcast_id INTEGER,
    PRIMARY KEY (segment_id),
    FOREIGN KEY (podcast_id) REFERENCES Podcast (podcast_id)
)
"""

with psycopg2.connect(CONNECTION) as conn:
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(CREATE_EXTENSION)
    cursor.execute(CREATE_PODCAST_TABLE)
    cursor.execute(CREATE_SEGMENT_TABLE)

    conn.commit()
