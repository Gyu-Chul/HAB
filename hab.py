import sys
import os

sys.path.append(os.path.abspath("src"))
from dotenv import load_dotenv

import interpreter_class
import graphicInterface_class

# 실행 파일(.exe) 필요 --> 환경변수 세팅 하고 hab 파일 실행
def hab():
    
    print(" ==== MAIN FUNCTION ====")
    print(os.environ["DEBUG"])

    interpreter = interpreter_class.Interpreter()
    interpreter.run()


    #graphicInterface = GraphicInterface()


    print("==== MAIN.PY OVER ====")
    input("Press Enter to exit...")



if __name__ == "__main__":
    hab()