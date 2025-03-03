#include <iostream>
#include "Interpreter.class.h"
#include "./src/lexical-analyzer/lexical-analyzer.class.h"

Interpreter::Interpreter() {
    std::cout << "==== INTERPRETER.CPP ====" << std::endl;
    std::cout << "Interpreter class connected to main" << std::endl;
    LexicalAnalyzer lexicalAnalyzer;
    lexicalAnalyzer.sayHello();
}

void Interpreter::sayHello() {
    std::cout << "Hello from Interpreter!" << std::endl;
}
