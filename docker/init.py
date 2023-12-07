import os
import sys

def create_file(filename):
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine the directory and filename to get the full path
    file_path = os.path.join(script_dir, filename)

    try:
        # Create a new file in the specified path
        with open(file_path, 'w') as new_file:
            print(f"File '{filename}' created successfully at '{script_dir}'.")
    except Exception as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python create_file.py <filename>")
        sys.exit(1)

    # Get the filename from the command-line argument
    filename = sys.argv[1]

    # Call the function to create the file
    create_file(filename)
