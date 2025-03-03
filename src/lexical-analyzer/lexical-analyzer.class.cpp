#include <iostream>
#include "lexical-analyzer.class.h"

LexicalAnalyzer::LexicalAnalyzer() {
    std::cout << "==== LEXICAL_ANALYZER.CPP ====" << std::endl;
    std::cout << "lexicalAnalyzer class connected to interpreter" << std::endl;
}

void LexicalAnalyzer::sayHello() {
    std::cout << "Hello from lexicalAnalyzer!" << std::endl;
}
