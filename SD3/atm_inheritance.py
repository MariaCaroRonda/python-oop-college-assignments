# Author: Maria Caro
# Class: Software Development - Object-Oriented Programming - 5N0541
# Description: ATM simulation program using object-oriented programming.
# The program allows users to authenticate, check balance, withdraw cash,
# lodge money, and allows an administrator to refill the ATM.
# Last edited: 2026-03-23

class User:
    """Base class representing a bank user"""

    def __init__(self, account_number, pin, balance, account_limit):
        # Store the user's account number
        self.account_number = account_number

        # Store the user's PIN
        self.pin = pin

        # Store the current account balance
        self.balance = balance

        # Store the maximum amount allowed in the account
        self.account_limit = account_limit


class Customer(User):
    """Customer class inheriting from User"""

    def check_balance(self):
        # Show the customer their current balance
        print(f"Current balance: €{self.balance:.2f}")

    def lodge_cash(self, amount):
        # Check if the amount is valid
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        # Check if adding the money would pass the account limit
        if self.balance + amount > self.account_limit:
            print("Account limit exceeded.")
        else:
            # Add the amount to the balance
            self.balance += amount
            print(f"Lodgement successful. New balance: €{self.balance:.2f}")

    def withdraw_cash(self, amount, atm):
        # Check if the withdrawal amount is valid
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        # Check if the customer has enough money
        if amount > self.balance:
            print("Insufficient account balance.")

        # Check if the ATM has enough cash
        elif amount > atm.atm_cash:
            print("ATM does not have enough cash.")

        # Check if the amount can be paid using the available notes
        elif amount % 5 != 0:
            print("Amount must be in multiples of 5.")

        else:
            # Remove the money from the customer's balance
            self.balance -= amount

            # Remove the money from the ATM cash
            atm.atm_cash -= amount

            # Show the new balance
            print(f"Withdrawal successful. New balance: €{self.balance:.2f}")

            # Show the note breakdown
            atm.calculate_notes(amount)


class Admin(User):
    """Administrator class inheriting from User"""

    def refill_atm(self, atm, amount):
        # Check if the refill amount is valid
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        # Add cash to the ATM
        atm.atm_cash += amount

        # Show the new ATM cash total
        print(f"ATM refilled. Total ATM cash: €{atm.atm_cash:.2f}")


class ATM:
    """ATM machine class"""

    def __init__(self):
        # Set the starting amount of cash in the ATM
        self.atm_cash = 5000

        # Store the note values used in withdrawals
        self.notes = [50, 20, 10, 5]

        # Store all users in a dictionary
        self.users = {
            "A001": Customer("A001", "1234", 500.0, 2000),
            "A002": Customer("A002", "5678", 10000.0, 2000),
            "A003": Customer("A003", "2468", 750.0, 2000),
            "A004": Customer("A004", "1357", 300.0, 2000),
            "ADMIN": Admin("ADMIN", "9999", 0, 0)
        }

    def authenticate_user(self):
        # Keep track of how many times the user tries to log in
        attempts = 0

        # Allow the user to try 3 times
        while attempts < 3:
            # Ask for the account number
            account = input("Enter account number: ").strip()

            # Ask for the PIN
            pin = input("Enter PIN: ").strip()

            # Check if the account exists and the PIN is correct
            if account in self.users and self.users[account].pin == pin:
                print("Login successful.")
                return self.users[account]
            else:
                # Increase the number of failed attempts
                attempts += 1
                print("Incorrect account number or PIN.")

        # Lock the user out after 3 failed attempts
        print("User locked out after 3 incorrect attempts.")
        return None

    def display_menu(self):
        # Show the customer menu
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Lodge Cash")
        print("4. Exit")

        # Get the user's choice
        return input("Choose an option: ")

    def calculate_notes(self, amount):
        # Show that the ATM is dispensing notes
        print("Dispensing notes:")

        # Go through each note value from largest to smallest
        for note in self.notes:
            # Work out how many of this note can be given
            count = amount // note

            # If at least one note can be given, show it
            if count > 0:
                print(f"€{note} x {int(count)}")

                # Update the remaining amount
                amount = amount % note


def main():
    atm = ATM()

    print("--- Welcome to the ATM ---")

    user = atm.authenticate_user()

    if user is None:
        return

    # If the user is an admin, show the admin option
    if isinstance(user, Admin):
        # Ask how much cash to add
        try:
            amount = float(input("Enter amount to refill ATM: "))
            user.refill_atm(atm, amount)
        except ValueError:
            print("Please enter a valid number.")
        return

    # Customer menu loop
    while True:
        # Show the menu and get the choice
        option = atm.display_menu()

        # Option 1: check balance
        if option == "1":
            user.check_balance()

        # Option 2: withdraw cash
        elif option == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                user.withdraw_cash(amount, atm)
            except ValueError:
                print("Please enter a valid number.")

        # Option 3: lodge cash
        elif option == "3":
            try:
                amount = float(input("Enter amount to lodge: "))
                user.lodge_cash(amount)
            except ValueError:
                print("Please enter a valid number.")

        # Option 4: exit program
        elif option == "4":
            print("Thank you for using the ATM.")
            break

        # Handle invalid input
        else:
            print("Invalid option.")


# Start the program
if __name__ == "__main__":
    main()
