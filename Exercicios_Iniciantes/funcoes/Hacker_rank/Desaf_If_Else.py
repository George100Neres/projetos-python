
# Given an integer, n perform the following conditional actions:

# if n is odd, print Weird
# if n is even and in the inclusive range of 2 to 5 print.Not Weird
# if n is even and in the inclusive range of 6 to 20 print Weird
#if in is even greater 20 print Not Weird

# Input Format
#A single line containing a positive integer, n

#Constraints

#1 <= n <= 100

# Output Format

if (n%2 != 0) or (n>=6 and n=20):
    print("Weird")
else:
    print("Not Weird")
