## This script is used to insert data into the database
import glob
import os
import json
# from dotenv import load_dotenv
# from datasets import load_dataset
import pandas as pd

from utils import fast_pg_insert, get_timestamp_from_secs

# read documents files
documents_dir = './documents/'
documents_file_paths = glob.glob(os.path.join(documents_dir, '*.jsonl'))

podcasts = {}
segments = {}
print('Reading', len(documents_file_paths), 'documents...')
for i, file_path in enumerate(documents_file_paths):
    if i % 3 == 0:
        print('\tReading file', i, 'out of', len(documents_file_paths))

    with open(file_path, 'r') as file:
        for line in file:
            # extract segment data
            data = json.loads(line)
            segment_id = data['custom_id']
            raw_start_time = data['body']['metadata']['start_time']  # TODO: get timestamp
            raw_end_time = data['body']['metadata']['stop_time']      # TODO: get timestamp
            content = data['body']['input']

            # extract podcast data
            title = data['body']['metadata']['title']
            podcast_id = data['body']['metadata']['podcast_id']

            # store segment data
            segments[segment_id] = {
                'start_time': get_timestamp_from_secs(raw_start_time),
                'end_time': get_timestamp_from_secs(raw_end_time),
                'content': content,
                'podcast_id': podcast_id
            }

            # store podcast data
            if podcast_id not in podcasts:
                podcasts[podcast_id] = title
print('Done reading documents!')

# read embeddings
embeddings_dir = './embeddings/'
embeddings_file_paths = glob.glob(os.path.join(embeddings_dir, '*.jsonl'))

print('Reading', len(embeddings_file_paths), 'embedding files...')
for i, file_path in enumerate(embeddings_file_paths):
    if i % 3 == 0:
        print('\tReading file', i, 'out of', len(embeddings_file_paths))

    with open(file_path, 'r') as file:
        for line in file:
            # extract embedding
            data = json.loads(line)
            segment_id = data['custom_id']
            embedding = data['response']['body']['data'][0]['embedding']
            
            # store embedding
            segments[segment_id].update({ 'embedding': embedding })
print('Done reading embedding files!')

# HINT: In addition to the embedding and document files you likely need to load the raw data via the hugging face datasets library
# ds = load_dataset("Whispering-GPT/lex-fridman-podcast")
# === SKIP ===

# TODO: Insert into postgres
# HINT: use the recommender.utils.fast_pg_insert function to insert data into the database
# otherwise inserting the 800k documents will take a very, very long time

# create pandas DataFrame containing all the data (podcasts[podcast_id, title] and segments[segment_id, start_ime, end_time, content, embedding, podcast_id])
podcasts_df = pd.DataFrame(list(podcasts.items()), columns=['podcast_id', 'title'])
segments_df = pd.DataFrame.from_dict(segments, orient='index').reset_index()
segments_df.rename(columns={'index': 'segment_id'}, inplace=True)

print(podcasts_df)
print(segments_df)
