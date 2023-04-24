def liab_admin():
    # Load current liabilities from file
    liabilities = {}
    with open('liabilities.txt', 'r') as f:
        for line in f:
            name, price = line.strip().split(':')
            liabilities[name] = int(price)

    # Initialize user-liability dictionary
    user_liabilities = {
        "Gab": "perez",
        "kim": "bautista",
        "elwin": "baredo",
        "gelo": "baricante",
        "gian": "gersaniba",
        "russel": "garcia",
        "james": "diola",
        "boris": "hernandez"
    }

    while True:
        print("Select an option:")
        print("1. Add liability")
        print("2. Remove liability")
        print("3. Assign liability to user")
        print("4. Exit")
        option = input("What do you want to do? ")

        if option == '1':
            liab_name = input("What's the name of the liability? ")
            liab_price = input("Price: ")
            price = int(liab_price)
            liabilities[liab_name] = price
            with open('liabilities.txt', 'a') as f:
                f.write(f"{liab_name}:{price}\n")
            print(f"{liab_name} has been added with price {price}.")

        elif option == '2':
            print("Which liability do you want to remove?")
            for i, name in enumerate(liabilities):
                print(f"[{i+1}] {name}: {liabilities[name]}")
            option_1 = input("Type the number of the liability you want to remove, or type 0 to cancel: ")
            if option_1 == '0':
                continue
            elif option_1.isdigit() and 1 <= int(option_1) <= len(liabilities):
                index = int(option_1) - 1
                name = list(liabilities.keys())[index]
                del liabilities[name]
                with open('liabilities.txt', 'w') as f:
                    for name, price in liabilities.items():
                        f.write(f"{name}:{price}\n")
                print(f"{name} has been removed.")
            else:
                print("Invalid input.")

        elif option == '3':
            print("Which user do you want to assign a liability to?")
            option_1 = input("Insert his/her username: ")
            if option_1 == 'gab':
                liab_name = input("What's the name of the liability? ")
                liab_price = input("Price: ")
                price = int(liab_price)
                liabilities[liab_name] = price
                with open('gab.txt', 'a') as f:
                    f.write(f"{liab_name}:{price}\n")
                print(f"{liab_name} has been added with price {price}.")
                    
            else:
                print("Invalid input.")
        
        elif option == '4':
            def gab_liab():
                with open('gab.txt', 'r') as file1:
                    liab1 = file1.read()

                with open('liabilities.txt', 'r') as file2:
                    liab2 = file2.read()

                    liab_all = liab1 + liab2
                    print(liab_all)
            gab_liab()
  
        elif option == '5':
            print("Exiting liability admin...")
            break

        else:
            print("Invalid input.")

    print("Goodbye!")