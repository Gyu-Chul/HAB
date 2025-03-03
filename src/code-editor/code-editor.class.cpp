#include <iostream>
#include "code-editor.class.h"

CodeEditor::CodeEditor() {
    std::cout << "CodeEditor class connected to graphicInterface!" << std::endl;
}

void CodeEditor::sayHello() {
    std::cout << "Hello from CodeEditor class!\n" << std::endl;
}
