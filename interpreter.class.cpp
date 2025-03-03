#include <iostream>
#include "Interpreter.class.h"
#include "./src/lexical-analyzer/lexical-analyzer.class.h"
#include "./src/syntax-analyzer/syntax-analyzer.class.h"
#include "./src/semantic-analyzer/semantic-analyzer.class.h"

Interpreter::Interpreter() {
    std::cout << "Interpreter class connected to main \n" << std::endl;
    std::cout << "==== INTERPRETER.CPP ====" << std::endl;
    LexicalAnalyzer lexicalAnalyzer;
    lexicalAnalyzer.sayHello();
    SyntaxAnalyzer syntaxAnalyzer;
    syntaxAnalyzer.sayHello();
    SemanticAnalyzer semanticAnalyzer ;
    semanticAnalyzer.sayHello();
    std::cout << "==== INTERPRETER.CPP OVER ====" << std::endl;
}

void Interpreter::sayHello() {
    std::cout << "Hello from Interpreter!" << std::endl;
}
