print("Weclome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 15, or 20? "))
people = int(input("How many people are you splitting the bill by? "))

tip_perct = tip / 100 
total_tip = bill * tip_perct 
total_bill = bill + total_tip
bill_per_person = total_bill / people 
final_bill = round(bill_per_person, 2)

print(f"Each person should pay: ${final_bill}")
