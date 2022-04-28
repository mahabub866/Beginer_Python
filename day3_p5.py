from re import L


print('Welcome to love calculator!')
name1=input('What is your name:\n')
name2=input('What is their name:\n')

combine_name=name1+name2
lowercase=combine_name.lower()

t=lowercase.count('t')
r=lowercase.count('r')
u=lowercase.count('u')
e=lowercase.count('e')
true=t+r+u+e
l=lowercase.count('l')
o=lowercase.count('o')
v=lowercase.count('v')
e=lowercase.count('e')
love=l+o+v+e

love_score=int(str(true)+str(love))

if (love_score<10) or (love_score>90):
    print(f'your love score {love_score},you like together cooking')
elif (love_score>40) or (love_score<50):
    print(f'Made for each other,score is {love_score}')
else:
    print(f'your score is {love_score}')