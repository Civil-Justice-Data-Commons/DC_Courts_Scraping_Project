# Made this out of boredom; seems to work, if a bit simplistic.
# Also used in testing for usage with Github re: CJDC project.

# Importing random for computer to make decision.
import random

# Defining the possible actions.
action = ['rock', 'paper', 'scissors']

# Adding scores to track
CompScore = 0
UserScore = 0

# Initialize string for playing again.
play_again = 'n'
continuing = True

# Introduction statement.
print('Rock, paper, scissor showdown! Best two out of three! FIGHT!')

# The actual game, in a while-loop
while continuing is True:
    while CompScore < 2 and UserScore < 2:
        # Asking the user for their choice of weapon.
        user_choice = input('\nRock, paper, scissors? ').lower()
        while user_choice not in action:
            print('Please only input rock, paper, or scissors.')
            user_choice = input('Rock, paper, scissors? ').lower()

        # Computer makes its choice.
        computer_choice = random.choice(action)

        # Determine the winner and print corresponding statement.
        if user_choice == computer_choice:
            print(f'Computer chose {computer_choice}, and you chose {user_choice}. It\'s a tie!')
        elif user_choice == 'rock':
            if computer_choice == 'scissors':
                print(f'Computer chose {computer_choice}, and you chose {user_choice}; you win!')
                UserScore += 1
            else:
                print(f'Computer chose {computer_choice}, and you chose {user_choice}; you lose.')
                CompScore += 1
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print(f'Computer chose {computer_choice}, and you chose {user_choice}; you win!')
                UserScore += 1
            else:
                print(f'Computer chose {computer_choice}, and you chose {user_choice}; you lose.')
                CompScore += 1
        elif user_choice == 'scissors':
            if computer_choice == 'paper':
                print(f'Computer chose {computer_choice}, and you chose {user_choice}; you win!')
                UserScore += 1
            else:
                print(f'Computer chose {computer_choice}, and you chose {user_choice}; you lose.')
                CompScore += 1

        # Displaying scores
        print('')
        print(f'Your score: {UserScore}')
        print(f'Computer score: {CompScore}')

    # Print corresponding statement depending upon the final scores.
    if UserScore > CompScore:
        print('Well done, you have outsmarted a computer.')
    else:
        print('The computer wins. SkyNet is inevitable.')

    # Taking input for continuing and ending game; if continuing, resets scores.
    # Also ensures user only puts in 'y' or 'n' as input.
    play_again = input('Play again (y/n)? ').lower()
    while play_again != 'n' and play_again != 'y':
        play_again = input('Please enter y/n. Play again (y/n)? ').lower()

    # Asking player if they want to play another game (i.e., go through the loop again)
    if play_again == 'n' or play_again == 'no':
        continuing = False
    else:
        UserScore = 0
        CompScore = 0
print('\nGoodbye!')