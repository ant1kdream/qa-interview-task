import json
from pathlib import Path

import pytest

root_dir = Path(__file__).parent
expected_json = root_dir / 'expected' / '[expected] -> [topics].json'


@pytest.mark.parametrize(
    'actual_json', [file for file in (root_dir / 'actual').glob('*')],
    ids=lambda p: f'JSON :: {str(p).split("/")[-1]}')
def test_document_topic(actual_json):

    actual_dict = json.loads(actual_json.read_text())
    expected_dict = json.loads(expected_json.read_text())
