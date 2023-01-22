blocks = int(input("Enter the number of blocks: "))

height = 0
used_blocks = 0

if blocks >= 1:
    height = 1
    used_blocks = 1

while used_blocks <= blocks:
    remaining_blocks = blocks - used_blocks
    if (height + 1) <= remaining_blocks:
        height += 1
        used_blocks += height
    else:
        break
    
print("The height of the pyramid:", height)

"""
Enter the number of blocks: 6
The height of the pyramid: 3
Enter the number of blocks: 20
The height of the pyramid: 5
Enter the number of blocks: 1000
The height of the pyramid: 44
Enter the number of blocks: 2
The height of the pyramid: 1
Enter the number of blocks: 1
The height of the pyramid: 1
Enter the number of blocks: 0
The height of the pyramid: 0
"""
