#include <iostream>
#include <sstream>
#include <string>
#include "lexical-analyzer.class.h"
#include "./Scanner/scanner.class.h"


LexicalAnalyzer::LexicalAnalyzer() {
    std::cout << "==== LEXICAL_ANALYZER.CPP ====" << std::endl;
}

void LexicalAnalyzer::run() {

    Scanner scanner;
    this -> sourceCode = scanner.run();

    // 2차원 배열(벡터) 내용 확인
    std::cout << "===== SCANNER_CONVERT_RESULT (2D array) =====" << std::endl;
    for (size_t i = 0; i < sourceCode.size(); ++i) {
        std::cout << "Line " << i << ":" << std::endl;
        for (size_t j = 0; j < sourceCode[i].size(); ++j) {
            std::cout << "  [" << j << "] " << sourceCode[i][j] << std::endl;
        }
        std::cout << std::endl;
    }
    //이제 sourceCode 를 사용할 STEP 2 개발.
    std::cout << "==== LEXICAL_ANALYZER.CPP OVER ====" << std::endl;
}
