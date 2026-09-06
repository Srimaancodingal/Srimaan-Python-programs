weight = int(input("Enter your weight"))
height = int(input("Enter your height"))
BMI = weight/(height/100) ** 2
if BMI <18.4:
    print ("Underweight")
elif BMI<= 24.9:
    print ("Healhy")
elif BMI<= 29.9: 
    print ("Overweight")
else:
    print ("Obese")
