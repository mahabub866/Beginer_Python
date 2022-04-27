#BMI
height=float(input('Enter Your Height in feet:'))
weight=float(input('Enter Your Weight in kg:'))

meter_height=height/3.281
bmi=weight/meter_height**2
print(bmi)