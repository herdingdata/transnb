import inspect
import os

from transnb.commands import all


def get_script_dir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def test__all_messages__match_expected():
    filepath = os.path.join(get_script_dir(), "expected_message_list.txt")
    with open(filepath, "r") as infile:
        expected_messages = [m for m in infile.read().split("\n")]
    result_messages = all()

    assert result_messages == expected_messages
