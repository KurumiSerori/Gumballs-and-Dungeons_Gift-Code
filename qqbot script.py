from qqbot import QQBotSched as qqbotsched, RunBot

fileHandle = open('code.txt')
code = fileHandle.read()
fileHandle.close()

@qqbotsched(hour='12', minute='5')
def mytask(bot):
    gl = bot.List('group', 'GROUPNAME')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, code)

if __name__ == '__main__':
    RunBot()
