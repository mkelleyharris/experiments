TODO use smart ptrs, finish readme, adjust file structure and names.

TemperatureMonitor is a demo project to show how to how to make our business logic more testable, and extendable.

In this demo, the main business logic is the TemperatorMonitor class.
Conceptually it depends on a temperature sensor and a temperature display.
But this demo uses the S.O.L.I.D. object-oriented design principles
and has the business logic depending on abstract interfaces (the "Dependency Inversion" principle), so that we can better unit test the logic, and to allow extending our system with different sensors and displays without modifying the business logic. (The "Open-Closed Principle") 