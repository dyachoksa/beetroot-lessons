import wx

class ApplicationFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        panel = wx.Panel(self)

        text = wx.StaticText(panel, label="Hello, world!")
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)

        btn = wx.Button(panel, label="Click me")
        self.Bind(wx.EVT_BUTTON, self.onBtnClick, btn)

        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(text, wx.SizerFlags().Border(wx.ALL, 25))
        # sizer.Add(btn, wx.SizerFlags().Border(wx.ALL, 25))

        sizer = wx.GridBagSizer(10, 10)
        sizer.Add(text, pos=(0, 0), flag=wx.ALL|wx.ALIGN_CENTER)
        sizer.Add(btn, pos=(0, 1))

        panel.SetSizer(sizer)

        self.CreateStatusBar()
        self.SetStatusText("Ready...")
    
    def onBtnClick(self, event):
        # wx.MessageBox("This is a wxPython Hello World sample", "Information", wx.OK|wx.ICON_INFORMATION)
        wx.InfoMessageBox(self)

if __name__ == "__main__":
    app = wx.App()
    
    app_frame = ApplicationFrame(None, title="wxWidgets Application")
    app_frame.Show()

    app.MainLoop()
