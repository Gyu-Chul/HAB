import os
from dotenv import load_dotenv

import interpreter_class
import graphicInterface_class


def main():
    
    print(" ==== MAIN FUNCTION ====")
    print(os.environ["DEBUG"])

    interpreter = interpreter_class.Interpreter()
    interpreter.sayHello()


    #graphicInterface = GraphicInterface()


    print("==== MAIN.PY OVER ====")
    input("Press Enter to exit...")



if __name__ == "__main__":
    main()