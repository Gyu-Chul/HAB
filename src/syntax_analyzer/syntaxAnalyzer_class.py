import ast
class SyntaxAnalyzer:

    def __init__(self,filePath):
        self.filePath = filePath
        self.astTree = None
        print("SyntaxAnalyzer class created in Interpreter.py\n")

    def run(self):
        print("==== SYNTAX_ANALYZER.PY ====")

        with open(self.filePath, "r", encoding="utf-8") as f:
            sourceCode = f.read()

        self.astTree = ast.parse(sourceCode)

        return self.astTree
        print("==== SYNTAX_ANALYZER.PY OVER ====")

    def print_ast_tree(self):
        print(ast.dump(self.astTree, indent=4))  # 보기 좋게 출력
