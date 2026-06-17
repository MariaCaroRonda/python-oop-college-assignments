# Development Notes – SD3 Python OOP ATM Program with Inheritance

## Requirements

The program needed to:

* Support multiple users
* Authenticate users using an account number and PIN
* Lock users out after three failed login attempts
* Display account balances
* Allow cash withdrawals
* Allow cash lodgements
* Prevent withdrawals above the available balance
* Prevent withdrawals above the available ATM cash
* Apply account balance limits
* Calculate note payouts
* Provide administrator access for ATM refills
* Use inheritance

## Design Decisions

I created a base `User` class to store common user information such as account number, PIN, balance, and account limits.

Two child classes inherit from `User`:

* `Customer`
* `Admin`

The `Customer` class handles customer operations such as:

* Checking balances
* Lodging cash
* Withdrawing cash

The `Admin` class provides functionality for refilling the ATM.

The `ATM` class stores:

* User accounts
* Available ATM cash
* Note values
* Authentication logic
* Menu functionality

Using inheritance allowed common user information to be stored in a single parent class while giving customers and administrators different responsibilities.

## Challenges

One challenge was implementing inheritance while keeping responsibilities separate between customers, administrators, and the ATM.

Another challenge was validating transactions and enforcing business rules such as:

* Account balance checks
* ATM cash availability checks
* Account limit checks
* Login attempt limits

The note payout calculation also required determining the smallest number of notes needed for a withdrawal.

## What I Learned

This project helped me practise:

* Object-Oriented Programming (OOP)
* Inheritance
* Parent and child classes
* User authentication
* Working with dictionaries
* User input validation
* Error handling using exceptions
* Designing larger programs using multiple classes
* Testing a Python application

## Possible Improvements

Some ideas for future improvements:

* Store account information in an external file or database
* Add transaction history
* Allow users to change their PIN
* Add account creation functionality
* Create a graphical user interface (GUI)
* Add automated tests

During review of the code, I identified a couple of areas that could be improved:

* Authentication, transaction processing, and user management could be separated into additional classes to further improve maintainability.
* User account information could be loaded from an external data source instead of being stored directly in the program.
* Additional administrator features could be added, such as viewing ATM statistics or transaction reports.

## Conclusion

This project gave me practical experience using inheritance to extend an existing object-oriented application.

It also helped me improve my understanding of class hierarchies, authentication, validation, and organising larger programs using multiple classes.
