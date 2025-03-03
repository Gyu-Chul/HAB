#include <iostream>
#include "runtime.class.h"

Runtime::Runtime() {
    std::cout << "Runtime class connected to graphicInterface!" << std::endl;
}

void Runtime::sayHello() {
    std::cout << "Hello from Runtime class!\n" << std::endl;
}
