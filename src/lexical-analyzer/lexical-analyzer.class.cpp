#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include "lexical-analyzer.class.h"
#include "./Scanner/scanner.class.h"


LexicalAnalyzer::LexicalAnalyzer() {
    std::cout << "==== LEXICAL_ANALYZER.CPP ====" << std::endl;

    //STEP 1 .py 파일 읽기
    std::ifstream file("../../script.py");
    if (!file) {
        std::cerr << "can't open the script.py" << std::endl;
        std::cin.get(); // 엔터 입력 대기
        return ; // 빈 벡터 반환
    }

     // 파일 전체를 읽어들이기 위한 스트림 버퍼 사용
    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string pythonCode = buffer.str();

    Scanner scanner;
    sourceCode = scanner.run(pythonCode);

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
}

void LexicalAnalyzer::sayHello() {
    std::cout << "==== LEXICAL_ANALYZER.CPP OVER ====" << std::endl;
}
