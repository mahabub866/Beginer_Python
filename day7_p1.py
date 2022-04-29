word_list=['mahabub','shamol','mak']
import random
from re import A


chosen_word=random.choice(word_list)
lives=3+len(chosen_word)

display=[]
for letter in range(len(chosen_word)):
    display+='_'

print(display)

end_of_game=False

while not end_of_game:
    guess=input('Guess a letter: ').lower()


    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter ==guess:
            display[position]=letter
        
    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives<=3:
            print(f'Your extra lives {lives} times')
        if lives==0:
             end_of_game=True
             print('You Lose')

    if '_' not in display:
        end_of_game=True
        print('You Win')

 