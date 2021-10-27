#include <iostream>

int foo(int a, int b) {
    if(a>b) {
        for(int i = 0; i <=a; i++)
        {
            std::cout << "{ {hgh}"; 
        }
    }
    return a + b;
}

int main() {
    std::cout << foo(7, 8) << std::endl;
    return EXIT_SUCCESS;
}