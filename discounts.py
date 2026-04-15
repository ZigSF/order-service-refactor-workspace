DISCOUNT_RATES = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
    "VIP": 0.30,
}


def apply_discount(total, code):
    if code is None or code not in DISCOUNT_RATES:
        return total

    discount_rate = DISCOUNT_RATES[code]
    return round(total * (1 - discount_rate), 2)
