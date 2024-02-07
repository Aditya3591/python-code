import sys

def print_powers_of_two(N):
    if not (0 <= N < 31):
        print("Please enter a valid value for N (0 <= N < 31).")
        return

    for i in range(N + 1):
        result = 2 ** i
        print(f"2^{i} = {result}")

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python power.py <N>")
else:
    try:
        N = int(sys.argv[1])
        print_powers_of_two(N)
    except ValueError:
        print("Please enter a valid integer for N.")
