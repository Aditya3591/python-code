def check_perfect_num(n):
    sum=0
    if n<=0:
        print("invalid number")

    
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return (sum)

n=int(input("enter a number:"))
perfect_num=check_perfect_num(n)
if perfect_num==n:
    print("it is a perfect number")
else:
    print("not a perfect number")

