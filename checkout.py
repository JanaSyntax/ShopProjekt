def checkout(user, cart):
    print(f"--- Checkout ---")
    print(f"User: {user}")
    print("Cart:")
    for item in cart:
        print(f"- {item["name"]}: €{item["price"]:.2f}")
    total = sum(item["price"] for item in cart)
    print(f"Total: €{total:.2f}")

