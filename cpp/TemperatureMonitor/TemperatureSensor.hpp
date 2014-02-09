// Interface for all Temperature Sensors

#ifndef TEMPERATURE_SENSOR_HPP
#define TEMPERATURE_SENSOR_HPP
	
class TemperatureSensor
{
public:
	virtual double GetValue() = 0;
};

class TemperatureSensorFake : public TemperatureSensor
{
public:
	TemperatureSensorFake(double temp = -9999.0)
	: temp(temp)
	{	
	}
	
	double GetValue()
	{
		return temp;
	}
	
private:
	double temp;
};


#endif //TEMPERATURE_SENSOR_HPP