def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, "r") as infile:
            original_content = infile.read()

        # Modify the content
        modified_content = modify_content(original_content)

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")

# Run the program
read_and_write_file()
