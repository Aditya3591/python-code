def check_odd_even(num):
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

try:
    num=int(input("enter a number:"))
    check_odd_even(num)
except ValueError:
    print("invalid input")
