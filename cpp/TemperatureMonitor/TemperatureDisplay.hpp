// Temperature Display abstract interface

#ifndef TEMPERATURE_DISPLAY_HPP
#define TEMPERATURE_DISPLAY_HPP

#include "./TemperatureStatus.hpp"

	
class TemperatureDisplay
{
public:	
	virtual void SetStatus(TemperatureStatus::Status status) = 0;
	virtual void SetTemp(double temp) = 0;
};


#endif //TEMPERATURE_DISPLAY_HPP