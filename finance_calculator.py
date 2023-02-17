import math

# print statement that informs the user of their calculator choices and what each choice calculates.
print('''
Choose Either the 'Investment' or 'Bond' Calculator from the Menu Below:

Investment - to calculate the amount of interest you will earn on your investment.
Bond - to calculate how much you'll have to pay on a home loan.
''')

calc_choice = input("Would you like to use the 'Investment' or 'Bond' Calculator:\t").lower()

# while loop, that requires an input of investment or bond to break out the loop.
while True:

    if calc_choice == "investment" or calc_choice == "bond":
        break

    print("\nYou have made an Invalid Selection! Please try again.\n")
    calc_choice = input("Would you like to use the 'Investment' or 'Bond' Calculator:\t").lower()

# if investment is chosen, investment details are stored in variables using input functions.
# while loop requires simple or compound to break out the loop.
# using formulas, calculate simple or compound based on user choice, rounded to 2.d.p and print.
if calc_choice == "investment":
    print("\nYou Have Selected the Investment Calculator!")

    deposit = float(input("\nHow much money are you depositing (No Currency Symbols): "))
    rate = float(input("\nWhat is the interest rate on the investment e.g. for 8% enter 8: "))
    years = float(input("\nHow many years do you plan on investing: "))
    interest = input("\nWould you like to calculate 'simple' or 'compound' interest on your investment: ").lower()

    while True:

        if interest == "simple" or interest == "compound":
            break

        print("\nYou have made an invalid interest choice! Please try again.")
        interest = input("\nWould you like to calculate 'simple' or 'compound' interest on your investment: ").lower()

    if interest == "simple":
        total = round(deposit * (1 + (rate/100) * years), 2)
    else:
        total = round(deposit * math.pow(1 + rate/100, years), 2)

    actual_interest = total - deposit

    print(f'''
    The total amount accumulated: £{total}
    The total interest earned: £{actual_interest}
    ''')

# else, bond is chosen. home loan details are stored in variables using input functions.
# calculate monthly repayment using formula to 2.d.p and print.
else:
    print("\nYou Have Selected the Bond Calculator!")

    pres_val = float(input("\nWhat is the present value of the house (No Currency Symbols): "))
    rate = float(input("\nWhat is the annual interest rate on the home loan e.g. for 8% enter 8: "))
    months = float(input("\nHow many months will the loan be repaid over: "))
    monthly_interest = (rate / 100) / 12

    repayment = round((monthly_interest * pres_val) / (1 - (1 + monthly_interest) ** (-months)), 2)

    print(f"\nThe repayment each month on the home loan: £{repayment}.")
