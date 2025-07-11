store = {}

while True:
    print("\n=== Product Options ===")
    print("1. Add a product")
    print("2. Change product price")
    print("3. Search products by price range")
    print("4. Show all products")
    print("5. Quit")

    option = input("Choose an option (1-5): ")

    if option == "1":
        item = input("Enter new product name: ")
        if item in store:
            print("This product already exists.")
        else:
            cost = float(input("Enter product price: "))
            store[item] = cost
            print("Product successfully added.")

    elif option == "2":
        item = input("Enter product name to modify: ")
        if item in store:
            new_cost = float(input("Enter updated price: "))
            store[item] = new_cost
            print("Price updated successfully.")
        else:
            print("No product found with that name.")

    elif option == "3":
        low = float(input("Minimum price: "))
        high = float(input("Maximum price: "))
        print(f"Products priced between {low} and {high}:")
        found = False
        for item, cost in store.items():
            if low <= cost <= high:
                print(f"{item}: {cost}")
                found = True
        if not found:
            print("No products found in that range.")

    elif option == "4":
        if store:
            print("Current Product List:")
            for item, cost in store.items():
                print(f"{item}: {cost}")
        else:
            print("No products in the store yet.")

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")
