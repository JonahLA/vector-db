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

q1_prompt = 'Q1: What are the five most similar segments to segment "267:476"?'
q1_sql = """
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '267:476') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '267:476'
ORDER BY distance
LIMIT 5
"""

q2_prompt = 'Q2: What are the five most dissimilar segments to segment "267:476"?'
q2_sql = """
SELECT
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT temp.embedding FROM temp.segment WHERE temp.segment_id = '267:476') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
ORDER BY distance DESC
LIMIT 5
"""

q3_prompt = 'Q3: What are the five most similar segments to segment "48:511"?'
q3_sql = """
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT temp.embedding FROM temp.segment WHERE temp.segment_id = '48:511') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '48:511'
ORDER BY distance
LIMIT 5
"""

q4_prompt = 'Q4: What are the five most similar segments to segment "51:56"?'
q4_sql = """
SELECT 
    title AS podcast_name,
    segment_id,
    content,
    start_time,
    end_time,
    embedding <-> (SELECT temp.embedding FROM temp.segment WHERE temp.segment_id = '51:56') AS distance
FROM segment
    JOIN podcast ON podcast.podcast_id = segment.podcast_id
WHERE segment_id <> '51:56'
ORDER BY distance
LIMIT 5
"""

# Segments ('267:476', '48:511', '51:56')
q5_prompt = 'Q5: For each of the following segments, find the five most similar podcast episodes.'
q5_sql = """
WITH ranked_podcasts AS (
    SELECT 
        p.title,
        '267:476' AS segment_id,
        AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '267:476')) AS avg_distance,
        RANK() OVER (PARTITION BY '267:476' ORDER BY 
            AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '267:476'))
        ASC) AS rank
    FROM podcast p
    JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.title

    UNION ALL

    SELECT 
        p.title,
        '48:511' AS segment_id,
        AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '48:511')) AS avg_distance,
        RANK() OVER (PARTITION BY '48:511' ORDER BY 
            AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '48:511'))
        ASC) AS rank
    FROM podcast p
    JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.title

    UNION ALL

    SELECT 
        p.title,
        '51:56' AS segment_id,
        AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '51:56')) AS avg_distance,
        RANK() OVER (PARTITION BY '51:56' ORDER BY 
            AVG(s.embedding <-> (SELECT temp.embedding FROM segment temp WHERE temp.segment_id = '51:56'))
        ASC) AS rank
    FROM podcast p
    JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.title
)

SELECT segment_id, title, avg_distance
FROM ranked_podcasts
WHERE rank <= 5
ORDER BY segment_id, rank
""" 

# Find the give other podcasts whose AVERAGE embedding is "closest" to the AVERAGE embedding for this podcast
q6_prompt = 'Q6: For podcast episode id = VeH7qKZr0WI, find the five most similar podcast episodes.'
q6_sql = """
WITH podcast_avgs AS (
    SELECT
        p.podcast_id,
        p.title,
        AVG(s.embedding) AS avg_embedding
    FROM podcast p
        JOIN segment s ON s.podcast_id = p.podcast_id
    GROUP BY p.podcast_id, p.title
)

SELECT
    podcast_avgs.title,
    podcast_avgs.avg_embedding <-> (SELECT temp.avg_embedding FROM podcast_avgs temp WHERE temp.podcast_id = 'VeH7qKZr0WI') AS distance
FROM podcast_avgs
WHERE podcast_avgs.podcast_id <> 'VeH7qKZr0WI'
ORDER BY distance
LIMIT 5
"""

# === RUN QUERIES ===
queries = {
    q1_prompt: q1_sql,
    q2_prompt: q2_sql,
    q3_prompt: q3_sql,
    q4_prompt: q4_sql,
    q5_prompt: q5_sql,
    q6_prompt: q6_sql,
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
