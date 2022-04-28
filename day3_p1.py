print('Weilcome to the rollercoaster!')
height=int(input('What is your height in cm:'))

if height>=120:
    print('You can ride rollercoaster!')
    age=int(input('What is your Age:'))
    if age<12:
        bill=5
        print('Child pay $5')
    elif age<=18:
        bill=7
        print('Youth pay $7')

    else:
        bill=12
        print('Adult Pay $12')

    def want_photo():
        guess=''
        while guess not in ['Y','N']:
            guess=input('Do you want to take Photo: Y or N :').upper()
        return guess
    want_photos=want_photo()
    if want_photos=='Y':
        bill+=3
    print(f'Your final Bill is: {bill}')
   

else:
    print('Sorry, you cant first you grow up than ride please')