# Ask the user to enter a single character
char = input("Enter a single character: ").lower()

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"The character '{char}' is a vowel.")
    else:
        print(f"The character '{char}' is a consonant.")
else:
    print("Invalid input! Please enter a single alphabet character.")