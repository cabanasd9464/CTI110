# Calculating a total sum of input numbers using a while loop
# March 18, 2019
# CTI-110 P4HW3 - Sum of Numbers
# Drake Cabanas

# Create total variable
# Have users input numbers
# Ensure loop ends when a negative number is input
# Total sum of input numbers
# Display sum of input numbers


def main():
    # Create variable to total numbers
    total = 0
    # Get the first number
    number = float(input('Enter the first number: '))
    # Loop ends when input number is less than 0
    while number > -1:
        # Add first number to running total
        total = total + number
        # Request additional numbers or instruct how to terminate loop
        number = float(input('Enter the next number or a negative number to quit: '))
    # Display sum
    print('The sum of all your numbers is ', total)
        
        
    






# Program start
main()
