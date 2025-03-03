#include <iostream>

#include "lexical-analyzer.class.h"
#include "./Scanner/scanner.class.h"


LexicalAnalyzer::LexicalAnalyzer() {
    std::cout << "==== LEXICAL_ANALYZER.CPP ====" << std::endl;
    Scanner scanner;
    sourceCode = scanner.run();
}

void LexicalAnalyzer::sayHello() {
    std::cout << "==== LEXICAL_ANALYZER.CPP OVER ====" << std::endl;
}
