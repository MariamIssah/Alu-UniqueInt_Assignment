class UniqueIntProcessor:
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31

    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.unique_integers = set()  # Use a set to store unique integers

    def read_input(self):
        try:
            with open(self.input_file_path, "r") as file:
                print(f"Reading from {self.input_file_path}...")  # Debugging line
                for line in file:
                    line = line.strip()
                    print(f"Read line: '{line}'")  # Debugging line
                    self.process_line(line)
        except FileNotFoundError:
            print(f"File {self.input_file_path} not found. Please check the file path.")
            exit()

    def process_line(self, line):
        try:
            my_int = int(line)
            print(f"Parsed integer: {my_int}")  # Debugging line
            if self.MIN_INT <= my_int <= self.MAX_INT:
                self.unique_integers.add(my_int)
                print(f"Added {my_int} to unique_integers")  # Debugging line
        except ValueError:
            print(f"Skipping line: '{line}' (not an integer)")  # Debugging line

    def write_output(self):
        if not self.unique_integers:
            print("No valid integers were found in the input file.")
            return
        
        sorted_integers = self.sort_unique_integers()  # Sort the unique integers
        
        with open(self.output_file_path, 'w') as output_file:
            print(f"Writing sorted integers to {self.output_file_path}...")  # Debugging line
            for integer in sorted_integers:
                output_file.write(f"{integer}\n")

        print(f"Processing complete! The results are stored in {self.output_file_path}")

    def sort_unique_integers(self):
        # Convert the set to a list and sort it
        return sorted(self.unique_integers)  # Use built-in sorting for simplicity

    def print_output(self):
        try:
            with open(self.output_file_path, 'r') as output_file:
                print("Content of the output file:")
                content = output_file.read().strip()  # Read the entire file content
                if content:
                    print(content)  # Print the file content
                else:
                    print("The output file is empty.")  # In case there's nothing in the file
        except FileNotFoundError:
            print(f"File {self.output_file_path} not found. Please check the file path.")

# Set the paths for the input and output files
input_file_path = "C:/Users/awini/Alu-UniqueInt_Assignment/dsa/hw01/input_01.txt"
output_file_path = "C:/Users/awini/Alu-UniqueInt_Assignment/dsa/hw01/output_01.txt"

# Create an instance of UniqueIntProcessor
processor = UniqueIntProcessor(input_file_path, output_file_path)
processor.read_input()  # Read integers from the input file
processor.write_output()  # Write the unique integers to the output file
processor.print_output()  # Print the output file content to the console
