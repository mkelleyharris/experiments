// A listening fake/stub implementing the TemperatureDisplay interface. For test.

#ifndef TEMPERATURE_DISPLAY_FAKE_HPP
#define TEMPERATURE_DISPLAY_FAKE_HPP

#include "./TemperatureDisplay.hpp"

class TemperatureDisplayFake : public TemperatureDisplay
{
public:
	void SetStatus(TemperatureStatus::Status status)
	{
		this->status = status;
	}
	
	void SetTemp(double temp)
	{	
		this->temp = temp;	
	}
	
	TemperatureStatus::Status GetStatus()
	{
		return status;
	}
	
	double GetDisplayedTemperature()
	{
		return temp;	
	}		

private:
	TemperatureStatus::Status status;
	double temp;
};

#endif //TEMPERATURE_DISPLAY_FAKE_HPP