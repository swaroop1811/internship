def bank_system():
    balance = 1000

    print("Initial Balance:", balance)

    deposit = int(input("Enter deposit amount: "))
    balance = balance + deposit

    withdraw = int(input("Enter withdraw amount: "))

    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdraw successful")
    else:
        print("Insufficient balance")

    print("Final Balance:", balance)


bank_system()
