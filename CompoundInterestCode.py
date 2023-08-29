# TODO: THE CODE BELOW CALCULATES COMPOUND INTEREST BY TAKING THE INVESTED AMOUNT, INTEREST RATE AND NUMBER OF YEARS
deposit = input("Enter your investment amount: ")
deposit = float(deposit)
interest_rate = input("Enter the interest rate without %: ")
interest_rate = float(interest_rate) / 100
number_of_years = input("Enter the number of years: ")
number_of_years = int(number_of_years)
for i in range(number_of_years):
    deposit = deposit + (deposit * interest_rate)
print(f"Your expected return after {number_of_years} years is: {deposit:.2f}")
