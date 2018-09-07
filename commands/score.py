from bot import karmas

MSG = """Hey Templar {user} you have {score} karma. Deus Vult"""
TOP_NUMBER = 10


def get_karma(**kwargs):
    """Check your Templar's karma score"""
    user = kwargs.get('user')
    if not user:
        return 'User not found'

    score = karmas.get(user)
    if score is None:
        return "Sorry Templar, you don't have any karma yet"

    return MSG.format(user=user, score=score)


def top_karma(**kwargs):
    """Ten Templars of the Eclipsed with most karma"""
    output = ['Ten Templars of the Eclipsed with most karma:']
    for person, score in karmas.most_common(TOP_NUMBER):
        output.append('{:<20} -> {}'.format(person, score))
    ret = '\n'.join(output)
    return '```{}```'.format(ret)


if __name__ == '__main__':
    user, channel, text = 'bob', '#general', 'some message'
    kwargs = dict(user=user,
                  channel=channel,
                  text=text)
    output = get_karma(**kwargs)

    output = top_karma(**kwargs)
    print(output)
