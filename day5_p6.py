import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print('Welcome to the Password Genenrator!')
nr_letters=int(input('How Many letters whould you like your password!\n'))
nr_numbers=int(input('How Many numbers you like your password!\n'))
nr_symbols=int(input('How Many symbols you like your password!\n'))

password=[]
for char in range(1,nr_letters+1):
    # password.append(random.choice(letter))
    password+=random.choice(letter)


for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)

for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)

random.shuffle(password)

password_list=''
for char in password:
    password_list+=char

print(f'your password is: {password_list}')