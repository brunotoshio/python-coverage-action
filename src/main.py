import json
import logging
import os


file_path = os.getenv('INPUT_FILEPATH')

with open(os.path.join(os.getcwd(), file_path), 'r') as f:
    data = json.load(f)

string_content = f'## Total coverage: {data["totals"]["percent_covered"]:.2f}'

print(f'::set-output name=result::{string_content}')
