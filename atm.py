import csv
def atm():
    try:
        filename = input("Enter the filename:")
        with open(filename,"r") as file:
            reader = csv.reader(file)
            header = next(reader)
            print("Header:",header)
            for row in reader:
                pin = int(row[0])
                bal = int(row[1])
        user_pin = int(input("Enter pin:"))
        if user_pin != pin:
            print("Invalid pin")
            return
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance")
        choice = int(input("Enter choice"))
        if choice == 1:
            amt = int(input("Enter deposited amount:"))
            if amt > 0:
                bal += amt
                print("Deposited Successful:")
                print("Updated Balance:",bal)
            else:
                print("Invalid amount")
        elif choice ==2:
            amt = int(input("Enter Withdrawal amount"))
            if amt <= bal:
                bal -= amt
                print("Withdraw Successful:")
                print("Remaining balance:",bal)
            else:
                print("Insufficient Balance:")
        elif choice == 3:
            print("Your balance:",bal)
        else:
            print("Incorrect choice:")
    except ValueError as e:
        print("Enter numbers only",e)
atm()
