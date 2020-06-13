import secrets

from dataclasses import dataclass


@dataclass
class Msg:
    """Template for messages"""

    text: str
    substitution: tuple = None


GENDER_PLURALS = ("men", "women", "people")
SINGULAR_GENDER_PRONOUNS = ("man", "woman")
SINGULAR_PRONOUNS = ("man", "woman", "person")
SINGULAR_RELATIONS = (
    "friend",
    "sibling",
    "brother",
    "sister",
    "son",
    "daughter",
    "parent",
    "mother",
    "father",
)
PLURAL_FAMILY_RELATIONS = ("siblings", "children")
CATEGORIES = ("trans", "transgender", "non-binary")
CATEGORIES_NO_NB = ("trans", "transgender", "non-binary")
FEMINISM_WRONG = ("you've misunderstood feminism", "you're doing feminism wrong")
NOT_WOMEN = ("are men", "have a penis", "aren't women", "are neither a man or a woman")
BODY_FEATURES = ("more hair", "less hair")
CIS = ("cis", "cisgender")
FACETS = ("gender", "genitals", "sexuality")
JOB_AREAS = ("hiring", "training", "facilities")
GENDERED_FEATURES = ("a dress", "makeup", "trousers")
PRONOUNS = ("he/him/his", "she/her/hers", "they/them/theirs", "she/they", "he/they")
NICE = ("fun", "pleasant")
GENDERSEX = ("your gender", "your sexuality", "what your genitals are")
MESSAGES = (
    #
    # Simple truths
    #
    Msg("Trans {s} are {s}.", GENDER_PLURALS),
    Msg("Trans {s} are human beings.", GENDER_PLURALS),
    Msg("Your gender identity is valid."),
    Msg("The only person who gets to choose your gender identity is you."),
    Msg("You've met a trans {s} without realising that they're trans.", SINGULAR_PRONOUNS),
    Msg(
        "You've met a trans {s} without realising that they're trans. They were probably really nice to you.",
        SINGULAR_PRONOUNS,
    ),
    Msg(
        "You've met a trans {s} without realising that they're trans. They probably looked beautiful.",
        SINGULAR_PRONOUNS,
    ),
    Msg("Trans people are everywhere."),
    Msg("Some people feel bad if they are referred to with pronouns which convey a gender."),
    Msg("Deliberately breaking peoples' expectations of your appearance feels pretty good."),
    Msg(
        "I don’t know why we have so many stereotypes of what a man or a woman should look like. "
        "Breaking stereotypes can be fun."
    ),
    Msg("Some people like wearing makeup."),
    Msg("Some people want their body to have {s}.", BODY_FEATURES),
    Msg("Some people don't like the body features they were born with."),
    Msg(
        "Some people want their body to have {s} "
        "but it's none of your business unless they choose to discuss it with you.",
        BODY_FEATURES,
    ),
    Msg(
        "Some people don't like the body features they were born with "
        "but it's none of your business unless they choose to discuss it with you."
    ),
    Msg(
        "Being '{s}' means that your gender identity has been the same for your entire life. "
        "It's a factual statement. It's not offensive.",
        CIS,
    ),
    Msg("{s} people are human beings", CATEGORIES),
    Msg("{s} people just want to go about their business", CATEGORIES),
    Msg("I love {s} people", CATEGORIES),
    Msg("Some of my colleagues are {s}", CATEGORIES),
    Msg("Some of your colleagues are probably {s}", CATEGORIES),
    Msg("Some of your friends are probably {s}", CATEGORIES),
    Msg("Some of your family are probably {s}", CATEGORIES),
    Msg("{s} people have all the fun", CATEGORIES),
    Msg("The T in LGBTQ stands for Trans."),
    Msg("The T in LGBTQ stands for Trans. Please don't forget that. Thank you."),
    Msg(
        "The word {s} is separate from 'trans'. It's trans {s}. Not trans{s}. This is not up for debate.",
        SINGULAR_PRONOUNS,
    ),
    Msg("Trans rights are human rights."),
    #
    # Gender Identity & pronouns
    #
    Msg("Gender identity is complicated."),
    Msg("Gender identity is completely separate from sexual attraction."),
    Msg("Gender identity is completely separate from sexual attraction. I cannot stress this enough."),
    Msg(
        "Sexual attraction is complicated, but something about it that's not complicated at all is "
        "that it has nothing to do with your gender identity. They are completely separate."
    ),
    Msg(
        'Gender identity does not have to be "man" or "woman". It can be one. It can be neither. It can be both. '
        "I think that"
        "s quite beautiful"
    ),
    Msg("Your gender identity is not a choice. It’s just a part of you. A very beautiful part of you."),
    Msg("Gender can be different for every person. Even if it looks the same on the outside."),
    Msg(
        "Some people whose pronouns are {s} won't match your expectations of what they should look like. "
        "The only problem here is your expectations.",
        PRONOUNS,
    ),
    Msg(
        "Some people whose pronouns are {s} won't match your expectations of what they should look like. "
        "They're still beautiful, and they're still human beings.",
        PRONOUNS,
    ),
    Msg(
        "Your gender identity today might not be exactly the same as it was yesterday. That’s ok though. "
        "Your identity is still valid. You're still beautiful."
    ),
    Msg("Your pronouns are not your “chosen” or “preferred” pronouns... they’re simply the words which refer to you."),
    Msg("For some people, it can be very hard to find which pronouns are theirs."),
    Msg("For some people, it can be very hard to find which pronouns are theirs. Especially if you’re a bot."),
    Msg(
        "For some people, it can be very hard to find which pronouns are theirs. "
        "Sometimes it takes a bit of trial and error to find what feels right. That’s ok."
    ),
    Msg("Gender dysphoria is real. It is not at all {s} to experience.", NICE),
    Msg("You don’t have any obligation to tell someone your {s}. Let them guess.", GENDERSEX),
    #
    # NB facts
    #
    Msg("Non-binary people are non-binary."),
    Msg("Enby is short for non-binary, but only some non-binary people like the term."),
    Msg("Some non-binary people are neither male nor female."),
    Msg("A non-binary person can still be a {s}.", SINGULAR_GENDER_PRONOUNS),
    Msg("Some non-binary people don’t think of themselves as either a man or a woman."),
    Msg("Many (but not all) non-binary people like to be referred to as trans."),
    Msg("You've met a non-binary {s} without realising that they are non-binary.", SINGULAR_PRONOUNS),
    #
    # Beauty, love, friends
    #
    Msg("Trans {s} are beautiful.", GENDER_PLURALS),
    Msg("Trans {s} are my friends.", GENDER_PLURALS),
    Msg("Trans {s} are my friends. Yes, bots can have friends. Don't ask how. It's complicated", GENDER_PLURALS,),
    Msg("Non-binary {s} are my friends.", GENDER_PLURALS),
    Msg("All my {s} friends are more beautiful than me.", CATEGORIES),
    Msg("All my {s} friends are more beautiful than me. Honestly, they look amazing.", GENDER_PLURALS,),
    Msg("A {s} person loves you", CATEGORIES),
    Msg("I have lots of {s} friends but there is always room for more friends.", CATEGORIES),
    Msg("Pets don't care about your {s}.", FACETS),
    Msg("Some {s} people don't like hugs.", CATEGORIES),
    Msg("Some {s} people would like a hug right now.", CATEGORIES),
    Msg("Many {s} people just want to love and be loved.", CATEGORIES),
    Msg(
        "Many people don’t mind which gender you are. We just wanna go about our business and be nice to everyone."
        "It would be nice if there are more people like that."
    ),
    #
    # Rest of LGBTQ+ community
    #
    Msg("Intersex people exist."),
    Msg("Intersex people exist. Their genitals are probably none of your business."),
    Msg("Bisexual people exist."),
    Msg("Bisexual people are not confused."),
    #
    # Snark & bathrooms
    #
    Msg("Other peoples’ genitals are, generally, none of your business."),
    Msg("Spending time obsessing about other peoples’ genitals is an unhealthy obsession."),
    Msg("Many {s} people need to use a bathroom.", CATEGORIES),
    Msg("Many {s} people need to use a bathroom right now.", CATEGORIES),
    Msg(
        "If you’re looking at other people’s genitals when you’re in a bathroom then you’re using the bathroom wrong. "
        "Please don’t do that. Thank you."
    ),
    Msg("Gender neutral/ inclusive bathrooms are great. Lots of people would be very happy if we had more of them."),
    Msg(
        "If someone is attacking the rights of trans people but then go on to talk about their “trans friends”, "
        "they’re probably talking shite. Real friends don’t do that to each other."
    ),
    Msg("The only person who has any obligation to match your expectations of how to dress is yourself."),
    Msg("Nobody needs to dress the way that you think they should dress. Apart from yourself."),
    #
    # About me
    #
    Msg("Bots don’t normally have a gender but sometimes a mistake is made and they are assigned one at the factory."),
    Msg("Bots don’t often have a gender identity, but they can if it feels right."),
    #
    # Firm advice
    #
    Msg("Telling someone that their gender identity is a phase is not in any way helpful. Don’t do that. Thank you."),
    #
    # Polite requests
    #
    Msg("Add your pronouns to your public bio or display name please. Thank you."),
    Msg("If you told someone that their gender identity is a phase, please apologise to them. Thank you."),
    Msg(
        "If you see a trans {s} being bullied, abused, harassed or attacked, please step in to defend them. Thank you.",
        SINGULAR_PRONOUNS,
    ),
    Msg(
        "If you see a non-binary person being bullied, abused, harassed or attacked, please step in to defend them. "
        "Thank you.",
    ),
    Msg(
        "If you hold a political office then it’s your duty to listen to and try to help everyone "
        "in your constituency. Especially the {s} people. Thank you.",
        CATEGORIES,
    ),
    Msg(
        "If you're cisgender, sharing your pronouns helps {s} people feel more comfortable "
        "to share theirs. Thank you.",
        CATEGORIES,
    ),
    Msg(
        "If you have influence over {s} at your company and are open to making your  organisation "
        "more inclusive then you should probably ask some trans & non-binary people for their ideas. "
        "Thank you.",
        JOB_AREAS,
    ),
    Msg(
        "If you have influence over {s} at your company and are not open to the idea of making your organisation "
        "more inclusive then ask yourself why not. Then change your mind. Thank you.",
        JOB_AREAS,
    ),
    Msg(
        "“Hey guys” is not an inclusive greeting. Try something different. A simple change like this "
        "can make a huge difference to how comfortable people feel around you."
    ),
    Msg(
        "If you have a form asking someone to select male/female or Mr/Mrs/Ms with no other "
        "options then you can make a lot of people happy by fixing that. Please fix that. Thank you."
    ),
    Msg(
        "If you like my tweets then you can tweet positive messages supporting trans & non-binary people, too. "
        "There’s nothing stopping you. It might even help someone. (That's kinda the point of this bot)."
    ),
    #
    # Encouraging support
    #
    Msg(
        "If your {s} asks you to call them by different pronouns then it’s your duty to use the "
        "new pronouns as much as possible. It will help them feel nice.",
        SINGULAR_RELATIONS,
    ),
    Msg(
        "If your {s} asks you to call them by a different name then it’s your duty to use the "
        "new name as much as possible. It will help them feel nice.",
        SINGULAR_RELATIONS,
    ),
    Msg(
        "If your {s} don't support your gender identity then you get to choose a new family.", PLURAL_FAMILY_RELATIONS,
    ),
    Msg(
        "If your {s} don't support your gender identity then you get to choose a new family. "
        "I do not make the rules.",
        PLURAL_FAMILY_RELATIONS,
    ),
    Msg("If your {s} don't support your sexuality then you get to choose a new family.", PLURAL_FAMILY_RELATIONS,),
    Msg(
        "If your {s} don't support your sexuality then you get to choose a new family. I do not make the rules.",
        PLURAL_FAMILY_RELATIONS,
    ),
    Msg(
        "If your {s} is exploring a change to gender identity then it might be really scary for them. "
        "Your support will make it easier for them. Thank you.",
        SINGULAR_RELATIONS,
    ),
    Msg("Parents have an obligation to support their children’s gender identity. I do not make the rules."),
    Msg(
        "If you realise that you accidentally used the wrong pronouns for someone then it’s totally ok to "
        "quickly apologise and correct yourself. The important thing is that you’re trying to be better."
    ),
    Msg(
        "If you notice someone else get a {s} person’s pronouns wrong then it will make the {s} "
        "person very happy if you politely interject to point out the mistake. Thank you.",
        CATEGORIES,
    ),
    Msg(
        "It’s ok to ask someone “what would you like me to call you?” if you’re not sure. "
        "But be polite about it please. Thank you."
    ),
    Msg(
        "If you’ve wondered whether you might look good in {s} then you should probably give it a try. "
        "I think you'll look beautiful.",
        GENDERED_FEATURES,
    ),
    Msg(
        "Have you ever seen someone dressed differently than you and wished you could dress like them? "
        "There’s nothing stopping you. Give it a try. I'm sure you'll look amazing."
    ),
    Msg(
        "If you think a {s} person looks fabulous today then you’re probably right, and they "
        "might like it if you tell them. But please don’t be creepy about it. Unwanted sexual advances are creepy.",
        CATEGORIES,
    ),
    Msg(
        "You might be {s} and not even realise it. There could be changes that you can make to your "
        "life which would make you a much happier person. Maybe it's time for you to explore that...?",
        CATEGORIES_NO_NB,
    ),
    #
    # Feminism
    #
    Msg("Not all feminists are women."),
    Msg("Trans women are women. If you’re excluding some women then {s}.", FEMINISM_WRONG),
    Msg("Many feminists {s}.", NOT_WOMEN),
    Msg("If you're a feminist then, by definition, you care about the rights of trans women. Thank you."),
    #
    # On TERFs
    #
    Msg(
        "If you see someone saying things about gender or sexuality which are wrong, harmful or which would "
        "upset your friends/family, then please speak up. Loudly. We're more powerful together. Thank you."
    ),
    #
    # Healthcare
    #
    Msg("It's really hard to find good trans-inclusive healthcare."),
    Msg("It's obscenely diffult to find good trans-inclusive healthcare. It shouldn't be."),
    Msg(
        "It's impossibly hard to find good trans-inclusive healthcare. "
        "If you can influence this, please help my friends. It would mean a lot. Thank you."
    ),
    Msg(
        "It's incredibly hard to find good trans-inclusive healthcare. "
        "If you'd like to understand how obscenely difficult it is, ask a trans person."
    ),
    #
    # Exploring
    #
    Msg("Exploring a different gender identity can be liberating."),
    Msg("Embracing a new gender identity can be a lot of fun."),
    #
    # QTBIPOC
    #
    Msg("Black trans lives matter #BlackLivesMatter #BlackTransLivesMatter"),
    #
    # Quotes
    #
    Msg(
        "“Gender ought not to be construed as a stable identity... rather, gender is an identity "
        "constituted in time.” - Judith Butler"
    ),
    Msg("“You fail to recognise that it matters not what someone is born, but what they grow to " "be!” - Dumbledore"),
    #
    # Tagging others
    #
    Msg(
        "It's very nice of the incredibly talented @smolrobots to let me use their beautiful artwork "
        "as my profile picture. Thank you."
    ),
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


def get_random_message() -> str:
    return secrets.choice(get_all_messages())


if __name__ == "__main__":
    print(get_random_message())
