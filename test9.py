# for task number 9
# Program to display the Fibonacci sequence up to n-th term
def fibonacci_sequence(n):
    if n <= 0:
        return 0

    fibo = [0] * (n + 1)
    fibo[1] = 1

    # Initialize result
    sm = fibo[0] + fibo[1]

    # Add remaining terms
    for ai in range(2, n + 1):
        fibo[ai] = fibo[ai - 1] + fibo[ai - 2]
        sm = sm + fibo[ai]

    return sm


print('the sum of the fibonacci numbers is', fibonacci_sequence(50))
