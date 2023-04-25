'''
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
        print("3. Assign liability to a specific user")
        print("4. Remove liability to a specific user")
        print("5. Exit")
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
            print("Which user do you want to remove a liability from?")
            option_1 = input("Insert their username: ")
            if option_1 == 'gab':
                with open('gab.txt', 'r') as file1:
                    liab1 = file1.read()

                with open('liabilities.txt', 'r') as file2:
                    liab2 = file2.read()

                liab_all = liab1 + liab2

                liab_list = liab_all.split('\n')  # convert to list of liabilities

                print("The following liabilities are currently listed:")
                for i, liab in enumerate(liab_list):
                    print(f"[{i+1}] {liab}")

                item_number = int(input("\nWhich liability do you want to remove? Enter the corresponding number: "))

                try:
                    item_to_remove = liab_list[item_number-1]  # get the specified item
                except IndexError:
                    print("Invalid input. Please enter a valid number.")
                    return  # exit the function if number is invalid

                liab_list.remove(item_to_remove)  # remove the specified item

                liab_all = '\n'.join(liab_list)  # convert back to string

                with open('gab.txt', 'w') as file1:
                    file1.write(liab_all)

                with open('liabilities.txt', 'w') as file2:
                    file2.write(liab_all)

                print(f"{item_to_remove} removed successfully.")

            else:
                print("Invalid input.")

        
        elif option == '5':
            print("Exiting liability admin...")
            break

        else:
            print("Invalid input.")

    print("Goodbye!")

'''

def liab_admin():
    # Load current liabilities from file
    liabilities = {}
    with open('liabilities.txt', 'r') as f:
        for line in f:
            name, price = line.strip().split(':', 1)
            if not price.isdigit():
                continue
            liabilities[name] = int(price)

    # Initialize user-liability dictionary
    user_liabilities = {
         'gelo': 'password456',
         'elwin': 'password456',
         'mochu': 'password456',
         'jawo': 'password456',
         'diola': 'password456',
         'russel': 'password456',
         'gian': 'password456',
         'boris': 'password456',
         'luna': 'password456',
         'gab': 'password456',
    }

    while True:
        print("Select an option:")
        print("1. Add liability")
        print("2. Remove liability")
        print("3. Assign liability to a specific user")
        print("4. Remove liability to a specific user")
        print("5. Exit")
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
            
            # dictionary that maps usernames to filenames
            file_dict = {'gelo': 'gelo.txt',
                        'elwin': 'elwin.txt',
                        'mochu': 'mochu.txt',
                        'jawo': 'jawo.txt',
                        'diola': 'diola.txt',
                        'russel': 'russel.txt',
                        'gian': 'gian.txt',
                        'boris': 'boris.txt',
                        'luna': 'luna.txt',
                        'gab': 'gab.txt'}
            
            # check if the entered username is in the dictionary
            if option_1 in file_dict:
                liab_name = input("What's the name of the liability? ")
                liab_price = input("Price: ")
                price = int(liab_price)
                liabilities[liab_name] = price
                with open(file_dict[option_1], 'a') as f:
                    f.write(f"{liab_name}:{price}\n")
                print(f"{liab_name} has been added with price {price}.")
            else:
                print("Invalid input.")

        elif option == '4':
            username_to_file = {
                'gelo': 'gelo.txt',
                'elwin': 'elwin.txt',
                'mochu': 'mochu.txt',
                'jawo': 'jawo.txt',
                'diola': 'diola.txt',
                'russel': 'russel.txt',
                'gian': 'gian.txt',
                'boris': 'boris.txt',
                'luna': 'luna.txt',
                'gab': 'gab.txt'
         }
            print("Which user do you want to remove a liability from?")
            option_1 = input("Insert their username: ")
            filename = username_to_file.get(option_1)
            if filename:
                with open(filename, 'r') as file1:
                    liab1 = file1.read()

                with open('liabilities.txt', 'r') as file2:
                    liab2 = file2.read()

                liab_all = liab1 + liab2

                liab_list = liab_all.split('\n')  # convert to list of liabilities

                print("The following liabilities are currently listed:")
                for i, liab in enumerate(liab_list):
                    print(f"[{i+1}] {liab}")

                item_number = int(input("\nWhich liability do you want to remove? Enter the corresponding number: "))

                try:
                    item_to_remove = liab_list[item_number-1]  # get the specified item
                except IndexError:
                    print("Invalid input. Please enter a valid number.")
                    return  # exit the function if number is invalid

                liab_list.remove(item_to_remove)  # remove the specified item

                liab_all = '\n'.join(liab_list)  # convert back to string

                with open(filename, 'w') as file1:
                    file1.write(liab_all)

                with open('liabilities.txt', 'w') as file2:
                    file2.write(liab_all)

                print(f"{item_to_remove} removed successfully.")
            else:
                print("Invalid username.")

        elif option == '5':
            print("Exiting liability admin...")
            break

        else:
            print("Invalid input.")

    print("Goodbye!")

 

 