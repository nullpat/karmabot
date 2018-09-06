""" private command, not callable """
from random import choice

# thanks Erik!
WELCOME_MSG = """Welcome {user}++!

>>> random.choice(pybites_init_questions)
{welcome_question}

My creators are making me smarter, type this if you need anything:
`@karmabot help`
"""
# some Pythonic welcome questions
WELCOME_QUESTIONS = """Deus Vult
Kill them all, God will sort them out"""


def welcome_user(user):
    """Welcome new Templars of the Eclipsed member"""
    questions = WELCOME_QUESTIONS.split('\n')
    random_question = choice(questions)
    return WELCOME_MSG.format(user=user['name'],
                              welcome_question=random_question)


if __name__ == '__main__':
    output = welcome_user(dict(name='bob'))
    print(output)
