import json
import os


filename = os.getenv(INPUT_FILENAME)

with open(filename, 'r') as f:
    data = json.load(f)

string_content = f'## Total coverage: {data["totals"]["percent_covered"]:.2f}'

print(f'::set-output name=result::{string_content}')
