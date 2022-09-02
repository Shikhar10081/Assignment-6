print("Enter value of A & B & C :")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
     print("real and distinct roots")

elif d==0:
     print("Real and equal roots")
else:
    print("Img root")
