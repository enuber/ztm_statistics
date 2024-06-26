# Dictionaries
# versatile data structure
# mutable, unordered collections of key-value pairs. each key corresponds to a specific value
# to create use {}. separate keys:values with a colon

my_spellbook = {
    'fireball': 3,
    'teleport': 5,
    'heal': 2
}

my_spellbook2 = dict(flame=3, ice=4, lava=5)

print(my_spellbook)
print(my_spellbook2.items())
my_spellbook['fireball']  # 3

# adding
my_spellbook['lightning'] = 4
print(my_spellbook)

# update
my_spellbook['heal'] = 3
print(my_spellbook)

# delete
del my_spellbook['teleport']
print(my_spellbook)

# access keys
print(my_spellbook.keys())
print(my_spellbook.values())


# Magical pet sound dictionary
pet_sounds = {'mew': 'I am hungry',
              'woof': 'I want to play',
              'grr': 'I am angry'}

# Create a Python code that tells the user the meaning of the sound
print(f"The possibilities are {list(pet_sounds.keys())}")
sound = input("Enter the magical sound: ")

# Interpret the meaning
# meaning = pet_sounds[sound]
# different way to get the sound with a fallback, get can be used to still get things out of dictiionary and, the second argument is what to do if it's not found
meaning = pet_sounds.get(sound, "nonsense")

# Communicate the findings
print(f"Your magical pet said {meaning}")


# CHALLENGE

# Data structure for income and expenses
expenses = {'groceries': 0, 'entertainment': 0, 'shopping': 0, 'other': 0}
income = {'salary': 0, 'investments': 0, 'other': 0}
transactions = []

# User input
while True:
    transaction_type = input("Is it an income or an expense?: ")
    if transaction_type == 'income':
        source = input("Enter the source (salary, investments or other): ")
        amount = float(input("Enter the amount: "))
        income[source] += amount
        # adding a dictionary into a list
        transactions.append(dict(transaction_type=transaction_type,
                                 source=source,
                                 amount=amount))

    elif transaction_type == 'expense':
        category = input(
            "Enter the category (groceries, entertainment, shopping or other): ")
        amount = float(input("Enter the amount: "))
        expenses[category] += amount
        transactions.append(dict(transaction_type=transaction_type,
                                 category=category,
                                 amount=amount))
    else:
        break

# calculations
total_income = sum(income.values())
total_expenses = sum(expenses.values())
balance = total_income - total_expenses

# Print the info to the uses
print("Transaction list: ")
print(transactions)
print(f"The total income is {total_income}")
print(f"The total expenses is {total_expenses}")
print(f"Your current balance is {balance}")


# Challenge
locations = {
    'start': {
        'description': "You are at the starting point. There are two paths: left and right.",
        'options': {'left': 'forest', 'right': 'cave'}
    },
    'forest': {
        'description': "You are in a dense forest. There are two paths: forward and backward.",
        'options': {'forward': 'river', 'backward': 'start'}
    },
    'cave': {
        'description': "You are inside a dark cave. There are two paths: forward and backward.",
        'options': {'forward': 'treasure', 'backward': 'start'}
    },
    'river': {
        'description': "You are at the edge of a roaring river. There is no way forward.",
        'options': {'backward': 'forest'}
    },
    'treasure': {
        'description': "You've found the treasure! Congratulations!",
        'options': {}
    }
}

# Game
current_location = 'start'

while True:
    # user's location description
    print(locations[current_location]['description'])

    # give the user options
    options = locations[current_location]['options']
    print("Options:")
    for option in options:
        print(f" - {option}")

    # Get the user input
    user_choice = input("Choose an option: ").lower()

    # Validate the options
    while user_choice not in options:
        user_choice = input("Invalid option. Choose again: ").lower()

    # Update the current location
    current_location = options[user_choice]

    # Finish the game
    if current_location == 'treasure':
        break

# print final message
print("Game over! You found the treasure")
