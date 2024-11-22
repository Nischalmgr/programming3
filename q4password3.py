'''4.Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD
_
PASSWORDS = ['password''letmein'sesame'
'hello',,,'justinbieber']'''
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
            else: 
               print("re enter another password")
     else:
        print("please enter password between 8-12 character")
 
        
     
    
 
    
    
        
    