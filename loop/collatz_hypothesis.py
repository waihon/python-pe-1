# In 1937, a German mathematician named Lothar Collatz formulated an
# intriguing hypothesis (it still remains unproven) which can be described
# in the following way:
# 1. Take any non-negative and non-zero integer number and name it c0;
# 2. If it's even, evaluate a new c0 as c0 ÷ 2;
# 3. Otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 4. If c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will
# always go to 1.

c0 = int(input("Enter any non-negative and non-zero integer: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1
else:
    print("steps =", steps)

"""
Enter any non-negative and non-zero integer: 15
46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17
"""
