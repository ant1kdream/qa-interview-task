import json
from pathlib import Path
from pprint import pprint

import pytest

root_dir = Path(__file__).parent
reference_json = root_dir / "expected" / "[expected] -> [scene].json"
actual_json = root_dir / "actual" / "[actual] -> [scene].json"


def test_scene():
    actual_dict = json.loads(actual_json.read_text())
    reference_dict = json.loads(reference_json.read_text())

    pprint(reference_dict)
    pprint(actual_dict)
