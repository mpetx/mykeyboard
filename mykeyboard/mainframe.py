
import wx

class MainFrame(wx.Frame):

    def __init__(self, keyboard):
        super().__init__(None, title=self.get_frame_title(keyboard), size=(840, 540))
        panel = wx.Panel(self)
        top_box = wx.BoxSizer(wx.VERTICAL)
        # コピーボタンを追加
        copy_button = wx.Button(panel, label="コピー", size=(8 * 12, 28))
        copy_button.Bind(wx.EVT_BUTTON, self.on_copy_button_clicked)
        top_box.Add(copy_button, flag=wx.RIGHT | wx.TOP | wx.ALIGN_RIGHT, border=10)
        # テキストエリアを追加
        text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.text_ctrl = text
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        text.SetFont(font)
        top_box.Add(text, flag=wx.EXPAND | wx.ALL, proportion=3, border=10)
        # キーボードを追加
        keys = wx.GridSizer(keyboard.column_count)
        for row in range(0, keyboard.row_count):
            for column in range(0, keyboard.column_count):
                if column >= len(keyboard.rows[row]):
                    key = None
                else:
                    key = keyboard.rows[row][column]
                if key == None:
                    keys.Add(wx.StaticText(panel))
                else:
                    button = wx.Button(panel, label=key.label, size=(1,28))
                    button.Bind(wx.EVT_BUTTON, self.on_key_clicked(key))
                    keys.Add(button, flag=wx.GROW)
        top_box.Add(keys, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, proportion=0, border=10)
        panel.SetSizer(top_box)

    def on_key_clicked(self, key):
        def handler(evt):
            if wx.GetKeyState(wx.WXK_SHIFT):
                letter = key.upper
            else:
                letter = key.lower
            self.text_ctrl.WriteText(letter)
            self.text_ctrl.SetFocus()
        return handler

    def on_copy_button_clicked(self, evt):
        value = self.text_ctrl.GetValue()
        clipboard = wx.Clipboard()
        clipboard.SetData(wx.TextDataObject(value))
        clipboard.Flush()
        clipboard.Close()
        from wx.adv import NotificationMessage
        message = NotificationMessage("MyKeyboard", "テキストをクリップボードに書き込みました。")
        message.Show()

    def get_frame_title(self, keyboard):
        if keyboard.name == None:
            return "MyKeyboard"
        else:
            return f"My Keyboard - {keyboard.name}"
