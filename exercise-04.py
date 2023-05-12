print("Enter the lengths of three side of a triangle: ")
a = input ("input a: ")
b = input ("input b: ")
c = input ("input c: ")


if a==b==c:
    print(f"A triangle with sides of {a}, {b} & {c} is a equalateral triangle")
elif a!=b and a!=c and b!=c:
    print(f"A triangle with sides of {a}, {b} & {c} is a scalene triangle")
else:
    print(f"A triangle with sides of {a}, {b} & {c} is a isosceles triangle")