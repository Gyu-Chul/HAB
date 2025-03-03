#include <iostream>
#include "graphic-maker.class.h"

GraphicMaker::GraphicMaker() {
    std::cout << "GraphicMaker class connected to graphicInterface!" << std::endl;
}

void GraphicMaker::sayHello() {
    std::cout << "Hello from GraphicMaker class!\n" << std::endl;
}
