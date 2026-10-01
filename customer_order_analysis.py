# Customer Order Analysis Using Python

customer_names = ["Alice", "Bob", "Charlie", "David", "Eva"]

customer_orders = [
    ("Alice", "Laptop", 1200.00, "Electronics"),
    ("Bob", "Smartphone", 800.00, "Electronics"),
    ("Charlie", "Headphones", 150.00, "Electronics"),
    ("David", "Shoes", 100.00, "Fashion"),
    ("Eva", "Watch", 200.00, "Fashion")
]

# Store customer orders in a dictionary
customer_order_dict = {}

for order in customer_orders:
    customer = order[0]
    product_info = (order[1], order[2], order[3])

    if customer in customer_order_dict:
        customer_order_dict[customer].append(product_info)
    else:
        customer_order_dict[customer] = [product_info]

# Map products to categories
product_category_dict = {}

for order in customer_orders:
    product = order[1]
    category = order[3]
    product_category_dict[product] = category

print("Product category mapping:")
print(product_category_dict)

# Unique product categories
unique_categories = set(product_category_dict.values())

print("\nAvailable product categories:")
for category in unique_categories:
    print(f"- {category}")

# Calculate total spending by each customer
customer_spending = {}

for order in customer_orders:
    customer = order[0]
    price = order[2]

    if customer in customer_spending:
        customer_spending[customer] += price
    else:
        customer_spending[customer] = price

print("\nTotal spending by each customer:")
for customer, total in customer_spending.items():
    print(f"- {customer}: ${total:.2f}")

# Classify customers
for customer, total in customer_spending.items():
    if total > 100:
        classification = "High-value buyer"
    elif 50 <= total <= 100:
        classification = "Moderate buyer"
    else:
        classification = "Low-value buyer"

    print(f"{customer} is classified as a {classification}.")

# Calculate revenue by product category
category_revenue = {}

for order in customer_orders:
    category = order[3]
    price = order[2]

    if category in category_revenue:
        category_revenue[category] += price
    else:
        category_revenue[category] = price

print("\nTotal revenue per product category:")
for category, revenue in category_revenue.items():
    print(f"- {category}: ${revenue:.2f}")

# Unique products
unique_products = {order[1] for order in customer_orders}

print("\nUnique products:")
for product in unique_products:
    print(f"- {product}")

# Customers who purchased electronics
electronics_customers = [
    order[0] for order in customer_orders
    if order[3] == "Electronics"
]

print("\nCustomers who purchased electronics:")
for customer in electronics_customers:
    print(f"- {customer}")

# Top three highest-spending customers
top_customers = sorted(
    customer_spending.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

print("\nTop three highest-spending customers:")
for customer, total in top_customers:
    print(f"- {customer}: ${total:.2f}")

# Customer spending summary
print("\nCustomer spending summary:")

for customer, total in customer_spending.items():
    if total > 100:
        classification = "High-value buyer"
    elif 50 <= total <= 100:
        classification = "Moderate buyer"
    else:
        classification = "Low-value buyer"

    print(
        f"{customer}: Total Spending = ${total:.2f}, "
        f"Classification = {classification}"
    )

# Customers who purchased from multiple categories
customer_categories = {}

for order in customer_orders:
    customer = order[0]
    category = order[3]

    if customer in customer_categories:
        customer_categories[customer].add(category)
    else:
        customer_categories[customer] = {category}

multiple_category_customers = [
    customer for customer, categories in customer_categories.items()
    if len(categories) > 1
]

print("\nCustomers who purchased from multiple categories:")
for customer in multiple_category_customers:
    print(f"- {customer}")

# Customers who bought both Electronics and Fashion
# Corrected: the dataset uses "Fashion", not "Clothing".
electronics_customers_set = {
    order[0] for order in customer_orders
    if order[3] == "Electronics"
}

fashion_customers_set = {
    order[0] for order in customer_orders
    if order[3] == "Fashion"
}

common_customers = electronics_customers_set & fashion_customers_set

print("\nCustomers who bought both electronics and fashion:")
for customer in common_customers:
    print(f"- {customer}")

# High-value customers
high_value_customers = [
    customer for customer, total in customer_spending.items()
    if total > 100
]

print("\nHigh-value customers:")
for customer in high_value_customers:
    print(f"- {customer}")

# Product purchase frequency
product_frequency = {}

for order in customer_orders:
    product = order[1]

    if product in product_frequency:
        product_frequency[product] += 1
    else:
        product_frequency[product] = 1

print("\nProduct purchase frequency:")
for product, count in product_frequency.items():
    print(f"- {product}: {count} time(s)")

# Most frequently purchased products
max_frequency = max(product_frequency.values())

most_frequent_products = [
    product for product, count in product_frequency.items()
    if count == max_frequency
]

print("\nMost frequently purchased product(s):")
for product in most_frequent_products:
    print(f"- {product}")

# Category-wise sales trend
print("\nCategory-wise sales trend:")

sorted_categories = sorted(
    category_revenue.items(),
    key=lambda x: x[1],
    reverse=True
)

total_revenue = sum(category_revenue.values())

for category, revenue in sorted_categories:
    share = (revenue / total_revenue) * 100
    print(f"- {category}: ${revenue:.2f} ({share:.1f}% of total revenue)")

top_category = sorted_categories[0][0]
print(f"Trend: {top_category} is the leading category by revenue.")
