#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "lexical-analyzer.class.h"

LexicalAnalyzer::LexicalAnalyzer() {
    std::cout << "==== LexicalAnalyzer.CPP ====" << std::endl;

    std::ifstream file("../../script.py");
    if (!file) {
        std::cerr << "can't open the script.py" << std::endl;
        std::cin.get(); // 엔터 입력 대기
        return;
    }
    
    // 파일 전체를 읽어들이기 위한 스트림 버퍼 사용
    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string sourceCode = buffer.str();
    
    // 파일 내용 출력 (확인용)
    std::cout << sourceCode << std::endl;


    std::vector<std::vector<char>> lines;  // 2차원 배열(벡터)
    {
        std::istringstream iss(sourceCode);
        std::string line;
        while (std::getline(iss, line)) {
            // 한 줄을 읽어서, 그 줄의 모든 문자를 vector<char>에 담기
            std::vector<char> lineChars(line.begin(), line.end());
            lines.push_back(lineChars);
        }
    }
    
    // 2차원 배열(벡터) 내용 확인
    std::cout << "===== lines (2D array) =====" << std::endl;
    for (size_t i = 0; i < lines.size(); ++i) {
        std::cout << "Line " << i << ":" << std::endl;
        for (size_t j = 0; j < lines[i].size(); ++j) {
            // 각 문자를 별도의 줄에 출력
            std::cout << "  [" << j << "] " << lines[i][j] << std::endl;
        }
        std::cout << std::endl; // 줄 하나가 끝난 뒤 구분을 위해 추가
    }
    std::cout << std::endl;
}

void LexicalAnalyzer::sayHello() {
    std::cout << "Hello from lexicalAnalyzer!\n" << std::endl;

    std::cout << "==== LexicalAnalyzer.CPP OVER ====" << std::endl;
}
