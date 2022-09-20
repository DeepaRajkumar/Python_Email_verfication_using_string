#g@g.in
email=input("Enter your Email:")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            #g@g..in (example email id)
            #if we use and in this case -4,-3 will be true
            #if we use or in this case -4,-3 will be true
            #if we use xor  in this case only one dot is allowed
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong Email id,please enter valid email id")
                else:
                    print("Correct email id")
            else:
                print("wrong Email id,please enter valid email id")
        else:
            print("wrong Email id,please enter valid email id")
    else:
        print("wrong Email id,please enter valid email id")

else:
    print("wrong Email id,please enter vaild email id")













