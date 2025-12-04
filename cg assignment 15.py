def is_palindrome(text):
    # Convert to lowercase and remove spaces
    text = text.lower().replace(" ", "")

    # Check if the text reads the same forward and backward
    return text == text[::-1]


# --- Main Program ---
word_or_phrase = input("Enter a word or phrase: ")
result = is_palindrome(word_or_phrase)

print("Is it a palindrome?:", result)