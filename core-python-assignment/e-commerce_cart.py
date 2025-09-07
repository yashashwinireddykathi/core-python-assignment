def ecommerce():
    cart_items={'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
    s=0
    for i in cart_items.values():
        s=s+i
    if len(cart_items) == 0:
        print("Cart is empty.")
    else:
        if len(cart_items) <= 5:
            print("Total Price:", s)
        else:
            print("Total Price:", int(s * 0.9))

ecommerce()