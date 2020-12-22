import json
import os


file_path = os.getenv(INPUT_FILE_PATH)

with open(file_path, 'r') as f:
    data = json.load(f)

string_content = f'## Total coverage: {data["totals"]["percent_covered"]:.2f}'

print(f'::set-output name=result::{string_content}')
