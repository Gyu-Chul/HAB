#include <iostream>
#include "Interpreter.class.h"
#include "./src/lexical-analyzer/lexical-analyzer.class.h"
#include "./src/syntax-analyzer/syntax-analyzer.class.h"


Interpreter::Interpreter() {
    std::cout << "==== INTERPRETER.CPP ====" << std::endl;
    std::cout << "Interpreter class connected to main \n" << std::endl;
    LexicalAnalyzer lexicalAnalyzer;
    lexicalAnalyzer.sayHello();
    SyntaxAnalyzer syntaxAnalyzer;
    syntaxAnalyzer.sayHello();
}

void Interpreter::sayHello() {
    std::cout << "Hello from Interpreter!" << std::endl;
}
