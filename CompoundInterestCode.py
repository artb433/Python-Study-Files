# TODO: THE CODE BELOW CALCULATES COMPOUND INTEREST BY TAKING THE INVESTED AMOUNT, INTEREST RATE AND NUMBER OF YEARS
money = input("Enter your investment amount: ")
money = float(money)
interest_rate = input("Enter the interest rate without percentage: ")
interest_rate = float(interest_rate) / 100
number_of_years = input("Enter the number of years without decimals: ")
number_of_years = int(number_of_years)
for i in range(number_of_years):
    money = money + (money * interest_rate)
print("Your expected return after 10years is: {:.2f}".format(money))
