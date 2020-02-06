
### Finding Perfect Number

number=int(input('Please enter a number: '))

total=0
i=1

while i<number:
    if number % i == 0 :
        total += i
    i += 1

if total == number:
    print(number, 'is a perfect number')
else:
    print(number, 'is not a perfect number')