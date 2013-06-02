#include "../src/a.hpp"

BOOST_AUTO_TEST_CASE( test_A_Add )
{
    A a;
	BOOST_CHECK_EQUAL(a.add(1, 2), 3);
    BOOST_CHECK_EQUAL(a.add(1, 4), 5);
}


