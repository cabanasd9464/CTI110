# Determining the number of calories burned while running.
# March 18, 2019
# CTI-110 P4HW1 - Calories Burned
# Drake Cabanas


# Assign number of calories burned per minute to a variable
# Assign minutes to loop
# Determine total calories burned
# Display amount of calories burned


def main():
    #Assign number of calories burned per minute to a variable
    calories_burned = 5
    #Assign minutes run to the loop
    for minutes in (20, 35, 45):
        #Determine total calories burned
        total = calories_burned * minutes
        #Display the total number of calories burned.
        print ('If you run on a treadmill for', minutes, 'minutes you will burn', total, 'calories.')
    
        



# program start
main()
