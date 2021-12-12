#include "package2/lib.h"

#include <iostream>
#include "package1/lib.h"

namespace pkg2
{
    void func1()
    {
        std::cout << "pkg2::func1()\n";
        pkg1::func1();
    }
    
    void func2()
    {
        std::cout << "pkg2::func2()\n";
        pkg1::func2();
    }
}