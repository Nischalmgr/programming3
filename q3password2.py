'''3.Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long. '''
passw=[]
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
 
        
    