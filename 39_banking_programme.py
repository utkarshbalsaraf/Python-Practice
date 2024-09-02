def show_balance(balance):
    print(f"Your balance is : ${balance}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("Invalid Amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount < 0:
        print("Invalid Amount")
        return 0
    elif amount > balance:
        print("Insufficient Balance")
        print(f"Your balance is {balance}")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------------------------------------------")
        print("Banking Programme")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")
    print("Thank you! Have a nice day!")


if __name__ == '__main__':
    main()
