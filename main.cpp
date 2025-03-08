#include <iostream>
#include <cstdlib>
#include "interpreter.class.h"
#include "graphicInterface.class.h"


int main() {
    std::cout << "==== MAIN.CPP ====" << std::endl;

    const char* debug = std::getenv("DEBUG");

    if (debug) {
        std::cout << "DEBUG: " << debug << std::endl;
    } else {
        std::cerr << "can't find DEBUG" << std::endl;
    }
    Interpreter interpreter;
    GraphicInterface GraphicInterface;

    std::cout << "==== MAIN.CPP OVER ====";
    std::cin.get(); // 엔터 입력 대기
    return 0;
}