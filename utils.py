def load_sample_orders():
    return [
        {
            "id": "A100",
            "apply_discount": True,
            "discount_code": "SAVE10",
            "items": [
                {"name": "keyboard", "price": 50, "quantity": 2},
                {"name": "mouse", "price": 25, "quantity": 1}
            ],
            "tax_rate": 0.08
        },
        {
            "id": "A101",
            "apply_discount": False,
            "items": [
                {"name": "monitor", "price": 200, "quantity": 1}
            ],
            "tax_rate": 0.08
        }
    ]
