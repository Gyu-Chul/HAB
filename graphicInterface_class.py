from window.window_class import Window
import wx

class GraphicInterface:
    
    def __init__(self):
        print("GraphicInterface class created in hab.py\n")

    def run(self):
        print("==== GRAPHICINTERFACE.PY ====")
        app = wx.App(False)
        frame = Window()
        frame.Show()
        app.MainLoop()
        print("==== GRAPHICINTERFACE.PY OVER ====")