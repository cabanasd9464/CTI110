# Meal, Tip, and Tax Calculator
# CTI-110
# P3HW2 - MealTipTax
# Drake Cabanas
# February 26, 2019

# Input the cost of the meal
# Determine tip percentage to use and ensure it is acceptable
# Calculate the tip and tax
# Display tip, tax, and total

# Input the cost of the meal
meal_cost = float(input('Enter the cost of the meal before tip in dollars: '))
tax_rate = 0.07
tax = meal_cost * tax_rate

#Determine tip percentages, calculate the tip, display amounts
tip_amount = float((input('How much would you like to tip: 15%?, 18%?, or 20%? Enter as a number. ')))
if (tip_amount == 15):
    tip = (meal_cost * tip_amount / 100)
    total_meal_cost = (meal_cost + tip + tax)
    print( 'Your tip is, $',(format(tip,',.2f')), ', your tax is, $',(format(tax,',.2f')), ', and your total cost is $',(format(total_meal_cost,',.2f')),  sep='')
elif (tip_amount == 18):
    total_meal_cost = (meal_cost + (meal_cost * (tip_amount / 100)) + (tax))
    tip = (meal_cost * tip_amount / 100)
    print( 'Your tip is, $',(format(tip,',.2f')), ', your tax is, $',(format(tax,',.2f')), ', and your total cost is $',(format(total_meal_cost,',.2f')),  sep='')
elif (tip_amount == 20):
    total_meal_cost = (meal_cost + (meal_cost * (tip_amount / 100)) + (tax))
    tip = (meal_cost * tip_amount / 100)
    print( 'Your tip is, $',(format(tip,',.2f')), ', your tax is, $',(format(tax,',.2f')), ', and your total cost is $',(format(total_meal_cost,',.2f')),  sep='')
else:
    print( 'The amount you chose to tip is not valid. Please try again')

    

      
