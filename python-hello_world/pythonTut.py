# for i in range(1, 21):
#     if(i % 2 != 0):
#         print("i = ", i)

# My Solution

# investment_value = float(input("Enter value for investment: "))
# interest_value = float(input("Enter value for interest: "))

# for i in range(1,11):
#     estimated_value = (interest_value + investment_value) * interest_value;
#     print("Value per year {} = {:.2f}".format(i, estimated_value))


# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment +
# their investment * the interest rate
# Print out their earnings after a 10 year period
 
# Ask for money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")
 
# Convert value to a float
money = float(money)
 
# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01
 
# Cycle through 10 years using for and range from 0 to 9
for i in range(10):
 
    # Add the current money in the account + interest earned that year
    money = money + (money * interest_rate)
 
# Output the results
print("Investment after 10 years: {:.2f}".format(money))


