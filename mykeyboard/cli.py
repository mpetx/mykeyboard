
import xml.etree.ElementTree as ET
from pathlib import Path

help_file = Path(__file__).parent.parent / "res" / "help.txt"

def print_help_and_exit():
    from sys import stderr
    with open(help_file, "r", encoding="UTF-8") as f:
        help_content = f.read()
    stderr.write(help_content)
    exit()

def main(argv):
    if len(argv) != 2 or argv[1].startswith("-"):
        print_help_and_exit()
    with open(argv[1], "r", encoding="UTF-8") as f:
        kbd_layout = ET.ElementTree(file=f)
    from .kbd import Keyboard
    import wx
    from .mainframe import MainFrame
    keyboard = Keyboard(kbd_layout)
    app = wx.App()
    mainframe = MainFrame(keyboard)
    mainframe.Show()
    app.MainLoop()
