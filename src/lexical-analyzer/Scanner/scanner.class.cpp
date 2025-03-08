#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include "scanner.class.h"

Scanner::Scanner() {
    std::cout << "==== SCANNER.CPP ====" << std::endl;
}

std::vector<std::vector<char>> Scanner::run(const std::string &pythonCode) {
    
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
    
    std::cout << "==== SCANNER.CPP OVER ====\n" << std::endl;

    return sourceCode;
}
