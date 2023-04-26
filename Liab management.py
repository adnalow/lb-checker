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
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            if len(parts) != 2:
                continue
            name, price = parts
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
                'elo': 'gelo.txt',
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

 

 
with open('gelo.txt', 'r') as file1:
                    liab1 = file1.read()

                    with open('liabilities.txt', 'r') as file2:
                        liab2 = file2.read()

                        liab_all = liab1 + liab2
                        print(liab_all)
                

def liab_admin(self):
        liabilities = {} # Load current liabilities from file
        with open('liabs_of_users/liabilities.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(':')
                if len(parts) != 2:
                    continue
                name, price = parts
                if not price.isdigit():
                    continue
                liabilities[name] = int(price)

        while True:
            print("\nWhat do you want to do?")
            print("[1] Add liability")
            print("[2] Remove liability")
            print("[3] Assign liability to a specific user")
            print("[4] Remove liability to a specific user")
            print("[5] Back")

            option = input("\nYour Choice: ")

            if option == '1':
                liab_name = input("\nInput the name of liability: ")
                liab_price = input("Price: ")
                price = int(liab_price)
                liabilities[liab_name] = price
                with open('liabs_of_users/liabilities.txt', 'a') as f:
                    f.write(f"{liab_name}:{price}\n")
                print(f"\n{liab_name} has been added with price {price}.")

            elif option == '2':
                while True:
                    with open('liabs_of_users/liabilities.txt', 'r') as f:
                        file_contents = f.read()
                        if len(file_contents) != 0:
                            print("\nWhich liability you want to remove?")
                            for i, name in enumerate(liabilities):
                                print(f"[{i+1}] {name}: {liabilities[name]}")

                            option_1 = input("\nInput the number of the liability you want to remove, or type 0 to cancel: ")

                            if option_1 == '0':
                                break

                            elif option_1.isdigit() and 1 <= int(option_1) <= len(liabilities): #Should display None or No Liabilities
                                index = int(option_1) - 1
                                name = list(liabilities.keys())[index]
                                del liabilities[name]

                                with open('liabs_of_users/liabilities.txt', 'w') as f:
                                    for name, price in liabilities.items():
                                        f.write(f"{name}:{price}\n")

                                print(f"\n{name} has been removed.")
                                break

                            else:
                                print("\nInvalid input! Please try again!")
                                continue
                        else:
                            print("\nNo liabilities")
                            print("[Back]") 

                            option_2= input("\nYour Choice: ")

                            if option_2 == "Back":
                                break
                            
                            else:
                                print("\nInvalid choice. Please try again!")
                                continue

            elif option == '3':
                while True:
                    print("\nWhich user do you want to assign a liability to?")
                    option_1 = input("Insert his/her username: ")
                    
                    # dictionary that maps usernames to filenames
                    file_dict = {'Mochu': 'liabs_of_users/mochu.txt',
                                'Russel': 'liabs_of_users/russel.txt',
                                'Gian': 'liabs_of_users/gian.txt',
                                'Luna': 'liabs_of_users/luna.txt',}
                
                    if option_1 in file_dict: # check if the entered username is in the dictionary
                        liab_name = input("Input the name of liability: ")
                        liab_price = input("Price: ")
                        price = int(liab_price)
                        liabilities[liab_name] = price

                        with open(file_dict[option_1], 'a') as f:
                            f.write(f"{liab_name}:{price}\n")
                        print(f"\n{liab_name} has been added with price {price}.")
                        break

                    else:
                        print("\nInvalid username! Please try again!")
                        continue

            elif option == '4':
                username_to_file = {
                    'Russel': 'liabs_of_users/russel.txt',
                    'Mochu': 'liabs_of_users/mochu.txt',
                    'Gian': 'liabs_of_users/gian.txt',
                    'Luna': 'liabs_of_users/luna.txt',
                }
                            
                while True:
                    option_1 = input("\nEnter the username of the person from whom you want to remove a liability: ")
                    filename = username_to_file.get(option_1)

                    if filename:
                        with open(filename, 'r') as file1:
                            liab1 = file1.read().strip()

                        if not liab1:
                            print("\nNo liabilities")
                            print("[Back]") 

                            option_2 = input("\nYour Choice: ")

                            if option_2 == "Back":
                                break
                            
                            else:
                                print("\nInvalid choice. Please try again!")
                                continue

                        with open('liabs_of_users/liabilities.txt', 'r') as file2:
                            liab2 = file2.read()

                        liab_all = liab1 + liab2

                        liab_list = liab_all.split('\n')  # convert to list of liabilities

                        print("\nThe following liabilities are currently listed:")

                        for i, liab in enumerate(liab_list):
                            print(f"[{i+1}] {liab}")

                        item_number = int(input("\nEnter the corresponding number of the liability you want to remove: "))

                        try:
                            item_to_remove = liab_list[item_number-1]  # get the specified item

                        except IndexError:
                            print("\nInvalid input! Please try again!")
                            return  # exit the function if number is invalid

                        liab_list.remove(item_to_remove)  # remove the specified item

                        liab_all = '\n'.join(liab_list)  # convert back to string

                        with open(filename, 'w') as file1:
                            file1.write(liab_all)

                        with open('liabs_of_users/liabilities.txt', 'w') as file2:
                            file2.write(liab_all)

                        print(f"\n{item_to_remove} removed successfully.")
                        break

                    else:
                        print("\nInvalid username!")
                        continue

            elif option == '5':
                print("\nExiting liability admin...")
                break

            else:
                print("\nInvalid input! Please try again")
                continue

    def options(self):
        print("\n[1] Make an Announcement")
        print("[2] Add/Remove Liabilities")
        print("[3] View Attendance")
        print("[4] Log out")

 def reg_liab(self, username):
        filename = user_liabs.get(username)

        if filename:
            with open(filename, 'r') as file1:
                liab1 = file1.read()

            with open('liabs_of_users/liabilities.txt', 'r') as file2:
                liab2 = file2.read()

            liab_all = liab1 + liab2

            liab_list = liab_all.split('\n')  # convert to list of liabilities

            if any(liab_list):
                print("\nThe following liabilities are currently listed:")
                for i, liab in enumerate(liab_list):
                    print(f"{i+1}. {liab}")
            else:
                print("\nNo liabilities")
 