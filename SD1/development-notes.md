# Development Notes – SD1 Python OOP Type Converter

## Requirements

The program needed to:

* Convert integers to floating-point numbers
* Convert floating-point numbers to integers
* Convert integers to strings
* Convert strings to lists
* Convert lists to strings
* Convert integers to binary values
* Convert integers to hexadecimal values
* Provide a menu-driven interface
* Validate user input
* Display clear messages

## Design Decisions

I created a `TypeConverter` class to group all conversion operations into a single object.

Each conversion was implemented in its own method:

* `int_to_float()`
* `float_to_int()`
* `int_to_string()`
* `string_to_list()`
* `list_to_string()`
* `int_to_binary()`
* `int_to_hex()`

This made the program easier to organise and maintain.

The application uses a main menu that allows the user to select a conversion option and return to the menu when finished.

## Challenges

One challenge was handling invalid user input.

To solve this, I used `try/except` blocks to catch conversion errors and display helpful messages instead of allowing the program to crash.

Another challenge was creating a menu system that allowed the user to perform multiple conversions without restarting the program.

## What I Learned

This project helped me practise:

* Object-Oriented Programming (OOP)
* Creating and using Python classes
* Writing methods for separate tasks
* User input validation
* Type conversion
* Error handling using exceptions
* Loops and conditional logic
* Testing a Python application

## Possible Improvements

Some ideas for future improvements:

* Add support for additional type conversions
* Allow conversions between more collection types
* Save conversion results to a file
* Create a graphical user interface (GUI)
* Add automated tests

During review of the code, I identified a couple of areas that could be improved:

* Some input validation logic is repeated across several conversion methods. This could be refactored into helper methods to reduce duplicated code and make maintenance easier.
* The menu system currently uses a separate `match-case` block for each conversion option. A future version could use a dictionary of operations to simplify the menu logic and make it easier to add new conversions.

## Conclusion

This project gave me practical experience using classes and methods to organise code.

It also helped me improve my understanding of data type conversions, user input validation, and exception handling in Python.
