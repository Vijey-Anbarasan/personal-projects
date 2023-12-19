print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? Rs."))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# if(tip_percentage==10):
#     percentage = total_bill * 0.10
# elif(tip_percentage==12):
#     percentage = total_bill * 0.12
# else:
#     percentage = total_bill * 0.15
# tipped_bill = total_bill+percentage

tipped_bill = total_bill + (total_bill * (tip_percentage/100))
print(f"Tipped Bill: {tipped_bill}")
split_between = float(input("How many people to split the bill? "))
payment = float(tipped_bill/split_between)
bill_after_split = round(payment,2)
print(f"Each person should pay : Rs{bill_after_split}")