x=eval(input("Enter any number:"))
if (x%400==0 or x%4==0 and x%100!=0):
      print("Leap year")
else:
     print("NOT leap year")
