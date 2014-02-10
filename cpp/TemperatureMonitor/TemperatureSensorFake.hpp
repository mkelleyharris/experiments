// A fake/stub implementing the TemperatureSensor interface. For test.

#ifndef TEMPERATURE_SENSOR_FAKE_HPP
#define TEMPERATURE_SENSOR_FAKE_HPP

#include "./TemperatureSensor.hpp"

class TemperatureSensorFake : public TemperatureSensor
{
public:
	TemperatureSensorFake(double temp = -9999.0)
	: temp(temp)
	{}
	
	double GetValue()
	{
		return temp;
	}
	
private:
	double temp;
};

#endif //TEMPERATURE_SENSOR_FAKE_HPP