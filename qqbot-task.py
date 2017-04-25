from qqbot import QQBotSched as qqbotsched, RunBot
from qqbot import QQBotSlot as qqbotslot, RunBot
import GiftCode

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content == 'ml':
        bot.SendTo(contact, GiftCode.GetCode())
    elif content == '-stop':
        bot.SendTo(contact, 'Closing')
        bot.Stop()

@qqbotsched(hour='12', minute='05')
def mytask(bot):
    code = GiftCode.GetCode()
    gl = bot.List('group', 'GROUPNAME')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, code)

if __name__ == '__main__':
    RunBot()
