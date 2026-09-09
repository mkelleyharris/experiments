
// pointer-tests.cpp

// See main-runner.cpp for build information


#include <iostream>
#include <assert.h>


void testDereferencingPoineterToArray() {
    int arr[] = {10, 20, 30};
    int* p = arr;
    assert( *p == 10 );  //Dereferences p with * accesses first a array element. index 1
}

void testMixOfRefereningAddOne() {
    int arr[] = {10, 20, 30};
    int* p = arr;

    assert( *p + 1 == 11 );  //Dereferencing p with * accesses first array element.
                // adds 1 to it yielding 11 in a temp context
    assert( arr[0] == 10 );  // arr index is 0 arr[0] and it's value does not change
                // precedence on the * as if (*p) + 1
}

void testIncrementingValue() {
    int arr[] = {10, 20, 30};
    int* p = arr;
    assert( ++*p == 11 ); //precedence equal. Eval right to left
    assert( arr[0] == 11 ); // array chqnge 10 to 11
}

void testMixOfRefereningAndIncrerment() {
    int arr[] = {10, 20, 30};
    int* p = arr;;

    assert( *p++ == 10); //precedence ++ Eval right to left *(p++)
    assert( *p == 20 ); 
}

void testMixOfPreceddence() {
    int arr[] = {10, 20, 30};
    int* p = arr;
    int** q = &p;

    assert( *q == p ); 
    assert( **q == 10 ); 
}


void testSuitePointers() {
    testDereferencingPoineterToArray();
    testMixOfRefereningAddOne();
    testIncrementingValue();
    testMixOfRefereningAndIncrerment();
    testMixOfPreceddence();
}
