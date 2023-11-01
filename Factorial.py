def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

result = factorial(5)  # Calculates 5! = 5 * 4 * 3 * 2 * 1 = 120
print(result)  # Output: 120
