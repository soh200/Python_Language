# diplaying the type of triangle
a=float(input(" enter the first side "))
b=float(input(" enter the second side "))
c=float(input(" enter the third side "))
if a==b and b==c :
    print(" the triangle is equilateral ")
elif a==b or b==c or a==c :
    print(" the triangle is isosceles ")
else:
    print(" the triangle is scelene ")

    
