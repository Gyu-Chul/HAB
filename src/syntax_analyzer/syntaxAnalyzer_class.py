import ast
import sys
import ctypes
from pympler import asizeof  # 전체 객체 크기 측정


class SyntaxAnalyzer(ast.NodeTransformer):

    def __init__(self, filePath):
        self.filePath = filePath
        self.originalAstTree = None
        self.habAstTree = None
        print("SyntaxAnalyzer class created in Interpreter.py\n")

    def run(self):
        print("==== SYNTAX_ANALYZER.PY ====")

        with open(self.filePath, "r", encoding="utf-8") as f:
            sourceCode = f.read()

        self.originalAstTree = ast.parse(sourceCode)

        self.habAstTree = self.visit(self.originalAstTree)
        ast.fix_missing_locations(self.habAstTree)
        print("==== SYNTAX_ANALYZER.PY OVER ====")

        return self.originalAstTree

    def printOriginalAstTree(self):
        print(ast.dump(self.originalAstTree, indent=4))  # 보기 좋게 출력

    def visit_BinOp(self, node):
        """ +, -, * 등의 연산을 감지하여 함수 호출 삽입 """
        line_number = node.lineno  # 연산이 발생한 줄 번호
        new_node = ast.Call(
            func=ast.Name(id="log_operator", ctx=ast.Load()),  # log_operator 함수 호출
            args=[
                self.visit(node.left),  # 왼쪽 피연산자 먼저 방문 (재귀적으로 변환)
                self.visit(node.right),  # 오른쪽 피연산자 방문
                ast.Constant(value=type(node.op).__name__),  # 연산자 타입 (예: Add)
                ast.Constant(value=line_number)  # 발생한 코드 줄 번호
            ],
            keywords=[]
        )
        return new_node

    def visit_Constant(self, node):
        """ 숫자가 참조될 때 함수 호출을 삽입 """
        return self.wrap_with_log(node)

    def wrap_with_log(self, node):
        """ 숫자 객체의 전체 메모리 크기와 실제 원본 숫자의 메모리 주소, 크기를 포함하여 로그 출력 """
        return ast.Call(
            func=ast.Name(id="log_number", ctx=ast.Load()),  # log_number 함수 호출
            args=[
                node,  # 원래 숫자 (ex: 5)
                ast.Call(func=ast.Name(id="id", ctx=ast.Load()), args=[node], keywords=[]),  # 객체의 메모리 주소
                ast.Call(func=ast.Name(id="type", ctx=ast.Load()), args=[node], keywords=[]),  # 객체의 타입
                ast.Call(
                    func=ast.Attribute(value=ast.Name(id="sys", ctx=ast.Load()), attr="getsizeof", ctx=ast.Load()),
                    args=[node],
                    keywords=[]
                ),  # sys.getsizeof(node) -> 객체 의 크기

                # `ctypes`를 사용하여 숫자 객체 내부의 실제 데이터 주소 및 크기 추출
                ast.Call(
                    func=ast.Name(id="get_raw_integer_info", ctx=ast.Load()),  # ctypes 활용한 정보 획득
                    args=[node],
                    keywords=[]
                ),

                # 객체 전체 크기 (pympler asizeof 사용)
                ast.Call(
                    func=ast.Attribute(value=ast.Name(id="asizeof", ctx=ast.Load()), attr="asizeof", ctx=ast.Load()),
                    args=[node],  # 전체 객체 크기
                    keywords=[]
                ),

                ast.Constant(value=node.lineno)  # 발생한 코드 줄 번호
            ],
            keywords=[]
        )