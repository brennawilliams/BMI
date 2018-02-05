weight = input("What is your weight in kilograms? ")
height = input("What is your height in centimeters? ")
BMI = 703*(int(weight)/(int(height)**2))

print("Your BMI is " + str(BMI)+ ".")

if(int(BMI) <= 18):
	print("You are underweight.")
elif(int(BMI) > 18) and (int(BMI) < 26):
	print("Your weight is normal.")
elif(int(BMI) >= 26):
	print("You are overweight.")