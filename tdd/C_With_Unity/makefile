

TARGET=TestRunner
#INCLUDES= Geometry.h

SOURCES= $(wildcard src/*.c) $(wildcard test/*.c)

INCLUDE_PATH= src
	
tests: $(SOURCES) $< $(INCLUDES)
	gcc $(SOURCES) -o tests -I $(INCLUDE_PATH) 
	
clean:
	rm $(TARGET)
	
test: tests
	./test/$(TARGET)