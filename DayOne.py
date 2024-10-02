a = float(input("Enter first value:"))
b = int(input("Choose the options:\n1: Addition\n2: Substraction\n3: Multiplication\n4: Division\n5: Modulus\n6: Floor Division\n7: Exponential\n"))
c = float(input("Enter second value:"))
if b == 1:
    print(f"Addition of {a} and {c} is: {a+c}")
elif b == 2:
    print("Substraction of %f and %f is: %f" %(a,c,a-c))
elif b == 3: 
    print("Multiplication of {} and {} is: {}".format(a,c,a*c))
elif b == 4:
    print("Division of %f ans %f is: %f"%(a,c,a/c))
elif b == 5: 
    print(f"Modulus of {a} and {c} is: {a%c}")
elif b == 6:
    print(f"Floor division of {a} and {c} is: {a//c}")
elif b == 7: 
    print(f"Exponential of {a} to the power {c} is: {a**c}")
else:
    print("Choose the available options!")