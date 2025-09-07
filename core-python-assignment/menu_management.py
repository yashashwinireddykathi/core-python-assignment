def restaurant():
    initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
    def a():
        initial_menu.append("Tacos")
    def rem():
        item_to_remove = "Salad"
        if item_to_remove in initial_menu:
            initial_menu.remove(item_to_remove)
    def find():
        check_item="Pizza"
        if check_item in initial_menu:
            print(check_item, "is available")
        else:
            print(check_item, "is not available")
    a()
    rem()
    print("Updated menu:", initial_menu)
    find()
restaurant()