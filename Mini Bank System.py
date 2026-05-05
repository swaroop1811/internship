def bank_system():
    balance = 1000;

    print("Initial Balance:", balance)

    deposit = int("Enter deposit amount: "))
    balance = balance + deposit

    withdraw = int("Enter withdraw amount "))

    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdraw successful")
    else
        print("Insufficient balance")

    print("Final Balance:", balance);


bank_system()
