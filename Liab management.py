def liab_admin():
    while True:
        print("Select an option:")
        print("1. Add liability")
        print("2. Remove liability")
        print("3. Exit")
        option = input("What do you want to do? ")

        if option == '1':
            liab_name = input("What's the name of the liability? ")
            liab_list_name.append(liab_name)
            liab_price = input("Price: ")
            price = int(liab_price)
            liab_list_price.append(price)
            print(f"{liab_name} has been added with price {price}.")

        elif option == '2':
            print("Which liability do you want to remove?")
            for i in range(len(liab_list_name)):
                print(f"[{i+1}] {liab_list_name[i]} {liab_list_price[i] if i < len(liab_list_price) else ''}")
            option_1 = input("Type the number of the liability you want to remove, or type 0 to cancel: ")
            if option_1 == '0':
                continue
            elif option_1.isdigit() and 1 <= int(option_1) <= len(liab_list_name):
                index = int(option_1) - 1
                del liab_list_name[index]
                del liab_list_price[index]
                print(f"The liability has been removed.")
            else:
                print("Invalid input.")

        elif option == '3':
            print("Exiting liability admin...")
            break

        else:
            print("Invalid input.")

    print("Liabilities:")
    for i in range(len(liab_list_name)):
        print(f"[{i+1}] {liab_list_name[i]} {liab_list_price[i] if i < len(liab_list_price) else ''}")
    print("Goodbye!")

    liab_admin()
