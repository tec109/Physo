import wx


class GUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        quitItem = wx.MenuItem(fileMenu, 1, '&Quit')
        fileMenu.Append(quitItem)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Centre()
        self.SetTitle('Physo')

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    gui = GUI(None)
    gui.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
