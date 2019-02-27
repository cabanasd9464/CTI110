# Calculating secondary colors from primary color combinations
# CTI-110 P3HW1 - Color Mixer
# Drake Cabanas
# February 26, 2019


# Input the primary colors chosen to mix
# Calculate and display the secondary color created
# Ensure only primary are chosen

# Input primary colors
color1 = input('Enter the first primary color to mix: ')
color2 = input('Enter the second primary color to mix: ')

#Calculate the secondary colors created and display the secondary color created
if (color1 == 'blue' and color2 == 'red') or (color1 == 'red' and color2 == 'blue'):
    print(color1 + " mixed with "  + color2 + " is purple " )
elif(color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
    print(color1 + " mixed with "  + color2 + " is orange " )
elif(color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
    print(color1 + " mixed with "  + color2 + " is green " )
    
#Ensure only primary colors are mixed
else:
    print( "One of your colors to combine, " + color1 + " or " + color2 + ", is not a primary color. Please try again." )
    
