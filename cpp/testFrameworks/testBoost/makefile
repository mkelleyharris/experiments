CC=g++
CFLAGS=-c -Wall
LDFLAGS=
# Add path to your Boost directory
# INCLUDES="/usr/local/boost/boost_1_92_0"
# INCLUDES="/usr/local/boost/boost_1_92_0"
INCLUDES="/usr/local/boost/test/unit_test.hpp>"
SOURCES=runner.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=runner

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) -I $(INCLUDES) $< -o $@

	
clean:
	rm -f $(OBJECTS) $(EXECUTABLE)
	echo "Clean Done"
	
test:
	make all
	./$(EXECUTABLE)