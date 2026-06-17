# Development Notes – SD2 Python OOP ATM Program

## Requirements

The program needed to:

* Support multiple users
* Authenticate users using a user ID and PIN
* Display account balances
* Allow cash withdrawals
* Allow cash lodgements
* Provide a menu-driven interface
* Validate user input
* Display clear messages

## Design Decisions

I created an `ATM` class to store user account information and manage ATM operations.

User accounts are stored in a dictionary, with each account containing:

* User ID
* PIN
* Account balance

The application separates responsibilities into individual methods such as:

* `authenticate_user()`
* `check_balance()`
* `withdraw_cash()`
* `lodge_cash()`
* `display_menu()`

This made the code easier to organise and maintain.

## Challenges

One challenge was validating user login details.

To solve this, I added checks for invalid user IDs and incorrect PINs before allowing access to ATM functions.

Another challenge was handling invalid transactions such as:

* Negative amounts
* Zero amounts
* Withdrawals greater than the available balance

The program validates these conditions and displays clear error messages.

## What I Learned

This project helped me practise:

* Object-Oriented Programming (OOP)
* Creating and using Python classes
* Working with dictionaries
* User authentication
* User input validation
* Updating stored data
* Error handling using exceptions
* Testing a Python application

## Possible Improvements

Some ideas for future improvements:

* Store user accounts in an external file or database
* Allow users to change their PIN
* Add transaction history
* Add account creation functionality
* Create a graphical user interface (GUI)
* Add automated tests

During review of the code, I identified a couple of areas that could be improved:

* Login attempts could be limited to improve security.
* Repeated validation and transaction messages could be moved into helper methods to reduce duplicated code.
* User account information could be separated from the ATM logic into dedicated account objects.

## Conclusion

This project gave me practical experience designing an object-oriented application that manages user authentication and account transactions.

It also helped me improve my understanding of dictionaries, validation, and organising functionality into classes and methods.
