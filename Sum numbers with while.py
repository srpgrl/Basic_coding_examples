### Sum Numbers

total = 0

while True:
    number=(input('Please enter a number: '))
    if number == 'Q':
        break
    else:
        total += int(number)

print('Total:', total)
