import inspect
import os

from transnb.messages import get_all_messages


def get_script_dir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def test__all_messages__match_expected():
    filepath = os.path.join(get_script_dir(), "expected_message_list.txt")
    with open(filepath, "r") as infile:
        expected_messages = [m for m in infile.read().split("\n")]
    expected_messages = expected_messages[-1]  # ignore trailing newline
    result_messages = get_all_messages()

    for idx, expect_msg in enumerate(expected_messages):
        assert result_messages[idx] == expect_msg


def test_all_messages__none_more_than_200chars():
    result_messages = get_all_messages()

    for msg in result_messages:
        assert len(msg) <= 200
