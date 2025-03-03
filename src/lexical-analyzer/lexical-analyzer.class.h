#ifndef LEXICAL_ANALYZER_H
#define LEXICAL_ANALYZER_H

#include <iostream>
#include <vector>
#include <string>

class LexicalAnalyzer {
public:
    LexicalAnalyzer();
    void sayHello();

private:
    std::vector<std::vector<char>> sourceCode;
};

#endif // LEXICAL_ANALYZER_H
