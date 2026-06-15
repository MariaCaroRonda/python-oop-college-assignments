# Author: Maria Caro
# Class: Software Development - Object-Oriented Programming - 5N0541
# Description: ATM program applying object-oriented programming principles.
# The program allows a user to log in with a user ID and PIN,
# then check balance, withdraw cash, lodge cash, or exit.
# Last edited: 2026-03-08


class ATM:
    """
    ATM class that handles user authentication and basic banking actions.

    This class stores user account details and provides methods for:
    - logging in
    - checking account balance
    - withdrawing money
    - lodging money
    - displaying the ATM menu
    """

    def __init__(self):
        self.users = {
            "U001": {"pin": "1234", "balance": 500.50},
            "U002": {"pin": "5678", "balance": 1000.00},
            "U003": {"pin": "2468", "balance": 750.25},
            "U004": {"pin": "1357", "balance": 300.00}
        }
        self.current_user = None

    def authenticate_user(self):
        # Request userID and PIN until it's correct
        while True:
            user_id = input("Enter User ID: ")
            if user_id not in self.users:
                print("Invalid User ID")
            else:
                break

        while True:
            pin = input("Enter your PIN number: ")
            if pin != self.users[user_id]["pin"]:
                print("Incorrect PIN.")
            else:
                self.current_user = user_id
                print("Login successful.")
                break

    def check_balance(self):
        return self.users[self.current_user]["balance"]

    def display_balance_message(self):
        print(f"Welcome {self.current_user}, your current balance is {self.check_balance():.2f}")

    def lodge_cash(self, amount):
        if amount <= 0:
            return "Amount must be greater than 0."
        self.users[self.current_user]["balance"] += amount
        return self.users[self.current_user]["balance"]

    def withdraw_cash(self, amount):
        if amount <= 0:
            return "Amount must be greater than 0."
        if amount > self.users[self.current_user]["balance"]:
            return "Amount cannot be greater than current balance."
        self.users[self.current_user]["balance"] -= amount
        return self.users[self.current_user]["balance"]

    def display_menu(self):
        print("\n--- ATM OPTIONS ---")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Lodge Cash")
        print("4. Exit")
        return input("Choose an option: ")


def main():
    """
    Main function that runs the ATM program.
    It creates an ATM object, authenticates the user,
    and keeps showing the menu until the user exits.
    """
    # Create the ATM object
    atm = ATM()

    # Display welcome message
    print("--- ATM MENU ---")
    print("Please insert your card and follow the menu.")

    # Ask the user to log in
    atm.authenticate_user()

    # Keep showing the menu until the user chooses to exit
    while True:
        option = atm.display_menu()

        # Option 1: show current user and balance
        if option == "1":
            atm.display_balance_message()

        # Option 2: withdraw cash
        elif option == "2":
            try:
                # Ask the user for the withdrawal amount
                amount = float(input("Enter amount to withdraw: "))

                # Attempt the withdrawal
                result = atm.withdraw_cash(amount)

                # If result is a string, it is an error message
                if isinstance(result, str):
                    print(result)
                else:
                    # Otherwise, result is the new balance
                    print(f"Withdraw successful. New balance is {result:.2f}")
            except ValueError:
                # Handle invalid number input
                print("Please enter a valid number.")

        # Option 3: lodge cash
        elif option == "3":
            try:
                # Ask the user for the lodgement amount
                amount = float(input("Enter amount to lodge: "))

                # Attempt the lodgement
                result = atm.lodge_cash(amount)

                # If result is a string, it is an error message
                if isinstance(result, str):
                    print(result)
                else:
                    # Otherwise, result is the new balance
                    print(f"Lodgement successful. New balance is {result:.2f}")
            except ValueError:
                # Handle invalid number input
                print("Please enter a valid number.")

        # Option 4: exit the program
        elif option == "4":
            print("ATM program ended.")
            break

        # Handle any invalid menu option
        else:
            print("Invalid option. Valid options are 1-4")


# Run the program
if __name__ == "__main__":
    main()
