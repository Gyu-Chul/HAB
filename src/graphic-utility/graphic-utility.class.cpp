#include <iostream>
#include "graphic-utility.class.h"

GraphicUtility::GraphicUtility() {
    std::cout << "GraphicUtility class connected to graphicInterface!" << std::endl;
}

void GraphicUtility::sayHello() {
    std::cout << "Hello from GraphicUtility class!\n" << std::endl;
}
