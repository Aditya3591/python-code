def quotient_remainder(dividend,divisor):
    quotient=dividend//divisor
    remainder=dividend%divisor
    return quotient, remainder


dividend=int(input("enter the dividend:"))
divisor=int(input("enter the divisor:"))

quotient,remainder=quotient_remainder(dividend,divisor)

print(f"quotient is:{quotient}")
print(f"remainder is:{remainder}")

