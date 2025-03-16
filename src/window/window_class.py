import wx
from graphic_utility.graphicUtility_class import GraphicUtility
from code_editor.codeEditor_class import CodeEditor

class Window(wx.Frame):
    """메인 윈도우"""
    def __init__(self):
        print("==== WINDOW.PY ====")

        super().__init__(parent=None, title="wxPython 코드 에디터 + 벡터 그래픽", size=(1000, 800), )
        
        panel = wx.Panel(self)  # 전체 패널
        sizer = wx.BoxSizer(wx.HORIZONTAL)  # 가로 배치
        
        # 좌측: 코드 편집기 (50%)
        self.code_editor = CodeEditor(panel)
        sizer.Add(self.code_editor, 1, wx.EXPAND | wx.ALL, 5)
        
        # 우측: 벡터 이미지 패널 (50%)
        self.draw_panel = GraphicUtility(panel)
        sizer.Add(self.draw_panel, 1, wx.EXPAND | wx.ALL, 5)
        
        panel.SetSizer(sizer)  # 패널에 레이아웃 적용
        self.Centre()  # 화면 중앙 배치

        print("==== WINDOW.PY OVER ====")

    def update_graphic(self, shape):
        """외부에서 그래픽을 변경할 수 있도록 메서드 추가"""
        self.draw_panel.set_shape(shape)
