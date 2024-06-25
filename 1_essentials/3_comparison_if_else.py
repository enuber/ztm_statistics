# comparison values
# compare two values and return a boolean either true or false

# == equal
# != not equal
#  > greater than
#  < less than
#  >= greather than or equal to
# <= less than or equal to

# Split bill challenge
# :.2f - means two decimal places to show

# Prompt the user for the total cost of the meal. 1.
total_cost = float(input('Total cost of the meal? : '))

# Prompt the user for the tip percentage they would like to apply. 2.
tip_percentage = float(input('How much would you like to tip? : '))
# Prompt the user for the number of people at the table. 3.
num_people = int(input('How many people are at the table? : '))
# Calculate the tip amount using the tip percentage and the meal cost. 4.
tip_amount = (tip_percentage / 100) * total_cost
# Calculate the total cost of the meal, including the tip. 5.
final_cost_of_meal_with_tip = tip_amount + total_cost
# Divide the total cost by the number of people at the table. 6.
cost_per_person = final_cost_of_meal_with_tip / num_people
# Display the tip amount, total cost, and cost per person to the user. 7.
print(f'Tipping: ${tip_amount:.2f}, total cost: ${
      total_cost:.2f}, total per person: ${cost_per_person:.2f}')


# CONDITIONS
# if, elif, else

x = 10

if x > 5:
    print('x is greater than 5')
elif x < 5:
    print('x is less than 5')
else:
    print('x is 5')

# challenge
# guests must be at least 18 yrs old
#  guests must not be older than 60
# max guests in club is 200

current_guests = 190
age = int(input('How old are you? '))
min_age = 18
max_age = 60
max_guests = 200

# If the guest is allowed to enter, print a message saying, "Welcome to Berghain!"
# If the guest is not allowed to enter due to age restrictions, print a message saying, "Sorry, you cannot enter the club due to age restrictions."
# If the guest is not allowed to enter due to the club being at maximum capacity, print a message saying, "Sorry, the club is at maximum capacity. Please try again later."

can_enter = (min_age <= age <= max_age) and (current_guests < max_guests)

if can_enter:
    print("Welcome to Berghain!")
elif age < min_age or age > max_age:
    print("Sorry, you cannot enter the club due to age restrictions.")
elif current_guests > max_guests:
    print("Sorry, the club is at maximum capacity. Please try again later.")
else:
    print('Sorry, not tonight')

# Monthy savings plan

# Prompt the user for their current age.
# Prompt the user for their target retirement age.
# Prompt the user for their desired savings amount at retirement.
# Prompt the user for the annual interest rate on their savings.
# Calculate the number of years left until retirement.
# Calculate the total number of months left until retirement.
# Determine the ideal monthly savings amount based on the desired savings, the number of months left until retirement, and the interest rate.
# Display the ideal monthly savings amount to the user.

age = int(input('What is your current age? '))
retirement_age = int(input('What is your target retirement age: '))
desired_savings = float(input('Enter your desired retirement savings: '))
interest_rate = float(input('Enter annual interest rate: '))

yrs_to_retirement = retirement_age - age
mnths_to_retirment = yrs_to_retirement * 12

# monthly_savings = (desired_savings * monthly_interest_rate) / ((1 + monthly_interest_rate) ** months_until_retirement - 1)
monthly_interest_rate = (1 + interest_rate/100) ** (1/12) - 1

monthly_savings = (desired_savings * monthly_interest_rate) / \
    ((1+monthly_interest_rate) ** mnths_to_retirment - 1)

print(f'ideal monthly savings: ${monthly_savings:.2f}')
