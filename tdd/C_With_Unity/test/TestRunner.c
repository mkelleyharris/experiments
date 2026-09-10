#include "Unity.h"

static void runAllTests()
{
	TEST_GROUP(Geometry)	
}

int main(int argc, char* argv[])
{
	UnityMain(argc, argv, runAllTests);
	return 0;
}