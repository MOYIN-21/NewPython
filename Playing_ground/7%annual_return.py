principal = 1000  # Original amount invested
rate = 0.07  # Annual rate of return
years = [10, 20, 30]  # Number of years

for n in years:
    amount = principal * (1 + rate) ** n
    print(f"After {n} years, you'll have ${amount:.2f}")
