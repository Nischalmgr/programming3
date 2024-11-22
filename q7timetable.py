'''7.Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.'''
num=int(input("enter the number from 0-12"))
if num>=0 and num <=12:
    for x in range(0,13):
        print(f"{x}* {num} =" , x*num)
else:
    print("please enter number between 0 and 12 ")