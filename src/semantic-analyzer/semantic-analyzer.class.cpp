#include <iostream>
#include "semantic-analyzer.class.h"

SemanticAnalyzer::SemanticAnalyzer() {
    std::cout << "semanticAnalyzer class connected to interpreter" << std::endl;
}

void SemanticAnalyzer::sayHello() {
    std::cout << "Hello from semanticAnalyzer!\n" << std::endl;
}
