class BalException(Exception):
    # __init__ is a constructor.
    def __init__(self, msg):
        self.msg = msg


customerid = "4504563922"
customername = "Albin Benny"
balance = 50000
# here int is nothing but a whole number
amount = int(input("Enter the amount do you want to withdraw:"))

if (amount > balance):
    print("Insufficient funds in your account")

else:
    # Using try Keyword here

    try:

        # 50000-46000=4000#here if you are trying to withdraw 96000 then what is balance
        balance = balance-amount

        if (balance < 5000):  # 4000<5000
            balance = balance+amount  # 4000+46000=50000
            # Using raise Keyword here
            raise BalException("Minimum Balance should be maintained is 5000:")
    # Using except Keyword here
    except BalException as be:
        print(be)
    # Using finally Keyword here
    finally:  # It is going to show you the balacne at all cases.
        print("The remaining balance is:", balance)
