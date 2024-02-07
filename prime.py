def check_prime(n):
    if n<=1:
        return False
    

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
           
    return True

n=int(input("enter a number:"))
if check_prime(n):
    print("the number is prime:")
else:
    print("the number is not a prime:")