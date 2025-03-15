from lexical_analyzer.lexicalAnalyzer_class import LexicalAnalyzer


class Interpreter:
    
    def __init__(self):
        print("Interpreter class created in main.py\n")


    def run(self):
        print("==== INTERPRETER.PY ====")
        lexicalAnalyzer = LexicalAnalyzer()
        lexicalAnalyzer.run()
        print("==== INTERPRETER.PY OVER ====")