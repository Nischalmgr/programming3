'''Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''
passw=[]
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
for pww in BAD_PASSWORDS:
    passw.append(pww)
# print(passw)
while True:
     pw=input("enter a new password ")
     conform=input("reenter the password ")
     if len(pw)>=8 and len(pw)<12:
        
        if pw!=conform:
            print("the password doesnot match")
        else:
            if pw not in  passw:
               passw.append(pw)
               print("password set")
               break;
            else: 
               print("re enter another password")
     else:
        print("please enter password between 8-12 character")
 
        
     
    
 
    
    
        
    