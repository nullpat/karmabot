def create_commands_table(commands):
    """Help for Templars who have lost their way"""
    ret = '\n'.join(['{:<30}: {}'.format(name, func.__doc__)
                     for name, func in sorted(commands.items())])
    return '```{}```'.format(ret)
