def primeTest():
    m=int(input("請輸入整數:"))
    if m<=0 or m==1:
        return print(m,"為非質數")
    elif m==2:
        return print(2,"為質數")
    else:   
        for i in range(2,m+1):
            if(m%i)==0:
                return print(m,"為非質數")
            else:
                return print(m,"為質數")
   
while True:
    primeTest()
    
    
    
    


    
