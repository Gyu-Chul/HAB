from .scanner_class import Scanner
import tokenize
from io import BytesIO
class LexicalAnalyzer:

    def __init__(self):
        self.tokens = []
        print("LexicalAnalyzer class created in Interpreter.py\n")
    def run(self):
        print("==== LEXICAL_ANALYZER.PY ====")
        scanner = Scanner()
        file_path = scanner.run()

        with open(file_path, "rb") as f:
            tokens = tokenize.tokenize(f.readline)


            self.tokens = [
                {
                    "type": tokenize.tok_name[token.type],  # 토큰 타입
                    "string": token.string,  # 실제 값
                    "start": token.start,  # (줄 번호, 컬럼 번호)
                    "end": token.end,  # (줄 번호, 컬럼 번호)
                }
                for token in tokens  # 모든 토큰 유지
            ]

        print("==== LEXICAL_ANALYZER.PY OVER ====")
        return tokens
