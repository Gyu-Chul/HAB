#include <iostream> 
#include "interpreter.class.h"


int main() {
    std::cout << "==== MAIN . CPP ====" << std::endl;
    Interpreter interpreter;
    interpreter.sayHello();

    std::cout << "Press Enter to exit...";
    std::cin.get(); // 엔터 입력 대기
    return 0;
}


