from typing import Tuple
import json
import logging
import os


def generate_md_string(
        filepath: str,
        th_bad: float = 70,
        th_acceptable: float = 90
    ) -> Tuple[float, str]:
    """Generates a markdown string from a coverage JSON file

    :param filepath: The path to the file
    :type filepath: str
    :param th_bad: Upper limit for a bad coverage, defaults to 70
    :type th_bad: float, optional
    :param th_acceptable: Upper limit for a acceptable coverage, defaults to 90
    :type th_acceptable: float, optional
    :return: The current coverage and the markdown string
    :rtype: Tuple[float, str]
    """
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        data = json.load(f)

    current_coverage = float(data["totals"]["percent_covered"])
    if current_coverage < th_bad:
        quality = ':rotating_light: :scream: :rotating_light: :scream: :rotating_light: :scream: :rotating_light: :scream:'
    elif current_coverage < th_acceptable:
        quality = ':warning: :thinking: :warning: :thinking: :warning: :thinking: :warning: :thinking:'
    else:
        quality = ':tada: :sunglasses: :tada: :sunglasses: :tada: :sunglasses: :tada: :sunglasses:'

    return current_coverage, f'## Total coverage: {data["totals"]["percent_covered"]:.2f} {quality}'


if __name__ == '__main__':
    file_path = os.getenv('INPUT_FILEPATH')
    threshold_bad = float(os.getenv('INPUT_THRESHOLD_BAD', 70))
    threshold_acceptable = float(os.getenv('INPUT_THRESHOLD_ACCEPTABLE', 90))
    threshold_pass = float(os.getenv('INPUT_THRESHOLD_PASS', 70))
    cov, md_output = generate_md_string(
        file_path,th_bad=threshold_bad, th_acceptable=threshold_acceptable)

    print(f'::set-output name=result::{md_output}')
    if cov >= threshold_pass:
        print(f'::set-output name=passed::true')
    else:
        print(f'::set-output name=passed::false')
