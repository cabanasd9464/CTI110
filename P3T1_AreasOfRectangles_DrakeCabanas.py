# Calculating the area of two rectangles and comparing values
# February 26, 2019
# CTI-110 P3T1 - Areas of Rectangles
# Drake Cabanas

# Input the length and width of rectangle 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the length of rectangle 1: '))

# Input the length and width of rectangle 2
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the length of rectangle 2: '))

# Calculate the area of the rectangles
area1 = length1 * width1
area2 = length2 * width2

# Determine which rectangle has a greater area
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')
