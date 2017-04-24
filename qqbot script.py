from qqbot import QQBotSched as qqbotsched, RunBot

@qqbotsched(hour='12', minute='5')
def mytask(bot):
    gl = bot.List('group', 'GROUPNAME')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '')

if __name__ == '__main__':
    RunBot()