// Monitor temperatures from a sensor and display status on a separate display

#ifndef TEMPTERATURE_MONITOR_HPP
#define TEMPTERATURE_MONITOR_HPP

#include "./TemperatureStatus.hpp"

#include <tr1/memory>

class TemperatureSensor;
class TemperatureDisplay;

typedef std::tr1::shared_ptr<TemperatureSensor> SENSOR_PTR;
typedef std::tr1::shared_ptr<TemperatureDisplay> DISPLAY_PTR;

class TemperatureMonitor
{
public:
	TemperatureMonitor(SENSOR_PTR sensor, DISPLAY_PTR display);	
	void DoMeasurement();	
	
private:	
	void UpdateDisplay();	
	void MeasureSensorTemperature();	
	void DetermineStatus();
	
	void PreconditionCheckOfObjectsPassedIn(SENSOR_PTR sensor, DISPLAY_PTR display);
	
	SENSOR_PTR sensor;
	DISPLAY_PTR display;
	TemperatureStatus::Status latestStatus;
	double latestTemperature;
};

	
#endif //TEMPTERATURE_MONITOR_HPP
