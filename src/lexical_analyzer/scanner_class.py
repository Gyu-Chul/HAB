import os
class Scanner:

    def __init__(self):
        print("Scanner class created in lexicalAnalyzer.py\n")


    def run(self):
        print("==== SCANNER.PY ====")
        # STEP 1: .py 파일 읽기
        base_dir = os.path.abspath(os.path.join(__file__, "../../.."))
        file_path = os.path.join(base_dir, "script.py")

        if not os.path.isfile(file_path):
            print(f"[ERROR] 파일이 존재하지 않습니다: {file_path}")
            return []  # 빈 리스트 반환


        print("==== SCANNER.PY OVER ====\n")

        return file_path
