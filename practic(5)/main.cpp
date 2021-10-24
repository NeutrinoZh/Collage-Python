#include <iostream>

int foo(int a, int b) {
    return a + b;
}

int main() {
    std::cout << foo(7, 8) << std::endl;
    return EXIT_SUCCESS;
}