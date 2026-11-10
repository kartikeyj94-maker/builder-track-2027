bill = float(input("What is the bill amount? "))
tip = float(input("What tip percentage would you like to give? "))
tip_percentage = bill * (tip / 100)
total = bill + tip_percentage
print(f"The tip is {tip_percentage:.2f}")
print(f"The total is {total:.2f}")