height=input("Enter your height\n")
weight=input("Enter your weight\n")
height_as_float=float(height)
weight_as_float=float(weight)
bmi_as_int=int(weight_as_float/(height_as_float**2.0))
BMI=str(bmi_as_int)
print("Your BMI is "+BMI)
if bmi_as_int<18 :
    print("You are underweight")
elif bmi_as_int<25 :
    print("You are normal weight")
elif bmi_as_int<30 :
    print("You are overweight")
elif bmi_as_int<35 :
    print("You are obese")
else :
    print("You are clinically obese")
