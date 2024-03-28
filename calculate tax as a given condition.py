def calculate_tax(income):
    if income <= 150000:
        return 0
    elif income <= 300000:
        return (income - 150000) * 0.1
    elif income <= 500000:
        return 15000 + (income - 300000) * 0.2
    else:
        return 45000 + (income - 500000) * 0.3


income = float(input("Enter the income: "))


tax = calculate_tax(income)

print("Tax to be paid:", tax)
