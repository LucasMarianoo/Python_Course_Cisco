income = float(input("Enter the annual income: "))

#
# Write your code here.
#
limit = int(85528)
base_tax = 14839.02

if income < limit:
    tax = (income * 0.18) - 556.02
    if tax <= 0:
        tax = 0.0
else:
    tax = ((income - limit) * 0.32) + base_tax
    
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
