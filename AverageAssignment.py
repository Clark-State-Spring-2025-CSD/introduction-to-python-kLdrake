#Print a line asking the user to enter three numbers
#Prompt the user to enter the three integers, one at a time
#Display the three numbers entered, their sum, and the average.
#You can assume the user will only enter positive integers
#Example output: (you do not have to match my words exactly)
#Please enter three whole numbers:
#Number 1: 11
#Number 2: 11
#Number 3: 12
#The sum of 11 and 11 and 12 is 34 and the average is 11.333333333333334.

print("Please enter three whole numbers below.")
a = (input("Number 1:"))
b = (input("Number 2:"))
c = (input("Number 3:"))
d = int(a)
e = int(b)
f = int(c)

# calculate the sum
aa = (d, e, f)
total = sum(aa)

# calculate the average 
average = total / 3

print("The sum of",d, "and",e, "and", f,"is",total, "and the average is", average,)