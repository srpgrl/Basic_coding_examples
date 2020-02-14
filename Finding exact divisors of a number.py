def find_divisors(number):
    divisors=[]
    for i in range(2,number):
        if number%i==0:
            divisors.append(i)
    return divisors

while True:
    number=input('Please enter a number or q for quit: ')
    if number=='q':
        print('Exit')
        break
    else:
        number=int(number)
        print('Exact divisors of', number,":", find_divisors(number))
