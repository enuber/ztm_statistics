# Lists

# store mulitple items in a single variable. Ordered, mutable and can include various data types.

# list created with []

nums = [1, 2, 3, 4, 5]

mixed_list = [42, True, "this", 3.14]

# access
print(nums[0])  # 1

# slicing
# start:finish (not including the final location)
print(nums[1:4])  # [2,3,4]

# mutable
nums[0] = 100
print(nums)  # 100, 2, 3, 4, 5

# can append to a list (add too)
# append puts it at end of list
nums.append(6)

# can also add them in this way
nums = nums + [7, 8, 9]
print(nums)

# remove from list del() or pop()
del nums[0]  # deletes first item in list

# remove - put in what you want taken out, will throw an error if what is trying to be removed isn't there
nums.remove(6)  # removes the six from the list
print(nums)

last_num = nums.pop()
some_num = nums.pop(2)  # remove from a specific index
print(last_num)
print(some_num)
print(nums)


# Expense report
monthly_expenses = [1200, 1350, 1050, 1450, 1150, 900, 1220]

# compute total expenses for month
expenses = 0
for num in monthly_expenses:
    expenses += num

print(f'${expenses}')

total_expenses = sum(monthly_expenses)
print(total_expenses)
# computer avg spending for month
avg = expenses / len(monthly_expenses)
print(f'${avg:.2f}')


# fibonacci
first_num = 1
second_num = 1
fib_seq = [first_num, second_num]

while len(fib_seq) < 10:
    fib_seq.append(fib_seq[len(fib_seq)-1] + fib_seq[len(fib_seq) - 2])

print(fib_seq)
