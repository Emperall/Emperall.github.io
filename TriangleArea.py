import math

print('Enter a, b, c')
a = int(input())
b = int(input())
c = int(input())
S = (a + b + c) / 2
area = math.sqrt(S * (S - a) * (S - b) * (S - c))

if a + b > c and a + c > b and b + c > a:
    print('Triangle exists')
    if a == b and b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    elif a != b and a != c and b != c:
        print('Versatile')
        print('S = ', S)
        print('Area = ', area)
else:
    print('Triangle does not exist')
