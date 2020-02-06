print(""" ********************
Welcome to ATM Machine

Transactions:

1.Balance Inquiry
2.Deposit Money
3.Withdraw Money

Press Q to quit.
***************************** """)

balance=1000

while True:
    transaction=input('Please select transaction: ')

    if transaction=='Q':
        print('Good Days.')
        break
    elif transaction == "1":
        print('Your deposit: {}'.format(balance))

    elif transaction == "2":
        quantity=int(input('Please enter quantity: '))
        balance += quantity

    elif transaction == "3":
        quantity = int(input('Please enter quantity: '))
        if balance < quantity:
            print('You can not withdraw such an amount')
            continue
        balance -= quantity
    else:
        print('Invalid transaction')

