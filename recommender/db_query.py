## This script is used to query the database
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

CONNECTION = os.getenv('CONNECTION_STRING')

# === TABLES REF ===
# podcast (
#     podcast_id TEXT,
#     title TEXT
# )

# segment (
#     segment_id TEXT,
#     start_time TIME,
#     end_time TIME,
#     content TEXT,
#     embedding VECTOR,
#     podcast_id TEXT
# )

# === WRITE QUERIES ===
# recall that <-> is L2 distance

# Q1: What are the five most similar segments to segment "267:476"?
q1_prompt = 'Q1: What are the five most similar segments to segment "267:476"?'
q1_sql = """
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '267:476') AS distance
FROM segment
JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '267:476'
ORDER BY distance
LIMIT 5
"""

# Q2: What are the five most dissimilar segments to segment "267:476"?
q2_prompt = 'Q2: What are the five most dissimilar segments to segment "267:476"?'
q2_sql = """
SELECT
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '267:476') AS distance
FROM segment
JOIN podcast ON podcast.podcast_id = segment.podcast_id
ORDER BY distance DESC
LIMIT 5
"""

# Q3: What are the five most similar segments to segment "48:511"?
q3_prompt = 'Q3: What are the five most similar segments to segment "48:511"?'
q3_sql = """
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '48:511') AS distance
FROM segment
JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '48:511'
ORDER BY distance
LIMIT 5
"""

# Q4: What are the five most similar segments to segment "51:56"?
q4_prompt = 'Q4: What are the five most similar segments to segment "51:56"?'
q4_sql = """
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT embedding FROM segment WHERE segment_id = '51:56') AS distance
FROM segment
JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '51:56'
ORDER BY distance
LIMIT 5
"""

# === RUN QUERIES ===
queries = {
    q1_prompt: q1_sql,
    q2_prompt: q2_sql,
    q3_prompt: q3_sql,
    q4_prompt: q4_sql,
}
with psycopg2.connect(CONNECTION) as conn:
    for prompt, sql in queries.items():
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

        print(prompt)
        for row in cursor.fetchall():
            print(row)
        print('---')
