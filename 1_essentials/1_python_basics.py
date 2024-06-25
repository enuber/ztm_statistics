# Print function

print('hello, world!')


# can you a comma which adds in spaces automatically
name = 'Erik'
age = '50'

print('my name is', name, 'and i\'m', age, 'years old')

# f-string

print(f'my name is {name} and i\'m {age} years old')


# input
# use input function to get info from a user, can be stored in a variable, gives back a string. You need to transform the outcome of the input if you need it as a different type
# str() # what is inside here becomes a string
# int() # what is inside here becomes an integer

name = input('Please enter your name: ')

age = int(input('Please enter your age: '))

print(f'Entered name: {name}, Entered age: {age}')

# SUPERHERO Challenge
# step 1: find the adjtective on the 13th page of the book
adjective = input('Find first adjective in the 13th page of the book: ')

# step 2: something that scares you (noun)
noun = input('Something that scares you: ')

# step 3: display info to usser
print(f'Superhero name is: {adjective} {noun}')
