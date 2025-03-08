#include <iostream>
#include "graphicInterface.class.h"
#include "./src/code-editor/code-editor.class.h"
#include "./src/datas/datas.class.h"
#include "./src/graphic-maker/graphic-maker.class.h"
#include "./src/graphic-utility/graphic-utility.class.h"
#include "./src/runtime/runtime.class.h"
#include "./src/window/window.class.h"

GraphicInterface::GraphicInterface() {
    std::cout << "\n\n\nGraphicInterface class connected to main \n" << std::endl;
    std::cout << "==== GRAPHIC_INTERFACE.CPP ====" << std::endl;
    CodeEditor codeEditor;
    codeEditor.sayHello();
    Datas datas;
    datas.sayHello();
    GraphicMaker graphicMaker;
    graphicMaker.sayHello();
    GraphicUtility graphicUtility;
    graphicUtility.sayHello();
    Runtime runtime;
    runtime.sayHello();
    Window window;
    window.sayHello();
    std::cout << "==== GRAPHIC_INTERFACE.CPP OVER ====\n\n" << std::endl;
}

void GraphicInterface::sayHello() {
    std::cout << "Hello from GRAPHIC_INTERFACE!" << std::endl;
}
