from lexical_analyzer.lexicalAnalyzer_class import LexicalAnalyzer
from syntax_analyzer.syntaxAnalyzer_class import SyntaxAnalyzer
from semantic_analyzer.semanticAnalyzer_class import SemanticAnalyzer
import os
class Interpreter:
    
    def __init__(self):
        print("Interpreter class created in hab.py\n")

    def run(self):
        print("==== INTERPRETER.PY ====")
        base_dir = os.path.abspath(os.path.join(__file__, "../"))
        file_path = os.path.join(base_dir, "script.py")

        if not os.path.isfile(file_path):
            print(f"[ERROR] 파일이 존재하지 않습니다: {file_path}")
            raise "FileNotExist"

        lexicalAnalyzer = LexicalAnalyzer(file_path)
        syntaxAnalyzer = SyntaxAnalyzer()
        semanticAnalyzer = SemanticAnalyzer()
        lexicalAnalyzer.run()
        for token in lexicalAnalyzer.tokens:
            print(f"Type: {token['type']}, String: {repr(token['string'])}, Start: {token['start']}, End: {token['end']}")


        syntaxAnalyzer.run()
        semanticAnalyzer.run()
        print("==== INTERPRETER.PY OVER ====")