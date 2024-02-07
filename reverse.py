def reversed_num(num):
    r=0
    while num>0:
        d=num%10
        r=r*10+d
        num=num//10
    return r


num=int(input("enter the number to be reversed:"))

new_num=reversed_num(num)

print(f"the reversed number is:{new_num}")