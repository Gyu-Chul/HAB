import wx
import wx.stc as stc 

class GraphicUtility(wx.Panel):
    def __init__(self, parent, diagram=None):
        super().__init__(parent)
        print("==== GRAPHIC_UTILITY.PY ====")

        self.diagram = BasicDiagram()
        self.diagram.Rectangle(20, 20, 100, 100)        # 네모 추가
        self.diagram.Circle(200, 70, 50)                # 동그라미 추가

        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        print("==== GRAPHIC_UTILITY.PY OVER ====")

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.diagram.draw(dc)

    def set_shape(self, diagram):
        self.diagram = diagram
        self.Refresh()



class BasicDiagram:
    def __init__(self):
        self.shapes = []

    def Circle(self, x, y, radius, color=(255, 100, 100)):
        self.shapes.append({
            "type": "circle",
            "x": x,
            "y": y,
            "radius": radius,
            "color": color
        })

    def Rectangle(self, x, y, width, height, color=(100, 200, 255)):
        self.shapes.append({
            "type": "rectangle",
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "color": color
        })

    def Arrow(self, x1, y1, x2, y2, color=(0, 0, 0)):
        self.shapes.append({
            "type": "arrow",
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "color": color
        })

    def Text(self, x, y, text, font_size=12, color=(0, 0, 0)):
        self.shapes.append({
            "type": "text",
            "x": x,
            "y": y,
            "text": text,
            "font_size": font_size,
            "color": color
        })


    def Table(self, x, y, rows, cols, cell_width=80, cell_height=40, color=(200, 200, 200), contents=None):
        """
        contents: 2차원 리스트 (rows x cols) 형태의 문자열 배열
        """
        self.shapes.append({
            "type": "table",
            "x": x,
            "y": y,
            "rows": rows,
            "cols": cols,
            "cell_width": cell_width,
            "cell_height": cell_height,
            "color": color,
            "contents": contents or [[""] * cols for _ in range(rows)]  # 비어 있으면 공백 문자열로 초기화
        })

    def draw(self, dc):
        for shape in self.shapes:
            shape_type = shape["type"]
            dc.SetPen(wx.Pen(wx.Colour(0, 0, 0), 2))

            if shape_type == "circle":
                dc.SetBrush(wx.Brush(wx.Colour(*shape["color"])))
                dc.DrawCircle(shape["x"], shape["y"], shape["radius"])

            elif shape_type == "rectangle":
                dc.SetBrush(wx.Brush(wx.Colour(*shape["color"])))
                dc.DrawRectangle(shape["x"], shape["y"], shape["width"], shape["height"])

            elif shape_type == "arrow":
                dc.SetPen(wx.Pen(wx.Colour(*shape["color"]), 2))
                dc.DrawLine(shape["x1"], shape["y1"], shape["x2"], shape["y2"])
                self._draw_arrow_head(dc, shape["x1"], shape["y1"], shape["x2"], shape["y2"], shape["color"])

            elif shape_type == "text":
                dc.SetTextForeground(wx.Colour(*shape["color"]))
                font = wx.Font(shape["font_size"], wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
                dc.SetFont(font)
                dc.DrawText(shape["text"], shape["x"], shape["y"])

            elif shape_type == "table":
                dc.SetBrush(wx.Brush(wx.Colour(*shape["color"])))
                font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
                dc.SetFont(font)

                for row in range(shape["rows"]):
                    for col in range(shape["cols"]):
                        cell_x = shape["x"] + col * shape["cell_width"]
                        cell_y = shape["y"] + row * shape["cell_height"]

                        # 테두리와 배경
                        dc.DrawRectangle(cell_x, cell_y, shape["cell_width"], shape["cell_height"])

                        # 셀 텍스트 중앙 정렬
                        content = shape["contents"][row][col]
                        text_width, text_height = dc.GetTextExtent(content)
                        text_x = cell_x + (shape["cell_width"] - text_width) // 2
                        text_y = cell_y + (shape["cell_height"] - text_height) // 2
                        dc.DrawText(content, text_x, text_y)


    def _draw_arrow_head(self, dc, x1, y1, x2, y2, color):
        import math
        # 간단한 화살촉
        angle = math.atan2(y2 - y1, x2 - x1)
        arrow_length = 10
        left_angle = angle + math.radians(150)
        right_angle = angle - math.radians(150)

        left_x = x2 + arrow_length * math.cos(left_angle)
        left_y = y2 + arrow_length * math.sin(left_angle)
        right_x = x2 + arrow_length * math.cos(right_angle)
        right_y = y2 + arrow_length * math.sin(right_angle)

        dc.DrawLine(x2, y2, int(left_x), int(left_y))
        dc.DrawLine(x2, y2, int(right_x), int(right_y))
