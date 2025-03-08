#ifndef SCANNER_H
#define SCANNER_H

#include <vector>
#include <string>

class Scanner {
public:
    Scanner();
    std::vector<std::vector<char>> run(const std::string &pythonCode);
};

#endif // SCANNER_H
