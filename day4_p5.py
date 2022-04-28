import random
# paper='paper'
# rock='rock'
# scissors='scissors'
def choice():
        guess=''
        while guess not in ['0','1','2']:
            guess=input('Do you want to choose: 0 for rock 1 for paper or 2 for scissors :')
        return int(guess)
user_choice=choice()
computer_choice=random.randint(0,2)

if user_choice == computer_choice:
    print(f'This game Draw {user_choice}={computer_choice}')
elif user_choice== 0 and computer_choice==2:
    print(f'I am win {user_choice} aginast Computer {computer_choice}')
elif user_choice== 2 and computer_choice==1:
    print(f'I am win {user_choice} aginast Computer {computer_choice}')
elif user_choice== 1 and computer_choice==0:
    print(f'I am win {user_choice} aginast Computer {computer_choice}')
else:
    print(f'{user_choice} Computer {computer_choice} Win')