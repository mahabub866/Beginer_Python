number=input('Input a list of numbers: ').split()
for n in range(0,len(number)):
    number[n]=int(number[n])
# print(type(number))
for i in number:
    if i%3==0 and i%5==0:
        print('fizz buzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0:
        print('Fizz')
    else:
        print(i)