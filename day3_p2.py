height=float(input('Enter Your Height in feet:'))
weight=float(input('Enter Your Weight in kg:'))

meter_height=height/3.281
bmi=round(weight/meter_height**2)
print(bmi)
if bmi<18.5:
    print('UnderWeight')
elif  bmi>=18.5 or bmi>25:
    print('normal weight')
elif  bmi>=25 or bmi>30:
    print('overweight')
elif  bmi>=30 or bmi>35:
    print('obese')
elif  bmi>=35 :
    print('clinically obese')

