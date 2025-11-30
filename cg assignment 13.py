# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Process the string: remove spaces and convert to lowercase
processed_input = user_input.replace(" ", "").lower()

# Check if the string is a palindrome
if processed_input == processed_input[::-1]:
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")