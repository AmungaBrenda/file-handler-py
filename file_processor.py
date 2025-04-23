import os

def process_file():
    """
    Reads a file provided by the user, modifies its content, and writes to a new file.
    Includes comprehensive error handling for various file-related issues.
    """
    print("File Modification Program")
    print("-------------------------")
    
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Check if file exists
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"Error: The file '{input_filename}' does not exist.")
        
        # Check if file is readable
        if not os.access(input_filename, os.R_OK):
            raise PermissionError(f"Error: You don't have permission to read '{input_filename}'.")
        
        # Read the content of the file
        with open(input_filename, 'r') as file:
            content = file.read()
            
        # Get output filename from user
        output_filename = input("Enter the name for the modified output file: ")
        
        # Check if output file already exists
        if os.path.exists(output_filename):
            choice = input(f"Warning: '{output_filename}' already exists. Overwrite? (y/n): ").lower()
            if choice != 'y':
                print("Operation cancelled.")
                return
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        try:
            with open(output_filename, 'w') as file:
                file.write(modified_content)
            print(f"Success! Modified content written to '{output_filename}'.")
            
            # Display statistics
            print(f"Original file size: {len(content)} characters")
            print(f"Modified file size: {len(modified_content)} characters")
            
        except PermissionError:
            print(f"Error: You don't have permission to write to '{output_filename}'.")
        except IOError as e:
            print(f"Error writing to file: {e}")
            
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except UnicodeDecodeError:
        print(f"Error: '{input_filename}' contains characters that cannot be decoded. Is this a text file?")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file()
    
    # Ask if the user wants to process another file
    while input("\nProcess another file? (y/n): ").lower() == 'y':
        process_file()
    
    print("Thank you for using the File Modification Program!")