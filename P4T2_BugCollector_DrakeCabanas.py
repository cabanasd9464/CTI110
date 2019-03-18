# Tallying the total number of bugs a collecter finds every day for multiple days
# March 18, 2019
# CTI-110 P4T2 - Bug Collecter
# Drake Cabanas
#

# Set the accumulator value
total = 0

# Get the number of bugs collected for each day.
for day in range (1, 8):
    # Prompt the user to enter data.
    print('Enter the number of bugs collected on day', day)
    # Input the number of bugs collected.
    bugs = int(input())
    # Add bugs to total. 
    total += bugs
    
# Display the total bugs collected.
print ('You collected a total of', total, 'bugs.')
