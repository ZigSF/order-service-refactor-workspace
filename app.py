from pricing import calculate_total_price
from discounts import apply_discount
from utils import load_sample_orders

def main():
    orders = load_sample_orders()

    results = []

    for order in orders:
        total = calculate_total_price(order["items"], order["tax_rate"])

        # feature flag placeholder (real-world smell)
        if order.get("apply_discount"):
            total = apply_discount(total, order.get("discount_code"))

        results.append({
            "order_id": order["id"],
            "total": total
        })

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
