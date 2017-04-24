from qqbot import QQBotSched as qqbotsched, RunBot
import os

@qqbotsched(hour='12', minute='5')
def mytask(bot):
    os.system('python "Gift Code.py"')
    fileHandle = open('code.txt')
    code = fileHandle.read()
    fileHandle.close()
    gl = bot.List('group', 'GROUPNAME')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, code)

if __name__ == '__main__':
    RunBot()
