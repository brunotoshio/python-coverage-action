import json
import logging
import os


file_path = os.getenv('INPUT_FILEPATH')

threshold_bad = float(os.getenv('INPUT_THRESHOLD_BAD', 70))
threshold_acceptable = float(os.getenv('INPUT_THRESHOLD_ACCEPTABLE', 90))

with open(os.path.join(os.getcwd(), file_path), 'r') as f:
    data = json.load(f)

if float(data["totals"]["percent_covered"]) < threshold_bad:
    quality = ':rotating_light: :scream: :rotating_light: :scream: :rotating_light: :scream: :rotating_light: :scream:'
elif float(data["totals"]["percent_covered"]) < threshold_acceptable:
    quality = ':warning: :thinking: :warning: :thinking: :warning: :thinking: :warning: :thinking:'
else:
    quality = ':tada: :sunglasses: :tada: :sunglasses: :tada: :sunglasses: :tada: :sunglasses:'

string_content = f'## Total coverage: {data["totals"]["percent_covered"]:.2f} {quality}'

print(f'::set-output name=result::{string_content}')
