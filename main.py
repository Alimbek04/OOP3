# main.py
from person import PersonalAccount


def main():
    # Create a new personal account
    account_number = int(input("Enter account number: "))
    account_holder = input("Enter account holder's name: ")
    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transaction History")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.print_transaction_history()
        elif choice == '4':
            print(f"Current Balance: ${account.get_balance():.2f}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()