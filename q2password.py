'''2. Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.'''
passw=[]
while True:
    pw=input("enter a new password: ")
    conform=input("reenter the password: ")
    if pw!=conform:
        print("the password doesnot match")
    else:
        if pw not in  passw:
            passw.append(pw)
            print("password set")
        else: 
            print("reenter another password")
    

        
    