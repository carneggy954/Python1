def is_prime(n):
    # A prime number must be greater than 1
    if n <= 1:
        return False

    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Example use:
num = int(input("Enter a positive integer: "))
print("Prime?", is_prime(num))