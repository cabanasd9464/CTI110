# Converting pounds to kilograms with a loop
# March 18, 2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Drake Cabanas
#

# Define variables
# Create table headings
# Assugb pounds to table
# Convert to kilograms
# Print pounds and kilograms

def main():
    
    # This program converts pounds from 100 pounds to 300 pounds
    # in increments of 10 to kilograms
    start_weight = 100
    end_weight = 310
    increment = 10
    conversion = .4535970244

    # Print the table heading
    print('Pounds\tKilograms')
    print('-----------------')

    # Assign weight range to loop
    for Pounds in range (start_weight, end_weight, increment):
        # Calculate conversion
        Kilograms = Pounds * conversion
        # Print the table
        print(Pounds, '\t', format(Kilograms, '.2f'))
    

# Program start
main()
