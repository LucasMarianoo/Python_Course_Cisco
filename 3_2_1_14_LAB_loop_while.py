blocks = int(input("Enter the number of blocks: "))

y = 1

# adds y+1 to y variable until it decrements user input to 0 or less

while blocks - y >= 0:
    blocks = blocks - y
    y += 1

  
height = y-1  # remove the last increment of y that 'negativate or makes the equation to 0'


print("The height of the pyramid:", height)