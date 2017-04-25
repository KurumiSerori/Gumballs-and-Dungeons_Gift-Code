from qqbot import QQBotSched as qqbotsched, RunBot
import GiftCode

@qqbotsched(hour='12', minute='05')
def mytask(bot):
    code = GiftCode.GetCode()
    gl = bot.List('group', 'GROUPNAME')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, code)

if __name__ == '__main__':
    RunBot()
