# build.sh

#!/bin/bash

# Compile the C++ program
g++ -o read_resistance read_resistance.cpp AnalogIn.cpp -std=c++11

# Check if compilation was successful
if [ $? -eq 0 ]; then
	    echo "Compilation successful. To run the program, use: ./read_resistance"
    else
	        echo "Compilation failed"
fi

