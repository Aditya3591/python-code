
def prime_factors(N):
    print(f"Prime factors of {N} are:")

    # Iterate from 2 to the square root of N for efficiency
    for i in range(2, int(N**0.5) + 1):
        while N % i == 0:
            print(i)
            N = N // i

    # If N is a prime number greater than 1
    if N > 1:
        print(N)

# Get user input
number = int(input("Enter the number to find prime factors: "))
prime_factors(number)
