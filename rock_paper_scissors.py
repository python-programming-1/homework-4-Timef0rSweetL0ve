# Homework 4
# Write a program that runs rock paper scissors game.

# Possible outcomes by user input and computer output
def possible_outcomes(user_input, comp_output):
    human_score = 0
    computer_score = 0
    # neutral:
    if user_input == comp_output:
        print('Same guess. Neither of you wins!')
    # user wins:
    elif (user_input == 'r' and comp_output == 's') or (user_input == 's' and comp_output == 'p') or (user_input == 'p' and comp_output == 'r'):
        print('You chose ' + inputs[user_input] + ' and the computer chose ' + inputs[comp_output] + '. You win!')
        human_score += 1       # update human score
    # computer wins:
    else:
        print('You chose ' + inputs[user_input] + ' and the computer chose ' + inputs[comp_output] + '. Computer wins!')
        computer_score += 1    # update computer score
    return human_score, computer_score    # catch both scores for global scope

# smarter computer
def move_history(user_input):
    count.setdefault(user_input, 0)                      # create a dictionary of user input as key and assign 0 as an initial value.
    count[user_input] = count[user_input] + 1            # update the value for each corresponding key (user input)
    if user_input == 'r' and count[user_input] >= 3:     # rock is the current key and its value reaches 3
        comp_output = 'p'                                # computer generates paper
    elif user_input == 'p' and count[user_input] >= 3:   # paper is the current key and its value reaches 3
        comp_output = 's'                                # computer generates scissors
    elif user_input == 's' and count[user_input] >= 3:   # scissors is the current key and its value reaches 3
        comp_output = 'r'                                # computer generates rock
    else:
        comp_output = random.choice(list(inputs.keys())) # computer randomly generates a letter r/s/p
    return comp_output

# update current score
def current_score(hscore_list, cscore_list):
    total_h = sum(hscore_list)
    total_c = sum(cscore_list)
    return total_h, total_c

import random
inputs = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
count = {}
hscore_list = []
cscore_list = []
while True:
    print('Make a move (r/s/p): ')              # prompt user to enter a value
    user_input = input()                        # catch user's entered value r/s/p
    comp_output = move_history(user_input)      # store user's history of moves and make computer smarter
    human_score, computer_score = possible_outcomes(user_input, comp_output)  # check the outcomes of both human and computer
    hscore_list.append(human_score)             # create the lists of scores for user
    cscore_list.append(computer_score)          # create the lists of scores for computer
    user_input = input()
    if user_input == 'sc':
        total_h, total_c = current_score(hscore_list, cscore_list)
        # show user total updated scores at each round
        print('Human: ' + str(total_h) + ' Computer: ' + str(total_c))
    print('Do you want to play again? (y/n)')
    play_request = input()
    if play_request == 'y':
        continue
    else:
        total_h, total_c = current_score(hscore_list, cscore_list)
        # print final scores for users and computer
        print('Thank you.\nHuman: ' + str(total_h) + '\nComputer: ' + str(total_c) + '\nSee you again!')
        break
