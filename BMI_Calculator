#bmi = weight / height * height 
#If BMI is under 18.5 (not including), print "underweight"
#If 18.5 - 25 (not including), print "normal weight"
#If 25 or 30 (not including), print "overweight"
#If 30 or over, print "obese"
#Check answer, weight = 80kg, height = 1.85m gives a bmi of 23.37 (normal weight)

print("Welcome to the BMI calculator.")
weight = float(input("What is your weight in kilograms (kg)?\n"))
height = float(input("What is your height in meters (m)?\n"))

#Round to 2 decimal places: str(round(answer, 2))

bmi = float(round(weight / height ** 2, 2))

if bmi >= 18.5:
  print(f"Your BMI is {bmi}. You are normal weight.")

elif bmi >= 25:
  print(f"Your BMI is {bmi}. You are overweight.")

elif bmi >= 30: 
  print(f"Your BMI is {bmi}. You are obese.")

else: 
  print(f"Your BMI is {bmi}. You are underweight.")
