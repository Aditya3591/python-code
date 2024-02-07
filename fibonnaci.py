def generate_series(num):
    fib_series=[0,1]

    while len (fib_series) <num:
        next_term=fib_series[-1]+fib_series[-2]
        fib_series.append(next_term)
    return(fib_series)
       
    


num=int(input("enter the number of terms to generate:"))

fibonaci_series=generate_series(num)

print(f"the series is:{fibonaci_series}")

    