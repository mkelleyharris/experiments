# builds TemperatureMonitor tests
# To build and run tests:
# $ make test

INCLUDES= TemperatureMonitor.hpp TemperatureSensor.hpp TemperatureDisplay.hpp TemperatureDisplayFake.hpp TemperatureStatus.hpp

SOURCES= TemperatureMonitorTests.cpp TemperatureMonitor.cpp

INCLUDE_PATH= /usr/local/boost/boost_1_53_0

	
tests: $(SOURCES) $< $(INCLUDES)
	g++ $(SOURCES) -o tests -I $(INCLUDE_PATH) 
	
clean:
	rm tests
	
test: tests
	./tests
	
	
# Command-line alternative:
#g++ TemperatureMonitorTests.cpp TemperatureMonitor.cpp #-o tests #-I/usr/local/boost/boost_1_53_0
# $ ./tests


