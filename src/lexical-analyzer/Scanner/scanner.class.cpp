#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include "scanner.class.h"

Scanner::Scanner() {
    std::cout << "==== SCANNER.CPP ====" << std::endl;
}

std::vector<std::vector<char>> Scanner::run() {

    //STEP 1 .py 파일 읽기
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
    std::vector<std::vector<char>> sourceCode; //--> 스캐너의 속성으로 변경 필요 
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
