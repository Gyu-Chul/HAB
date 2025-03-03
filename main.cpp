#include <iostream> 
#include "interpreter.class.h"
#include "graphicInterface.class.h"


int main() {
    std::cout << "==== MAIN.CPP ====" << std::endl;
    Interpreter interpreter;
    GraphicInterface GraphicInterface;

    std::cout << "==== MAIN.CPP OVER ====";
    std::cin.get(); // 엔터 입력 대기
    return 0;
}


