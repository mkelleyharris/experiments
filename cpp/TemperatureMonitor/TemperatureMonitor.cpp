// Monitor's temperature and displays status

#include "./TemperatureSensor.hpp"
#include "./TemperatureDisplay.hpp"
#include "./TemperatureMonitor.hpp"
#include "./TemperatureStatus.hpp"

#include <exception>

const double LOW_TEMP_ALERT_HIGH = 0.0;
const double TEMP_NORMAL_LOW = 0.0;
const double TEMP_NORMAL_HIGH = 100.0;
const double TEMP_WARNING_LOW = 100.0;
const double TEMP_WARNING_HIGH = 200.0;
const double HIGH_TEMP_ALERT_LOW = 200.0;

	
TemperatureMonitor::TemperatureMonitor(SENSOR_PTR sensor, DISPLAY_PTR display)
: sensor(sensor), display(display), latestTemperature(TEMPERATURE_NOT_SET), 
  latestStatus(TemperatureStatus::NOTSET)
{	
	PreconditionCheckOfObjectsPassedIn(sensor, display);
}

void TemperatureMonitor::PreconditionCheckOfObjectsPassedIn(SENSOR_PTR sensor, DISPLAY_PTR display)
{
	if ( !sensor)
	{
		throw "Sensor was null";
	}
	
	if ( !display)
	{
		throw "Display was null";
	}	
}

void TemperatureMonitor::DoMeasurement()
{
	MeasureSensorTemperature();
	DetermineStatus();
	UpdateDisplay();
}
	
void TemperatureMonitor::UpdateDisplay()
{
	display->SetStatus(latestStatus);				
}
	
void TemperatureMonitor::MeasureSensorTemperature()
{
	latestTemperature = sensor->GetValue();
}
	
void TemperatureMonitor::DetermineStatus()
{
	TemperatureStatus::Status status = TemperatureStatus::NOTSET;
		
	if ( (latestTemperature >= TEMP_NORMAL_LOW) && ( latestTemperature < TEMP_NORMAL_HIGH))
	{
		status = TemperatureStatus::NORMAL;	
	}
	else if ( (latestTemperature >= TEMP_WARNING_LOW) && (latestTemperature < TEMP_WARNING_HIGH) )
	{
		status = TemperatureStatus::WARNING;					
	}
	else if ( (latestTemperature >= HIGH_TEMP_ALERT_LOW))
	{
		status = TemperatureStatus::ALERT_HI;					
	}
	else if ( (latestTemperature < LOW_TEMP_ALERT_HIGH))
	{
		status = TemperatureStatus::ALERT_LOW;					
	}
	else // Default case. Should not get here.
	{
		status = TemperatureStatus::ERROR;
	}
		
	latestStatus = status;			
}
