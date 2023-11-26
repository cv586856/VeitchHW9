// read_resistance.cpp
//
#include <iostream>
#include <iomanip>
#include "AnalogIn.h" 

int main() {
	 // AnalogIn
	 AnalogIn analogIn("P9_39"); 

	 //the top resistor value
	 const double topResistor = 10000.0; // 10kΩ

	 //the supply voltage
	 const double supplyVoltage = 1.8; // 1.8V

	  // Read voltage across the bottom resistor
	  double bottomVoltage = analogIn.readVoltage();

	  // Calculate resistance using the voltage divider formula
	  double bottomResistor = (topResistor * (supplyVoltage - bottomVoltage)) / bottomVoltage;

	   // Print the result
	   std::cout << std::fixed << std::setprecision(2);

	   if (bottomResistor < 1000.0) {
		             std::cout << "Resistance: " << bottomResistor << " Ohms" << std::endl;
	   } else {
			     std::cout << "Resistance: " << bottomResistor / 1000.0 << " kOhms" << std::endl;
	   }

	  
	   return 0;
}
