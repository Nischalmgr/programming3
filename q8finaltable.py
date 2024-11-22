'''8.Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "
-7"
would produce the Seven Times Table starting at "12 times" down to "0 times"
.'''
num=int(input("enter the number from 0-12"))
if num>=0 and num <=12:
    for x in range(0,13):
        print(f"{x}* {num} =" , x*num)
elif num<0:
     num=abs(num) 
      
     if num<=12:
        for x in range(12,-1,-1):
            print(f"{x}* {num} =" , x*num)
     else: print("please enter number between 0 and 12 ")

else:
    print("please enter number between 0 and 12 ")