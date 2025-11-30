# Prompt the user to enter a positive integer
num = int(input("Enter a positive integer: "))

# Check if the input is valid
if num <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    print(f"Collatz sequence starting from {num}:")

    # Generate the Collatz sequence
    while num != 1:
        print(num, end=" -> ")
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num)  # Print the last number (1)