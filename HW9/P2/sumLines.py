# sumLines.py
# This script reads a text file and computes the sum, number of integers, and the average of all numbers.
# The script takes one command line argument - the path to the input text file.
# Example invocation: python3 sumLines.py dataInput.txt

import sys

def process_file(file_path):
        # Initialize variables to keep track of sum and number of elements
        total_sum = 0
        num_elements = 0

        # Open the file and process each line
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into a list of integers
                numbers = [int(num) for num in line.split()]

                # Update sum and number of elements
                total_sum += sum(numbers)
                num_elements += len(numbers)

        # Calculate the average
        average = total_sum / num_elements if num_elements != 0 else 0

        # Display the results
        print(f"Sum = {total_sum}, Number of Elements = {num_elements}, Average = {average}")


if __name__ == "__main__":
        # Check if the correct number of command line arguments is provided
            if len(sys.argv) != 2:
                print("Usage: python3 sumLines.py <input_file>")
                sys.exit(1)  # Exit with an error code

        # Get the file path from the command line arguments
                input_file = sys.argv[1]

        # Process the file and display the results
                process_file(input_file)
