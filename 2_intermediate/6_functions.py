# Functions

# reasons to use
# reusability
# organization
# debugging

def greet():
    print('howdy partner!')


greet()


def food(food1):
    print(f'{food1} are good')


food('oranges')

# exercise


def add(a, b):
    return a + b


print(add(4, 5))


# count the vowels in a word

def count_vowels(word):
    word = word.lower()
    vowels = 'aeiou'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


print(count_vowels('ninja'))


# Ingredient list
ingredients = [
    {'name': 'flour', 'quantity': 200, 'unit': 'g'},
    {'name': 'sugar', 'quantity': 100, 'unit': 'g'},
    {'name': 'butter', 'quantity': 150, 'unit': 'g'},
    {'name': 'eggs', 'quantity': 2, 'unit': 'pcs'},
    {'name': 'vanilla extract', 'quantity': 5, 'unit': 'ml'}
]

# Conversion table
conversion_table = {
    'g': {'oz': 0.035274, 'cups': 0.00422675, 'tbsp': 0.067628, 'tsp': 0.202884},
    'oz': {'g': 28.3495, 'cups': 0.119826, 'tbsp': 1.91722, 'tsp': 5.75167},
    'cups': {'g': 236.588, 'oz': 8.3454, 'tbsp': 16, 'tsp': 48},
    'tbsp': {'g': 14.7868, 'oz': 0.521594, 'cups': 0.0625, 'tsp': 3},
    'tsp': {'g': 4.92892, 'oz': 0.173473, 'cups': 0.0208333, 'tbsp': 0.333333}
}

# defining a function that converts units


def convert_units(quantity, from_unit, to_unit):
    if from_unit == to_unit:
        conversion_factor = 1
    else:
        conversion_factor = conversion_table[from_unit][to_unit]
    return quantity * conversion_factor

# Build function to convert recipes


def recipe_converter(ingredients, recipe_factor, desired_units):
    # converted ingredients
    converted_recipe = []

    for i in range(len(ingredients)):
        # Get the data
        ingredient = ingredients[i]
        original_quantity = ingredient['quantity']
        original_unit = ingredient['unit']
        desired_unit = desired_units[i]

        # Scale the quantities
        scaled_quantity = original_quantity * recipe_factor

        # convert units
        converted_quantity = convert_units(scaled_quantity,
                                           original_unit,
                                           desired_unit)
        # store the converted ingredients
        converted_ingredients = {'name': ingredient['name'],
                                 'quantity': converted_quantity,
                                 'unit': desired_unit}
        converted_recipe.append(converted_ingredients)
    return converted_recipe


# ingredients
recipe_factor = 3
desired_units = ['cups', 'oz', 'tsp', 'pcs', 'ml']

# Apply the funtions
recipe_converted = recipe_converter(ingredients,
                                    recipe_factor,
                                    desired_units)

# get the results
print("Original Recipe")
for i in ingredients:
    print(i)
print("Converted Recipe")
for i in recipe_converted:
    print(i)
