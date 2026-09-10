
// pointer-tests
// using a "unity build" for speed (including .cpp files, no .h files, ...)
//
// compile: clang++ -std=c++20 -Wall -Wextra amain-runner.cpp -o ptest
// compile and run: clang++ -std=c++20 -Wall -Wextra main-runner.cpp -o ptest && ./ptest
// run:  ./ptest


#ifndef MAIN_RUNNER_CPP
#define MAIN_RUNNER_CPP



#include <iostream>
#include "pointer-tests.cpp"
int main() {

    std::cout << "main-runner tests using simple assert function." << std::endl;  

    testSuitePointers();

    std::cout << "main-runner tests. No asserts fired.  SUCCESS" << std::endl;  

    return 0;
}

#endif // MAIN_RUNNER_CPP

