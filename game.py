import random 
playing = True 
mumber = str(random.randint(10 , 20)) 
print('l will generate a number from 0 to 9 and you have to guess of dight of the number') 
print('If you win the you get 1 hero') 
while playing:
    guess = input('Give me your best guess') 
    if mumber == guess:
        print('You win the game !') 
        print('The mumber was ', mumber ) 
        break 
    else:
        print('Your guess is not quite right try again') 
