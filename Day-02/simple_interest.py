principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))
si = (principal * rate * time) / 100
print("Simple Interest:", si)
print("Total Amount:", principal + si)
