# For Loop
#  can repeat tasks elegantly and efficiently

# iterate over a sequence like lists, dictionaries and strings

# for variable in sequence:
#   code to be executed

colors = ['red', 'blue', 'green']

for color in colors:
    print(f'The color is {color}')

# can be combined with range() to repeat code a specific number of times

# goes from 0 to 5
# x = list(range(1, 5))  # [1,2,3,4]
# print(x)
for i in range(5):
    print(f'interation: {i}')


# Exercise
# Sum of numbers
# user inputs a number add up from 1 to that number 4 then do 4+3+2+1

num = int(input('Enter a number ? '))
sum = 0
for i in range(1, num + 1):
    sum += i
print(sum)


# Excercise
# Count number of times a character in a string
# 'd' : 1
# 'i' : 2 etc

letters = {}
word = input('Please enter a word or sentence. ').lower()
for char in word:
    if char == ' ':
        continue
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1

print("Character count")
for char, count in letters.items():
    print(f'{char} : {count}')
