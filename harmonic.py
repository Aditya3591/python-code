n=int(input("enter the nth harmonic number:"))

if n<0:
    print("invalid input")

else:

    res=0.0
    for i in range (1,n+1):
        res=res+1/i

    print(res)