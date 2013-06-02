
#include "a.hpp"
#include "b.hpp"

#include "iostream"

int main()
{
	std::cout << "simple running" << std::endl;
	
	A a;
	std::cout << "a.add(1, 4): " << a.add(1, 4) << std::endl;
	
	B b;
	std::cout << "b.subtract(1, 4): " << b.subtract(1, 4) << std::endl;
	
	std::cout << "simple end" << std::endl;

}