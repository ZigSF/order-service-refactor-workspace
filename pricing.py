def calculate_total_price(items, tax_rate):
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    return total + (total * tax_rate)
