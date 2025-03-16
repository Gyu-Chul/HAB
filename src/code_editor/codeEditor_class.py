import wx
import wx.stc as stc  # wxPy


class CodeEditor(stc.StyledTextCtrl):
    """좌측 코드 편집기 패널"""
    def __init__(self, parent):
        print("==== CODE_EDITOR.PY ====")
        super().__init__(parent)

        # 폰트 설정
        self.StyleSetFont(stc.STC_STYLE_DEFAULT, wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        # 문법 강조 (Python 스타일 적용)
        self.SetLexer(stc.STC_LEX_PYTHON)
        self.StyleSetForeground(stc.STC_P_COMMENTLINE, wx.Colour(0, 128, 0))  # 주석 - 초록색
        self.StyleSetForeground(stc.STC_P_STRING, wx.Colour(255, 0, 255))  # 문자열 - 보라색
        self.StyleSetForeground(stc.STC_P_NUMBER, wx.Colour(0, 0, 255))  # 숫자 - 파란색
        self.StyleSetForeground(stc.STC_P_OPERATOR, wx.Colour(255, 0, 0))  # 연산자 - 빨간색
        self.StyleSetForeground(stc.STC_P_WORD, wx.Colour(0, 0, 255))  # 키워드 - 파란색 (STC_P_KEYWORD 대신 STC_P_WORD 사용)
        
        # 키워드 목록 추가
        self.SetKeyWords(0, "def class return if else elif import from as while for try except finally with lambda yield raise pass break continue global nonlocal assert del is in and or not")

        # 자동 줄 바꿈 & 줄 번호
        self.SetMarginType(1, stc.STC_MARGIN_NUMBER)  # 줄 번호
        self.SetMarginWidth(1, 40)  # 줄 번호 너비
        self.SetWrapMode(stc.STC_WRAP_WORD)  # 자동 줄 바꿈 설정
        print("==== CODE_EDITOR.PY OVER ====")