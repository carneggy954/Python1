# Prompt the user to enter the number of rows
rows = int(input("Enter the number of rows for the pattern: "))

# Check if the input is valid
if rows <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    print("Right-angled triangle pattern:")
    # Generate the pattern
    for i in range(1, rows + 1):
        print("*" * i)