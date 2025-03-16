import wx
import wx.stc as stc 

class GraphicUtility(wx.Panel):

    def __init__(self, parent):
        print("==== GRAPHIC_UTILITY.PY ====")

        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))  # 흰색 배경
        self.Bind(wx.EVT_PAINT, self.OnPaint)  # 그리기 이벤트 바인딩


        print("==== GRAPHIC_UTILITY.PY OVER ====")

    def OnPaint(self, event):
        """동그라미와 네모를 그리는 함수"""
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush(wx.Colour(100, 200, 255)))  # 연한 파란색 채우기
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0), 3))  # 검은색 테두리, 두께 3
        
        # 네모 (x=20, y=20, width=100, height=100)
        dc.DrawRectangle(20, 20, 100, 100)

        # 동그라미 (x=200, y=70, radius=50)
        dc.SetBrush(wx.Brush(wx.Colour(255, 100, 100)))  # 연한 빨간색 채우기
        dc.DrawCircle(200, 70, 50)  # 중심 좌표 (200, 70), 반지름 50
