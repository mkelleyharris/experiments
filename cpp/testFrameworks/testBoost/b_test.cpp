#include "../src/b.hpp"

BOOST_AUTO_TEST_CASE( test_B_Subtract )
{
    B b;
	BOOST_CHECK_EQUAL(b.subtract(1, 2), -1);
    BOOST_CHECK_EQUAL(b.subtract(1, 4), -3);
}
