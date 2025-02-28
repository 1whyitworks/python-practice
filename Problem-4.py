# Problem 4: Factorial Calculator (Easy)
# Write a function that computes the factorial of a non-negative integer.
# You can use either loops or recursion.
# Example:
#   Input: 5
#   Output: 120

def factorial(n):
    # TODO: Return the factorial of n
    result = 1
    for i in range(1, n + 1):
        result = i * result
    return result

# Test
print(factorial(5))  # Expected output: 120
