blocks = int(input("Enter the number of blocks: "))

#This code calculates height of a triangle pyramid which it is
#consist of  layers have 1 more block than preceding layer


left_blocks = blocks
height = 0
while left_blocks > height:
    height += 1
    left_blocks -= height

#it ignores leftover blocks
print("The height of the pyramid:", height)
