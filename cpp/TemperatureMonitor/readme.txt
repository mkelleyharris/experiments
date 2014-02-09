TemperatureMonitor: A C++ demo of some S.O.L.I.D. object-oriented design Principles.  
Michael Kelley Harris kelley@kelleyharris.com

TemperatureMonitor is a demo project to show how to make our business logic more testable, and extendable. The monitor uses a sensor object and a display object, both via abstract interfaces.

In this demo, the main business logic is the TemperatorMonitor class.
Conceptually it depends on a temperature sensor and a temperature display.
But this demo uses the S.O.L.I.D. object-oriented design principles.
It has the business logic depending on abstract interfaces (the "Dependency Inversion" principle), so that we can better unit test the key business logic, and enable us to extend our system, with different sensors and displays, without modifying the business logic. (The "Open-Closed Principle") 

The method "void TemperatureMonitor::DoMeasurement()" is an example of the ComposedMethod pattern, 
in which it reads easily at the same level of abstraction.

This demo uses shared_ptr's, to insure memory clean up, less the risk for null pointers.

The unit tests are written in the BOOST_TEST framework. However, they can be easily ported to 
any other test framework. (I've used 14+ C++ test frameworks, and found them to be more similar than different.
we spend most of our time get the logic right. The syntax is quick to change.)
