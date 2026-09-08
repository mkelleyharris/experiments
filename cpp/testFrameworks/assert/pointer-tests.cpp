
// pointer-tests

// compile: clang++ pointer-tests.cpp -o ptest
// compile and run: clang++ pointer-tests.cpp -o ptest && ./ptest
// run:  ./ptest


#include <iostream>
#include <assert.h>


int main() {


    std::cout << "pointer-tests using simple assert function. " << std::endl;  


    {
        int arr[] = {10, 20, 30};
        int* p = arr;
        assert( *p == 10 );  //Dereferences p with * accesses first a array element. index 1
    }

    {
        int arr[] = {10, 20, 30};
        int* p = arr;

        assert( *p + 1 == 11 );  //Dereferencing p with * accesses first array element.
                    // adds 1 to it yielding 11 in a temp context
        assert( arr[0] == 10 );  // arr index is 0 arr[0] and it's value does not change
                    // predence on the * as if (*p) + 1
    }

    {
        int arr[] = {10, 20, 30};
        int* p = arr;
        assert( ++*p == 11 ); //precedence equal. Eval right to left
        assert( arr[0] == 11 ); // array chqnge 10 to 11
    }

    {
        int arr[] = {10, 20, 30};
        int* p = arr;;

        assert( *p++ == 10); //precedence ++ Eval right to left *(p++)
        assert( *p == 20 ); 
    }

    {
        int arr[] = {10, 20, 30};
        int* p = arr;
        int** q = &p;

        assert( *q == p ); 
        assert( **q == 10 ); 
    }


    std::cout << "pointer-tests all passed no asserts fired" << std::endl; 
    return 0;
}