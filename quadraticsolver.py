import math, sys

print("\nQuadratic Equation Solver")
print("=========================\n")
print("Input a:")
a = float(input())
print("\nInput b:")
b = float(input())
print("\nInput c:")
c = float(input())


x1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
x2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)

print("\nSolution(s):")
print("============")

if (x1 == x2):
  print(x1)
else:
  print(x1)
  print(x2)