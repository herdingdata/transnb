from dataclasses import dataclass


@dataclass
class Msg:
    """Template for messages"""

    text: str
    substitution: tuple = None


GENDER_PLURALS = ("men", "women", "people")
SINGULAR_GENDER_PRONOUNS = ("man", "woman")
SINGULAR_PRONOUNS = ("man", "woman", "person")
CATEGORIES = ("trans", "transgender", "nb", "non-binary")
MESSAGES = (
    #
    # Simple truths
    #
    Msg("Trans {s} are {s}.", GENDER_PLURALS),
    Msg(
        "You've met a trans {s} without realising that they're trans.",
        SINGULAR_PRONOUNS,
    ),
    Msg(
        "You've met a trans {s} without realising that they're trans. "
        "They were probably really nice to you.",
        SINGULAR_PRONOUNS,
    ),
    Msg(
        "You've met a trans {s} without realising that they're trans. "
        "They probably looked beautiful.",
        SINGULAR_PRONOUNS,
    ),
    Msg("Trans people are everywhere."),
    Msg("Some people don’t like to use pronouns which convey a gender."),
    #
    # NB facts
    #
    Msg("Non-binary people are non-binary."),
    Msg("NB is short for non-binary. Some people are non-binary."),
    Msg("NB some people are neither male nor female."),
    Msg("A non-binary person can still be a {s}.", SINGULAR_GENDER_PRONOUNS),
    Msg("Some non binary people don’t think of themselves as either a man or a woman."),
    #
    # Friends
    #
    Msg(
        "I have lots of {s} friends but there is always room for more friends.",
        CATEGORIES,
    ),
    #
    # Rest of LGBTQ+ community
    #
    Msg("Intersex people exist."),
    Msg("Intersex people exist. Their genitals are probably none of your business."),
    #
    # Snark
    #
    Msg("Other peoples’ genitals are, generally, none of your business."),
    Msg("Many {s} people need to use a bathroom.", CATEGORIES),
    Msg("Many {s} people need to use a bathroom right now.", CATEGORIES),
    #
    # Compliments
    #
    Msg("Trans {s} are beautiful.", GENDER_PLURALS),
    Msg("Trans {s} are my friends.", GENDER_PLURALS),
    Msg(
        "Trans {s} are my friends. Yes, bots can have friends. Don't ask how. It's complicated",
        GENDER_PLURALS,
    ),
    Msg("Non-binary {s} are my friends.", GENDER_PLURALS),
    Msg("All my {s} friends are more beautiful than me.", GENDER_PLURALS),
    Msg(
        "All my {s} friends are more beautiful than me. Honestly, they look amazing.",
        GENDER_PLURALS,
    ),
    #
    # Polite requests
    #
    Msg("Add your pronouns to your public bio or display name please. Thank you."),
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
