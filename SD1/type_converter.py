# Author: Maria Caro
# Class: Software Development - Fundamentals of Object Oriented Programming - 5N0541
# Description: Object-oriented type conversion program (int/float/string/list/binary/hex) with Menu.
# Last edited: 2026-01-28

class TypeConverter:
    """
    TypeConverter class provides methods for converting between different data types.

    This class groups together different type-conversion utilities including:
    - Numeric conversions (int/float)
    - String conversions (int to string, string to list)
    - Collection conversions (list to string)
    - Base conversions (int to binary/hexadecimal)

    Each method is interactive and keeps asking for input until the user types "M" to return
    to the main menu.
    """

    def int_to_float(self):
        """
        Convert an integer entered by the user into a floating-point number.

        This method continuously prompts the user for integer input and converts it to float.
        The user can return to the main menu by entering 'M'.
        """
        while True:
            # Display the submenu header for this conversion option
            print("\n--- Integer to Float ---")
            print("M. Go back to Main Menu")

            # Get user input and remove any leading/trailing whitespace
            user_input = input("Enter an integer (or enter M for Main Menu): ").strip()

            # Check if user wants to return to the main menu
            if user_input.upper() == "M":
                return

            # Attempt to convert the input string to an integer
            try:
                number = int(user_input)
            except ValueError:
                # Handle invalid input that cannot be converted to integer
                print("Invalid integer. Example inputs: 42, -7")
                continue  # Re-prompt the user for valid input

            # Convert the integer to float and display the result
            print("Result:", float(number))

    def float_to_int(self):
        """
        Convert a floating-point number entered by the user into an integer.

        This method truncates the decimal part (doesn't round).
        Example: 3.9 becomes 3, -3.9 becomes -3
        """
        while True:
            # Display the submenu header for this conversion option
            print("\n--- Float to Integer ---")
            print("M. Go back to Main menu")

            # Get user input and remove any leading/trailing whitespace
            user_input = input("Enter a float (or M for Main Menu): ").strip()

            # Check if user wants to return to the main menu
            if user_input.upper() == "M":
                return

            # Attempt to convert the input string to a float
            try:
                number = float(user_input)
            except ValueError:
                # Handle invalid input that cannot be converted to float
                print("Invalid float. Example inputs: 3.14, -0.5, 10")
                continue  # Re-prompt the user for valid input

            # Convert float to integer (truncates toward zero) and display result
            print("Result:", int(number))

    def int_to_string(self):
        """
        Convert an integer entered by the user into a string representation.

        This converts the numeric value to its text/character form.
        Example: 42 becomes "42"
        """
        while True:
            # Display the submenu header for this conversion option
            print("\n--- Integer to String ---")
            print("M. Go back to Main Menu")

            # Get user input and remove any leading/trailing whitespace
            user_input = input("Enter an integer (or M for Main Menu): ").strip()

            # Check if user wants to return to the main menu
            if user_input.upper() == "M":
                return

            # Attempt to convert the input string to an integer
            try:
                number = int(user_input)
            except ValueError:
                # Handle invalid input that cannot be converted to integer
                print("Invalid integer. Example inputs: 42, -7")
                continue  # Re-prompt the user for valid input

            # Convert the integer to string format and display result
            print("Result:", str(number))

    def string_to_list(self):
        """
        Convert a string into a list of individual characters.

        Each character in the string becomes a separate element in the list.
        Example: "abc" becomes ['a', 'b', 'c']
        """
        while True:
            # Display the submenu header for this conversion option
            print("\n--- String to List ---")
            print("M. Go back to Main Menu")

            # Get user input and remove any leading/trailing whitespace
            user_input = input("Enter a string (or M for Main Menu): ").strip()

            # Check if user wants to return to the main menu
            if user_input.upper() == "M":
                return

            # Convert the string to a list of characters and display result
            # list() splits the string into individual characters
            print("Result:", list(user_input))

    def list_to_string(self):
        """
        Convert comma-separated items entered by the user into a single string.

        The user enters items separated by commas, and they are combined into one string.
        Example input: "a, b, c" becomes output: "a, b, c"
        Empty items are filtered out.
        """
        while True:
            # Display the submenu header and instructions for this conversion option
            print("\n--- List to String ---")
            print("Enter items separated by commas (example: a, b, c)")
            print("M. Go back to Main menu")

            # Get user input and remove any leading/trailing whitespace
            user_input = input("Enter items (or M for Main Menu): ").strip()

            # Check if user wants to return to the main menu
            if user_input.upper() == "M":
                return

            # Process the comma-separated input:
            # 1. Split the string on commas using split(",")
            # 2. Strip whitespace from each item using part.strip()
            # 3. Filter out empty strings using the if condition
            # This creates a list comprehension that builds a clean list of items
            items = [part.strip() for part in user_input.split(",") if part.strip()]

            # Validate that at least one valid item was entered
            if not items:
                print("No valid items entered. Try again (example: a, b, c).")
                continue  # Re-prompt the user for valid input

            # Join all list items into a single string with ", " as separator
            result = ", ".join(items)
            print("Result:", result)

    def int_to_binary(self):
        """
        Convert an integer entered by the user to its binary representation.

        Binary is base-2 number system using only 0s and 1s.
        The result includes the '0b' prefix to indicate binary format.
        Example: 5 becomes '0b101'
        """
        while True:
            # Display the submenu header for this conversion option
            print("\n--- Integer to Binary ---")
            print("M. Go back to Main Menu")

            # Get user input and remove any leading/trailing whitespace
            user_input = input("Enter an integer (or M for Main Menu): ").strip()

            # Check if user wants to return to the main menu
            if user_input.upper() == "M":
                return

            # Attempt to convert the input string to an integer
            try:
                number = int(user_input)
            except ValueError:
                # Handle invalid input that cannot be converted to integer
                print("Invalid integer. Example inputs: 42, -7")
                continue  # Re-prompt the user for valid input

            # Convert integer to binary string using bin() and display result
            # bin() returns a string with '0b' prefix
            print("Result:", bin(number))

    def int_to_hex(self):
        """
        Convert an integer entered by the user to its hexadecimal representation.

        Hexadecimal is base-16 number system using digits 0-9 and letters a-f.
        The result includes the '0x' prefix to indicate hexadecimal format.
        Example: 255 becomes '0xff'
        """
        while True:
            # Display the submenu header for this conversion option
            print("\n--- Integer to Hexadecimal ---")
            print("M. Go back to Main Menu")

            # Get user input and remove any leading/trailing whitespace
            user_input = input("Enter an integer (or M for Main Menu): ").strip()

            # Check if user wants to return to the main menu
            if user_input.upper() == "M":
                return

            # Attempt to convert the input string to an integer
            try:
                number = int(user_input)
            except ValueError:
                # Handle invalid input that cannot be converted to integer
                print("Invalid integer. Example inputs: 42, -7")
                continue  # Re-prompt the user for valid input

            # Convert integer to hexadecimal string using hex() and display result
            # hex() returns a string with '0x' prefix
            print("Result:", hex(number))


def main():
    # Create a single TypeConverter object to use throughout the program
    # This object will handle all conversion operations
    converter = TypeConverter()

    # Main menu loop: continues running until the user selects option 8 to exit
    while True:
        print("\n--- TYPE CONVERSION MENU ---")
        print("1. Integer to Float")
        print("2. Float to Integer")
        print("3. Integer to String")
        print("4. String to List")
        print("5. List to String")
        print("6. Integer to Binary")
        print("7. Integer to Hexadecimal")
        print("8. Exit")

        # Get user input for menu choice and remove extra spaces
        choice = input("Choose an option (1-8): ").strip()

        # Use match-case statement to execute the corresponding conversion
        match choice:
            case "1":  # Convert integer to float
                converter.int_to_float()
            case "2":  # Convert float to integer
                converter.float_to_int()
            case "3":  # Convert integer to string
                converter.int_to_string()
            case "4":  # Convert string to list
                converter.string_to_list()
            case "5":  # Convert list to string
                converter.list_to_string()
            case "6":  # Convert integer to binary
                converter.int_to_binary()
            case "7":  # Convert integer to hexadecimal
                converter.int_to_hex()
            case "8":  # Exit the program
                print("Program ended.")
                break
            case _:  # Handle invalid input
                print("Invalid choice, try again.")

# Run the program
if __name__ == "__main__":
    main()
