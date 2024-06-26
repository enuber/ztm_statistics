#  randomization

#  used for genrating data, simulating random events, adding variety to user interfaces

# in statistical analysis, it is used for unbiased data collection, it ensures that analysis is representative of the population.


import random

# generate random float number
random_float = random.random()
print(random_float)

# gives a random number between (first, last) numbers
random_int = random.randint(1, 10)
print(random_int)

# random float within a range (star, end) so between these
random_float2 = random.uniform(1, 10)
print(random_float2)

# random from list
my_list = ['apple', 'banana', 'cherry', 'orange']
random_choice = random.choice(my_list)
print(random_choice)

# shuffle a list
my_list2 = [1, 2, 3, 4, 5]
random.shuffle(my_list2)
print(my_list2)

# choose multiple unique items, takes in the list to choose from and how many uniques to grab
random_sample = random.sample(my_list2, 3)
print(random_sample)


# Exercise
# Random Movie Picker:
# Create a list of your favorite movies
# write a program that randomly picks a movie to watch until you've seen them all.
remaining_movies = ['The Matrix', 'Inception', 'The Dark Knight',
                    'Avengers: Endgame', 'Interstellar']
watched_movies = []

while len(watched_movies) < len(remaining_movies):
    random_movie = random.choice(remaining_movies)
    if random_movie not in watched_movies:
        watched_movies.append(random_movie)

print(watched_movies)
