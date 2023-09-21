amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    coin = input("Insert Coin: ").strip()
    if coin in ["25", "10", "5"]:
        amount_due -= int(coin)
    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
        break
