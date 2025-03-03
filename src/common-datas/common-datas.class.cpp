#include <iostream>
#include "common-datas.class.h"

CommonDatas::CommonDatas() {
    std::cout << "CommonDatas class connected to graphicInterface!" << std::endl;
}

void CommonDatas::sayHello() {
    std::cout << "Hello from CommonDatas class!\n" << std::endl;
}
