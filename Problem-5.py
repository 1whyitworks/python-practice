# Problem 5: Fibonacci Sequence Generator (Medium)
# Write a function that generates the first n numbers of the Fibonacci sequence.
# Example:
#   Input: 7
#   Output: [0, 1, 1, 2, 3, 5, 8]

def fibonacci_sequence(n):
    # TODO: Return a list with the first n Fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result

# Test
print(fibonacci_sequence(7))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
