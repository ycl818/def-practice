def nroot(x,y):
    return x**(1/y)
x=int(input("請輸入被開方數字: "))
y=int(input("請輸入開方數字: "))
result=nroot(x,y)
print(str(x)+"開"+str(y)+"次方為"+"{:.0f}".format(result))
