
### Armstrong number

number=input('Please enter a number: ')
digit_number=len(number)
total=0

for i in number:
    total += ((int(i)) ** digit_number)

if int(number) == total:
    print(number, 'is an Armstrong number.')
else:
    print(number, 'is not an Armstrong number')