
#The year can be evenly divided by 4, is a leap, unless:
# The year can be evenly divided by 100, It is NOT a leap year, unless
# The year is also evenly divisible by 400. Then It is a leap year.

# This means that in the Gregorian calendar the years 2000 and are leap
# years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years SOurce

def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

year = int(input())