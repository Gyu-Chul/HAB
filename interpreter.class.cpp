#include <iostream>
#include "Interpreter.class.h"

Interpreter::Interpreter() {
    std::cout << "Interpreter class connected" << std::endl;
}

void Interpreter::sayHello() {
    std::cout << "Hello from Interpreter!" << std::endl;
}
