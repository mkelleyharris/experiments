//
//  StrategyTest.cpp
//  
//
//  Created by Michael Kelley Harris on 5/26/13.
//
//

#include "../../patterns/Patterns/Strategy.h"  // TODO add path to Patterns in project settings.


#define BOOST_TEST_MODULE StrategyTest
#include <boost/test/included/unit_test.hpp>

BOOST_AUTO_TEST_SUITE( patterns_test_suite )


BOOST_AUTO_TEST_CASE( test_strategyAdd )
{
    Add add;
    Context context(&add);
    BOOST_CHECK_EQUAL(context.execute(1, 2), 3);
    BOOST_CHECK_EQUAL(context.execute(3, 5), 8);
}

BOOST_AUTO_TEST_CASE( test_strategySubtract )
{
    Subtract subtract;
    Context context(&subtract);
    BOOST_CHECK_EQUAL(context.execute(1, 2), -1);
    BOOST_CHECK_EQUAL(context.execute(3, 5), -2);
    BOOST_CHECK_EQUAL(context.execute(3, 1), 2);
}

BOOST_AUTO_TEST_SUITE_END()
