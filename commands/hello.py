MSG = """Templar {user}, how are you doing today?"""


def hello_user(**kwargs):
    """Hello world of Templars"""
    user = kwargs.get('user')
    if not user:
        return None
    return MSG.format(user=user)


if __name__ == '__main__':
    user, channel, text = 'bob', '#general', 'some message'
    kwargs = dict(user=user,
                  channel=channel,
                  text=text)
    output = hello_user(**kwargs)
    print(output)
