#ifndef LEXICAL_ANALYZER_H
#define LEXICAL_ANALYZER_H

#include <iostream>
#include <vector>
#include <string>

class LexicalAnalyzer {
public:
    LexicalAnalyzer();
    std::vector<std::vector<char>> sourceCode;
    void run();

};

#endif // LEXICAL_ANALYZER_H
