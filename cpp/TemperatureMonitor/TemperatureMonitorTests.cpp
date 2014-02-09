// Unit tests for TemperatureMonitor


#define BOOST_TEST_MODULE TemperatureMonitorTests
#include <boost/test/included/unit_test.hpp>
//#include </usr/local/boost/boost_1_53_0/boost/test/included/unit_test.hpp>
	
#include "./TemperatureMonitor.hpp"
#include "./TemperatureSensor.hpp"
#include "./TemperatureDisplayFake.hpp" 
#include "./TemperatureStatus.hpp" 

typedef std::tr1::shared_ptr<TemperatureDisplayFake> DISPLAY_FAKE_PTR;

BOOST_AUTO_TEST_SUITE (TemperatureMonitorTests) 
		
BOOST_AUTO_TEST_CASE(DisplayNotSet)
{
	SENSOR_PTR sensor(new TemperatureSensorFake());
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());
	TemperatureMonitor monitor(sensor, display);
	BOOST_CHECK_EQUAL(display->GetStatus(), TemperatureStatus::NOTSET);
}

BOOST_AUTO_TEST_CASE(DisplayNormalForZeroDegrees)
{
	SENSOR_PTR sensor(new TemperatureSensorFake(0.0));
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());
	TemperatureMonitor monitor(sensor, display);
	monitor.DoMeasurement();
	BOOST_CHECK_EQUAL(display->GetStatus(), TemperatureStatus::NORMAL);
}

BOOST_AUTO_TEST_CASE(DisplayNormalFor99Degrees)
{
	SENSOR_PTR sensor(new TemperatureSensorFake(99.0));
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());
	TemperatureMonitor monitor(sensor, display);
	monitor.DoMeasurement();
	BOOST_CHECK_EQUAL(display->GetStatus(), TemperatureStatus::NORMAL);
}

BOOST_AUTO_TEST_CASE(DisplayWarningFor100Degrees)
{
	SENSOR_PTR sensor(new TemperatureSensorFake(100.0));
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());
	TemperatureMonitor monitor(sensor, display);
	monitor.DoMeasurement();
	BOOST_CHECK_EQUAL(display->GetStatus(), TemperatureStatus::WARNING);
}

BOOST_AUTO_TEST_CASE(DisplayWarningFor199Degrees)
{
	SENSOR_PTR sensor(new TemperatureSensorFake(199.0));
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());
	TemperatureMonitor monitor(sensor, display);
	monitor.DoMeasurement();
	BOOST_CHECK_EQUAL(display->GetStatus(), TemperatureStatus::WARNING);
}

BOOST_AUTO_TEST_CASE(DisplayAlertHiFor200Degrees)
{
	SENSOR_PTR sensor(new TemperatureSensorFake(200.0));
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());
	TemperatureMonitor monitor(sensor, display);
	monitor.DoMeasurement();
	BOOST_CHECK_EQUAL(display->GetStatus(), TemperatureStatus::ALERT_HI);
}

BOOST_AUTO_TEST_CASE(DisplayAlertLowForMinusOneDegrees)
{
	SENSOR_PTR sensor(new TemperatureSensorFake(-1.0));
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());
	TemperatureMonitor monitor(sensor, display);
	monitor.DoMeasurement();
	BOOST_CHECK_EQUAL(display->GetStatus(), TemperatureStatus::ALERT_LOW);
}

BOOST_AUTO_TEST_CASE(MonitorThrowsIfSensorIsNull)
{
	SENSOR_PTR sensor;  // null for test
	DISPLAY_FAKE_PTR display(new TemperatureDisplayFake());	
	
	try 
	{
		TemperatureMonitor monitor(sensor, display);
		BOOST_ERROR("Sensor is null. Should have thrown exception but didn't");
	}
	catch(...){}		
}


BOOST_AUTO_TEST_CASE(MonitorThrowsIfDisplayIsNull)
{
	SENSOR_PTR sensor(new TemperatureSensorFake(10)); 
	DISPLAY_FAKE_PTR display;  // null for test
	
	try 
	{
		TemperatureMonitor monitor(sensor, display);
		BOOST_ERROR("Display is null. Should have thrown exception but didn't");
	}
	catch(...){}	
}
	
BOOST_AUTO_TEST_SUITE_END( )