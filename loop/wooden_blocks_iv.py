blocks = int(input("Enter the number of blocks: "))

blocks_required = 1
height = 0

while blocks >= blocks_required:
    height += 1
    blocks -= blocks_required
    blocks_required += 1

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
