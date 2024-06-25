# While loops
# repeating a cycle of code while a condtion is true. If it is no longer true it will move on.

# uber driver

people = 1

while people < 5:
    print(f'People in the car: {people}')
    people += 1

print('To many people in car now.')

n = 20
i = 0

while i <= 20:
    if (i % 2 == 0):
        print(f'{i}')
    else:
        print(f'Number {i} is not even')
    i += 1
