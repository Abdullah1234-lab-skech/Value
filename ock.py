import random 
while True:
    user_action=input('Enter a choice rock paper or scissors:') 
    possible_actions=['rock','paper','scissors'] 
    computer_action=random.choice(possible_actions) 
    print(f'You chose {user_action}, computer chose {computer_action}') 
    if user_action==computer_action:
        print(f'Both players selected {user_action}. It is a tie!') 
    elif user_action=='rock': 
        if computer_action=='scissors':
            print('rock smashes scissors! You win!')  
        else:
            print('paper covers rock! You lose.') 
    elif user_action=='scissors': 
        if computer_action=='paper':
            print('paper covers rock! You win!')  
        else:
            print('scissors cuts  paper! You lose.') 
    elif user_action=='scissors': 
        if computer_action=='paper':
            print('scissors cuts paper! You win!')  
        else:
            print('rock smashes scissors! You lose.')
    play_again=input('Play again? (y/n):')  
    if play_again != 'y': 
        break

