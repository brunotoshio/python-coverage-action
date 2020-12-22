import json
import logging
import os


_logger = logging.getLogger('python-coverage-action')


_logger.info(os.getcwd())
file_path = os.getenv(INPUT_FILE_PATH)

with open(file_path, 'r') as f:
    data = json.load(f)

string_content = f'## Total coverage: {data["totals"]["percent_covered"]:.2f}'

print(f'::set-output name=result::{string_content}')
