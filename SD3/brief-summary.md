# Brief Summary: SD3 ATM Program with Inheritance

## Module

Fundamentals of Object-Oriented Programming 5N0541

## Assignment Title

Skills Demonstration 3: Design, code, and test an object-oriented program that uses inheritance.

## Task Summary

The task was to extend the ATM simulation from Skills Demonstration 2 by using inheritance and adding more advanced ATM functionality.

The program needed to support at least four users and allow customers to:

- Access the ATM using an account number and PIN
- Check their balance
- Withdraw cash
- Lodge cash
- Exit the program

The program also needed to include:

- User lockout after three incorrect login attempts
- Prevention of withdrawals above the user's account balance
- Prevention of withdrawals above the available ATM cash
- A limit on each customer's account
- Withdrawal payout using the least number of notes
- Administrator access to top up the cash available in the ATM
- Classes, identifiers, and methods/functions in the code

## Main Requirements

The assignment required:

- A simple algorithm
- A flowchart
- Pseudocode
- A data dictionary
- A working Python program
- Object-oriented programming using inheritance
- Appropriate variables and data types
- Classes, identifiers, and methods/functions
- Clear comments
- Suitable variable and object names
- Testing and debugging evidence

## Implementation Summary

My solution uses a base `User` class and two child classes: `Customer` and `Admin`.

The `Customer` class handles customer actions such as checking balance, lodging cash, and withdrawing cash. The `Admin` class handles refilling the ATM. The `ATM` class stores the available ATM cash, note values, and user accounts.

The program authenticates users with an account number and PIN. If incorrect details are entered three times, the user is locked out. Customers cannot withdraw more than their account balance or more than the cash available in the ATM. Lodgements are checked against each customer's account limit. Withdrawals are paid out using the least number of available notes.

## Result

Distinction — 28/30

## Grade Breakdown

| Criteria | Marks |
|---|---:|
| Clearly Documented Source Code | 3/3 |
| Program Functionality | 3/3 |
| Accurate Programming: Syntax and Semantics | 18/20 |
| Software Testing/Debugging | 4/4 |
| **Total** | **28/30** |

## What I Learned

This assignment helped me practise:

- Using inheritance in Python
- Creating a parent class and child classes
- Separating user roles into customer and administrator classes
- Building on an earlier program with additional requirements
- Authenticating users with account numbers and PINs
- Handling failed login attempts
- Applying account balance and account limit rules
- Checking available ATM cash before withdrawals
- Calculating note payouts
- Testing and debugging a larger interactive Python program