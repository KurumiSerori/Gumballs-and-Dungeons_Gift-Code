# -*- coding: utf-8 -*-

import requests
import json
#import easygui
import wx

response = requests.post("http://wechat.leiting.com/weixin/gumballs/201610/gift/common/getGift.php", data = {"type":"1"})
# print(response.content)

data = json.loads(response.content)
code = data['message']['code']
#easygui.msgbox(code, "每日密令")
class App(wx.App):
    def OnInit(self):
        dlg = wx.MessageDialog(None, code, u"每日密令", wx.ICON_INFORMATION, wx.DefaultPosition)
        result = dlg.ShowModal()
        dlg.Destroy()
        return True

app = App()
app.MainLoop()
