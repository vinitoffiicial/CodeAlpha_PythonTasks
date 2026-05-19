# Stock Portfolio Tracker

# Step 1: Stock prices (hardcoded)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

print("Welcome to Stock Portfolio Tracker")

total_investment = 0
portfolio = []

# Safe input for number of stocks
while True:
    try:
        n = int(input("How many different stocks do you want to enter? "))
        break
    except ValueError:
        print("Please enter a valid number!")

# Step 2: Input loop
for i in range(n):
    stock = input("Enter stock name: ").upper()

    #Safe input for quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        portfolio.append((stock, quantity, price, investment))
    else:
        print("Stock not found! Skipping...")

# Step 3: Display result
print("\nPortfolio Summary:")
for item in portfolio:
    print(f"{item[0]} - Qty: {item[1]}, Price: {item[2]}, Value: {item[3]}")

print("\nTotal Investment Value:", total_investment)

# Step 4: Save to file (optional)
choice = input("\nDo you want to save to file? (yes/no): ").lower()

if choice == "yes":
    file_type = input("Save as (txt/csv): ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio\n")
            for item in portfolio:
                f.write(f"{item[0]} - Qty: {item[1]}, Price: {item[2]}, Value: {item[3]}\n")
            f.write(f"\nTotal Investment: {total_investment}")
        print("Saved to portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for item in portfolio:
                f.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
            f.write(f"\nTotal,,,{total_investment}")
        print("Saved to portfolio.csv")

    else:
        print("Invalid file type!")
