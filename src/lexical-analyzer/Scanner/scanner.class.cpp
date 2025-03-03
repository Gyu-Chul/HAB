#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "scanner.class.h"

Scanner::Scanner() {
    std::cout << "==== SCANNER.CPP ====" << std::endl;
}

std::vector<std::vector<char>> Scanner::run() {
    std::ifstream file("../../script.py");
    if (!file) {
        std::cerr << "can't open the script.py" << std::endl;
        std::cin.get(); // 엔터 입력 대기
        return {}; // 빈 벡터 반환
    }
    
    // 파일 전체를 읽어들이기 위한 스트림 버퍼 사용
    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string pythonCode = buffer.str();
    
    // 파일 내용 출력 (확인용)
    std::cout << pythonCode << std::endl;

    // 2차원 배열(벡터) 생성: 각 줄을 문자 단위로 분리
    std::vector<std::vector<char>> sourceCode;
    {
        std::istringstream iss(pythonCode);
        std::string line;
        while (std::getline(iss, line)) {
            // 한 줄을 읽어서, 그 줄의 모든 문자를 vector<char>에 담기
            std::vector<char> lineChars(line.begin(), line.end());
            sourceCode.push_back(lineChars);
        }
    }
    
    // 2차원 배열(벡터) 내용 확인
    std::cout << "===== SCANNER_CONVERT_RESULT (2D array) =====" << std::endl;
    for (size_t i = 0; i < sourceCode.size(); ++i) {
        std::cout << "Line " << i << ":" << std::endl;
        for (size_t j = 0; j < sourceCode[i].size(); ++j) {
            std::cout << "  [" << j << "] " << sourceCode[i][j] << std::endl;
        }
        std::cout << std::endl;
    }
    std::cout << "==== SCANNER.CPP OVER ====\n" << std::endl;

    return sourceCode;
}
