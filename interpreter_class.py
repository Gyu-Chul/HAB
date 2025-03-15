from lexical_analyzer.lexicalAnalyzer_class import LexicalAnalyzer
from syntax_analyzer.syntaxAnalyzer_class import SyntaxAnalyzer
from semantic_analyzer.semanticAnalyzer_class import SemanticAnalyzer

class Interpreter:
    
    def __init__(self):
        print("Interpreter class created in hab.py\n")

    def run(self):
        print("==== INTERPRETER.PY ====")
        lexicalAnalyzer = LexicalAnalyzer()
        syntaxAnalyzer = SyntaxAnalyzer()
        semanticAnalyzer = SemanticAnalyzer()
        lexicalAnalyzer.run()
        for token in lexicalAnalyzer.tokens:
            print(f"Type: {token['type']}, String: {repr(token['string'])}, Start: {token['start']}, End: {token['end']}")
        syntaxAnalyzer.run()
        semanticAnalyzer.run()
        print("==== INTERPRETER.PY OVER ====")