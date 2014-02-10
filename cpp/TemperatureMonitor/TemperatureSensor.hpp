// Interface for all Temperature Sensors

#ifndef TEMPERATURE_SENSOR_HPP
#define TEMPERATURE_SENSOR_HPP
	
class TemperatureSensor
{
public:
	virtual double GetValue() = 0;
};

#endif //TEMPERATURE_SENSOR_HPP