import math

print("Enter a, b, c: ")
a = int(input())
b = int(input())
c = int(input())

D = b * b - 4 * a * c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Two roots: {0} and {1}".format(root1, root2))
else:
    print("No real roots exist.")  # Adding a message for the case where no real roots exist
