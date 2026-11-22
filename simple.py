principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Simple interest: {simple_interest:.2f}")
print(f"Total amount: {total_amount:.2f}")