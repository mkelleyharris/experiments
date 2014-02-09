
#ifndef TEMPERATURE_STATUS_HPP
#define TEMPERATURE_STATUS_HPP

namespace TemperatureStatus
{

enum Status
{
	NOTSET = 0,
	ALERT_LOW,
	NORMAL,
	WARNING,
	ALERT_HI,
	ERROR
};

} // namespace TemperatureStatus

const double TEMPERATURE_NOT_SET = -9999.0;


#endif //TEMPERATURE_STATUS_HPP