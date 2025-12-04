def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage
print(power(2, 3))  # Output: 8