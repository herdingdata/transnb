from dataclasses import dataclass


@dataclass
class Msg:
    """Template for messages"""

    text: str
    substitution: tuple = None


GENDER_PLURALS = ("men", "women", "people")
MESSAGES = (
    Msg("Trans {s} are {s}.", GENDER_PLURALS),
    Msg("Non binary people are non binary."),
)


def get_all_messages() -> tuple:
    messages = []
    for msg_template in MESSAGES:
        if msg_template.substitution is None:
            messages.append(msg_template.text)
        else:
            substitutions = msg_template.substitution
            for sub in substitutions:
                messages.append(msg_template.text.format(s=sub))
    return tuple(messages)
