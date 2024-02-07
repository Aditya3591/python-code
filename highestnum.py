def check_the_largest(num1,num2,num3):

    if num1>num2 and num1>num3:
        print(f"{num1} is the largest")
    elif num2>num1 and num2>num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest")



num1=int(input("enter the 1 number:"))
num2=int(input("enter the 2 number:"))
num3=int(input("enter the 3 number:"))

check_the_largest(num1,num2,num3)