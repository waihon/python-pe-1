school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    sum = 0
    counter = 0
    for score in school_class[name]:
        sum += score
        counter += 1
    average = sum / counter
    print(name, ":", average)

"""
Enter the student's name: Joe
Enter the student's score (0-10): 7
Enter the student's name: Mary
Enter the student's score (0-10): 8
Enter the student's name: Peter
Enter the student's score (0-10): 6
Enter the student's name: Joe
Enter the student's score (0-10): 5
Enter the student's name: Mary
Enter the student's score (0-10): 9
Enter the student's name: Peter
Enter the student's score (0-10): 4
Enter the student's name:
Joe : 6.0
Mary : 8.5
Peter : 5.0
"""
