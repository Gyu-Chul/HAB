from lexical_analyzer.lexicalAnalyzer_class import LexicalAnalyzer
from syntax_analyzer.syntaxAnalyzer_class import SyntaxAnalyzer
from semantic_analyzer.semanticAnalyzer_class import SemanticAnalyzer
import os
class Interpreter:
    
    def __init__(self):
        print("Interpreter class created in hab.py\n")

    def run(self):
        print("==== INTERPRETER.PY ====")
        baseDir = os.path.abspath(os.path.join(__file__, "../"))
        filePath = os.path.join(baseDir, "script.py")

        if not os.path.isfile(filePath):
            print(f"[ERROR] 파일이 존재하지 않습니다: {filePath}")
            raise "FileNotExist"

        lexicalAnalyzer = LexicalAnalyzer(filePath)
        syntaxAnalyzer = SyntaxAnalyzer(filePath)
        semanticAnalyzer = SemanticAnalyzer()

        lexicalAnalyzer.run()
        for token in lexicalAnalyzer.tokens:
            print(f"Type: {token['type']}, String: {repr(token['string'])}, Start: {token['start']}, End: {token['end']}")

        syntaxAnalyzer.run()
        syntaxAnalyzer.print_ast_tree()

        semanticAnalyzer.run()
        print("==== INTERPRETER.PY OVER ====")