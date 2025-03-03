#include <iostream>
#include "lexical-analyzer.class.h"

LexicalAnalyzer::LexicalAnalyzer() {
    std::cout << "lexicalAnalyzer class connected to interpreter" << std::endl;
}

void LexicalAnalyzer::sayHello() {
    std::cout << "Hello from lexicalAnalyzer!\n" << std::endl;
}
