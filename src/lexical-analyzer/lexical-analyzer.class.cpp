#include <iostream>
#include "lexical-analyzer.class.h"

LexicalAnalyzer::LexicalAnalyzer() {
    std::cout << "lexicalAnalyzer class connected to interpreter \n" << std::endl;
}

void LexicalAnalyzer::sayHello() {
    std::cout << "Hello from lexicalAnalyzer!" << std::endl;
}
