import time
import random

puzzles = [
    {
        'type': 'riddle',
        'question': 'What has keys but can\'t open locks?',
        'solution': 'piano',
        'story': 'You find a hidden key inside the piano that opens a secret door.'
    },
    {
        'type': 'code',
        'question': 'Decrypt this message: "Wklv phvvdjh lv hqfubswhg xvlqj Fdhvdu flskhu."',
        'solution': 'This message is encrypted using Caesar cipher',
        'story': 'The decrypted message reveals a clue about a hidden safe in Mr. White\'s office.'
    },
    {
        'type': 'pattern',
        'question': 'What comes next in the sequence? 2, 4, 8, 16, ...',
        'solution': '32',
        'story': 'Entering the correct number into a keypad unlocks a mysterious box containing a crucial piece of evidence.'
    },
    {
        'type': 'riddle',
        'question': 'What has a head, a tail, but does not have a body?',
        'solution': 'coin',
        'story': 'You find an old coin which reveals the year when the mansion was built.'
    },
    {
        'type': 'code',
        'question': 'Decrypt this message using the reversed alphabet: "Gsv xzhrmt yvhg zm gsv xlnnkzmzoob."',
        'solution': 'The secret lies at the mysterious door',
        'story': 'A mysterious door is discovered, leading to a hidden room.'
    },
    {
        'type': 'pattern',
        'question': 'What comes next in the sequence? 1, 1, 2, 3, 5, ...',
        'solution': '8',
        'story': 'The correct number reveals the number of steps to take in a secret passage.'
    },
    {
        'type': 'riddle',
        'question': 'What is always in front of you but can’t be seen?',
        'solution': 'future',
        'story': 'A painting of Mr. White reveals a hidden message about his plans.'
    },
    {
        'type': 'code',
        'question': 'Decode this Morse code: ".- / --. .... --- ... -"',
        'solution': 'A ghost',
        'story': 'A hidden diary tells a story about a ghost haunting the mansion.'
    },
    {
        'type': 'pattern',
        'question': 'What comes next in the sequence? 3, 6, 12, 24, ...',
        'solution': '48',
        'story': 'Entering the correct number into a lock reveals a hidden chamber.'
    },
    {
        'type': 'riddle',
        'question': 'What can you hold in your left hand but not in your right?',
        'solution': 'your right elbow',
        'story': 'Discovering a hidden lever shaped like an elbow, you open a secret compartment.'
    }
]


def welcome():
    print("Welcome to the Story-driven Virtual Escape Room!")
    print("You are a detective trying to solve a mysterious disappearance.")
    print("A wealthy businessman, Mr. White, has vanished from his mansion.")
    print("Explore the mansion, discover hidden clues, and solve puzzles to unravel the mystery and find Mr. White.")
    print("You have a limited time to complete all puzzles. Good luck!\n")


def play_puzzle(puzzle, time_limit):
    is_correct = False
    while not is_correct:
        # Get the question
        print(puzzle['question'])

        # User's answer
        user_solution = input("Please share your solution: ")

        # checking if solution is correct
        is_correct = puzzle['solution'].lower() == user_solution.lower()

        # output
        if is_correct:
            print("Correct!")
            print(f"Story: {puzzle['story']} \n")
        else:
            print(f"Incorrect! Please try again")
            time_limit -= 50

    return time_limit


def play_escape_room(time_limit):
    # Start the timer
    start_time = time.time()

    # Welcome message
    welcome()

    # shuffle the puzzle list
    random.shuffle(puzzles)
    num_puzzles = len(puzzles)
    solved_puzzles = 0

    # Iterate through the list - Play puzzle
    for puzzle in puzzles:
        time_limit = play_puzzle(puzzle, time_limit)
        solved_puzzles += 1

        # if time spent is bigger than time allowed, the game needs to stop
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Time's up! You did not finish the Escape Room Game in time")
            return
        else:
            print(f"You have {
                  round(time_limit - elapsed_time)} seconds remaining")

    # if number of puzzles solved is the same as number of puzzles
    if solved_puzzles == num_puzzles:
        print(f"Congratulations! You completed game and you had {
              round(time_limit - elapsed_time)} seconds left")


play_escape_room(300)
