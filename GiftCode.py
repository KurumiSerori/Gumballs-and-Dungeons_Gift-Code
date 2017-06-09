# -*- coding: utf-8 -*-

import requests
import json
##import easygui

def GetCode():
    response = requests.post("http://wechat.leiting.com/weixin/gumballs/201610/gift/common/getGift.php", data = {"type":"1"})
##    print(response.content)
    
    data = json.loads(response.content)
    code = data['message']
    
##    fileHandle = open('code.txt', 'w')
##    fileHandle.write(code)
##    fileHandle.close()
    return code

if __name__ == "__main__":
    code = GetCode()
##    easygui.msgbox(code, "每日密令")
    import wx
    class App(wx.App):
        def OnInit(self):
            dlg = wx.MessageDialog(None, code, u"每日密令", wx.ICON_INFORMATION, wx.DefaultPosition)
            result = dlg.ShowModal()
            dlg.Destroy()
            return True
    
    app = App()
    app.MainLoop()
