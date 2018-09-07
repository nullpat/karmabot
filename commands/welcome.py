""" private command, not callable """
from random import choice

# thanks Erik!
WELCOME_MSG = """Welcome {user} ++!

Introduce yourself if you like ...
- Which holy order do you belong to?
- What is your favorite way to kill the nonbelievers?
- And: >>> random.choice(pybites_init_questions)
{welcome_question}

My creators are making me smarter, type this if you need anything:
`@karmabot help`
Although you will meet some awesome folks here, you can also talk to me :)
Type `help` in a direct message to me (@karmabot) to get started ...
"""
# some Pythonic welcome questions
WELCOME_QUESTIONS = """Deus Vult
Kill them all, God will sort them out"""


def welcome_user(user):
    """Welcome new Templar of the Eclipsed"""
    questions = WELCOME_QUESTIONS.split('\n')
    random_question = choice(questions)
    return WELCOME_MSG.format(user=user['name'],
                              welcome_question=random_question)


if __name__ == '__main__':
    output = welcome_user(dict(name='bob'))
    print(output)
