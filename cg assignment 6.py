# Ask the user to enter an amount in USD
usd = float(input("Enter amount in USD: "))

# Fixed exchange rate (example: 1 USD = 0.90 EUR)
exchange_rate = 0.90

# Convert USD to EUR
eur = usd * exchange_rate

# Display the result
print("Amount in EUR:", eur)