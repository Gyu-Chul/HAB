#include <iostream>
#include "window.class.h"

Window::Window() {
    std::cout << "window class connected to interpreter" << std::endl;
}

void Window::sayHello() {
    std::cout << "Hello from window class!\n" << std::endl;
}
