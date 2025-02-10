## This script is used to insert data into the database
import gc
import glob
import os
import json
from dotenv import load_dotenv
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
print('\tDone reading documents!')

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
print('\tDone reading embedding files!')

# HINT: In addition to the embedding and document files you likely need to load the raw data via the hugging face datasets library
# ds = load_dataset("Whispering-GPT/lex-fridman-podcast")
# === SKIP ===

# create pandas DataFrame containing all the data (podcasts[podcast_id, title] and segments[segment_id, start_ime, end_time, content, embedding, podcast_id])
podcasts_df = pd.DataFrame(list(podcasts.items()), columns=['podcast_id', 'title'])
segments_df = pd.DataFrame.from_dict(segments, orient='index').reset_index()
segments_df.rename(columns={'index': 'segment_id'}, inplace=True)

# collect memory
del podcasts
gc.collect()
del segments
gc.collect()

# load data into database
load_dotenv()
CONNECTION = os.getenv('CONNECTION_STRING')
PODCAST_TABLE = 'podcast'
SEGMENT_TABLE = 'segment'

# insert podcasts
print('Uploading podcasts...')
fast_pg_insert(podcasts_df, CONNECTION, PODCAST_TABLE, list(podcasts_df.columns))
print('\tDone!')

# batch the segments because it is so big
BATCH_SIZE = 50_000

curr_pos = 0
last_line = segments_df.size
print('Uploading segment items...')
while curr_pos < last_line:
    end_batch = last_line if (curr_pos + BATCH_SIZE > last_line) else curr_pos + BATCH_SIZE
    print('\tUploading items', curr_pos, 'through', end_batch)
    fast_pg_insert(segments_df.iloc[curr_pos:end_batch], CONNECTION, SEGMENT_TABLE, list(segments_df.columns))
    curr_pos = end_batch
print('\tDone!')
