print('Welcome to the tip calculator.')
bill=float(input('What was the total bill:'))
def percentage_input():
	guess=''
	while guess not in ['10','12','15']:
		guess=input('What percentage tip would you like to give: 10,12 or 15 :')
	return int(guess)

percentage=percentage_input()

people=int(input('How many People to split the bill:'))

percentage_result=bill*(percentage/100)
# print(percentage_result)
bill_result=bill+percentage_result
# print(bill_result)
each_person=bill_result/people
print(f'Each person should pay: {round(each_person,2)}')