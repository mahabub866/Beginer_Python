print('Welcome to python pizza deliveries')
print('Small Pizza price: $15')
print('Medium Pizza price: $20')
print('Large Pizza price: $25')
def pizza_size():
	guess=''
	while guess not in ['S','M','L']:
		guess=input('What size pizza do you want! S,M or L :').upper()
	return guess

size=pizza_size()
print('Pepperoni for small pizza : $2')
print('Pepperoni for medium and large pizza : $3')
def Add_Pepperoni():
        guess=''
        while guess not in ['Y','N']:
            guess=input('Do you want to Pepperoni: Y or N :').upper()
        return guess
Add_Pepperonis=Add_Pepperoni()
print('Extra cheese for any size pizza : $1')
def extra_Chees():
        guess=''
        while guess not in ['Y','N']:
            guess=input('Do you want to Chees: Y or N :').upper()
        return guess
extra_Cheess=extra_Chees()
price=0
if size=='S':
    price=price+15
elif size=='M':
    price=price+20 
elif size=='L':
    price=price+25 

if Add_Pepperonis=='Y':
    if size=='S':
        price+=2
    else:
        price+=3

if extra_Cheess=='Y':
    price+=1

print(f'Your Final price is : ${price}')