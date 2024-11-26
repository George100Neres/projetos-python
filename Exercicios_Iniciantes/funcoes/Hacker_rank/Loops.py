
# Task

#Read an integer N, for all non-negative integers i < N, print i2. See sample for details

#Input Format

# The Fist and only contains the integer N.

# Contraints 
#1 <= N <= 20

N = int(input())

# Itera sobre todos os inteiros não negativois menores que N

for i in range(N):
     # Imprime o quadrado de i 
    print(i * i)
