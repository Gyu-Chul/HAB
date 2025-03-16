import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.abspath("src"))

import interpreter_class
import graphicInterface_class

# 실행 파일(.exe) 필요 --> 환경변수 세팅 하고 hab 파일 실행
def hab():
    
    print(" ==== HAB START ====")

    interpreter = interpreter_class.Interpreter()
    interpreter.run()


    graphicInterface = graphicInterface_class.GraphicInterface()
    graphicInterface.run()

    print("==== HAB END ====")



if __name__ == "__main__":
    hab()