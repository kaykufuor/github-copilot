# # Write code below 💖
# stock_prices = [
#     34.68,
#     36.09,
#     34.94,
#     33.97,
#     34.68,
#     35.82,
#     43.41,
#     44.29,
#     44.65,
#     53.56,
#     49.85,
#     48.71,
#     48.71,
#     49.94,
#     48.53,
#     47.03,
#     46.59,
#     48.62,
#     44.21,
#     47.21,
# ]


# def price_at(x):
#     price = stock_prices[x]
#     return price


# def max_price(a, b):
#     max_stock = max(stock_prices[a:b])
#     return max_stock


# def min_price(a, b):
#     min_stock = min(stock_prices[a:b])
#     return min_stock


# print(price_at(2))
# print(max_price(1, 20))
# print(min_price(1, 20))
# Stonks 📈
# Codédex

stock_prices = [
    34.68,
    36.09,
    34.94,
    33.97,
    34.68,
    35.82,
    43.41,
    44.29,
    44.65,
    53.56,
    49.85,
    48.71,
    48.71,
    49.94,
    48.53,
    47.03,
    46.59,
    48.62,
    44.21,
    47.21,
]


# Define a function that returns the price at a 1-based day index.
def price_at(i):
    # Convert from 1-based day number to 0-based list index and return that price.
    return stock_prices[i - 1]


# Define a function that finds the maximum price between day a and day b (inclusive).
def max_price(a, b):
    # Start with 0 as the current maximum.
    mx = 0
    # Loop through every day from a to b, including b.
    for i in range(a, b + 1):
        # Update mx if the current day's price is larger.
        mx = max(mx, price_at(i))
    # Return the highest price found in the range.
    return mx


# Define a function that finds the minimum price between day a and day b (inclusive).
def min_price(a, b):
    # Start with the first price in the range as the current minimum.
    mn = price_at(a)
    # Loop through every day from a to b, including b.
    for i in range(a, b + 1):
        # Update mn if the current day's price is smaller.
        mn = min(mn, price_at(i))
    # Return the lowest price found in the range.
    return mn


# Print the highest price from day 1 through day 15.
print(max_price(1, 15))
# Print the lowest price from day 5 through day 10.
print(min_price(5, 10))
# Print the price at day 3.
print(price_at(3))
