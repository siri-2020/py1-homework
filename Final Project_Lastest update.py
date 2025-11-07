print("╔════════════════════════════════════════════════════╗")
print("║                    Bill Splitter                   ║")
print("╚════════════════════════════════════════════════════╝\n")

# Collect menu and prices
menu_dictionary = {}

print("Enter dish names and prices:")
print("**Press Enter on an empty line to continue**")

while True:
    dish_name = input("\nDish name: ").strip()
    if dish_name == "":
        break
    # Collect dish prices
    dish_price = -1
    while dish_price < 0:
        price_input = input("Enter price for " + dish_name \
            + " (number only): THB ").strip()

        is_valid_number = True
        decimal_count = 0
        # --- CHECK  VALID PRICE ---
        # Check if the string is empty
        if len(price_input) == 0:
            is_valid_number = False
        else:
            for character in price_input:
                if '0' <= character <= '9':
                    pass
                elif character == '.':
                    decimal_count += 1
                else:
                    is_valid_number = False
                    break

            if decimal_count > 1:
                is_valid_number = False

            # Check for inputs that are just "."
            if price_input == '.':
                is_valid_number = False

        # --- END OF CHECK PRICE ---

        if is_valid_number:
            dish_price = float(price_input)

            if dish_price < 0:
                print("Price must not be negative")
                dish_price = -1

        if not is_valid_number:
            print("\n **Please input valid price** \n")
            dish_price = -1

    # Make a dictionary
    menu_dictionary[dish_name] = dish_price

if len(menu_dictionary) == 0:
    print("No dishes entered")
else:
    # Show the entire menu
    print("\n--- Menu List (" + str(len(menu_dictionary)) \
        + " items) ---")
    for dish_name in menu_dictionary:
        dish_price = menu_dictionary[dish_name]
        print(
            dish_name + ": THB " + str(round(dish_price, 2)))

    # Collect people names
    people_list = []
    print("\nEnter people's names (one per line):")
    print("**Press Enter on an empty line to continue**")

    while True:
        person_name = input("Name: ").strip()

        if person_name == "":
            break

        if person_name in people_list:
            print(person_name + " is already in the list")
        else:
            people_list.append(person_name)

    if len(people_list) == 0:
        print("No people at this table")
    else:
        # Show all names
        print("\n--- People List (" + str(len(people_list)) \
            + " total) ---")
        for person_name in people_list:
            print("- " + person_name)

        # Collect dishes for each person
        dish_eaters_dict = {}
        for dish_name in menu_dictionary:
            dish_eaters_dict[dish_name] = []

        print("\n--- Who ate what ---")

        dish_name_list = list(menu_dictionary.keys())

        for person_name in people_list:
            print("\nWhat did " + person_name + " eat?")

            # Menu in choices
            for index in range(len(dish_name_list)):
                number_display = index + 1
                dish_name = dish_name_list[index]
                print(str(number_display) + ". " + dish_name)

            # User input dish numbers
            got_selected_dishes = False
            while not got_selected_dishes:
                prompt_text = ("Dishes for " + person_name \
                    + " (enter numbers separated by commas, " \
                    + "e.g. 1,2,3): ")
                choice_input = input(prompt_text).strip()

                if choice_input == "":
                    got_selected_dishes = True
                else:
                    number_inputs = choice_input.split(',')
                    selected_dishes = []
                    is_valid = True

                    # --- CHECK VALID DISH NUMBERS ---
                    for number_input in number_inputs:
                        number_input = number_input.strip()

                        # Check if input is a valid integer
                        is_valid_integer = True
                        if len(number_input) == 0:
                            is_valid_integer = False
                        else:
                            for character in number_input:
                                if not ('0' <= character <= '9'):
                                    is_valid_integer = False
                                    break

                        if not is_valid_integer:
                            print("\n **Please input valid answer** \n")
                            is_valid = False
                            break

                        selected_index = int(number_input) - 1

                        if (0 <= selected_index <
                                len(dish_name_list)):
                            dish_name = (dish_name_list[selected_index])
                            selected_dishes.append(dish_name)
                        else:
                            print("\n **Please input valid answer** \n")
                            is_valid = False
                            break
                    # --- END OF CHECK VALID DISH NUMBERS ---

                    if is_valid:
                        for dish_name in selected_dishes:
                            dish_eaters_dict[dish_name].append(person_name)
                        got_selected_dishes = True

        # Calculation
        print("\n" + "=" * 50)
        print("Summarized Details")
        print("=" * 50)

        person_total_dict = {}
        for person_name in people_list:
            person_total_dict[person_name] = 0.0

        for dish_name in menu_dictionary:
            dish_price = menu_dictionary[dish_name]
            eaters_list = dish_eaters_dict[dish_name]
            number_of_eaters = len(eaters_list)

            if number_of_eaters > 0:
                shared_price = dish_price / number_of_eaters

                print("\n" + dish_name + ": THB " \
                    + str(round(dish_price, 2)))

                eaters_text = ", ".join(eaters_list)
                print("  Who ate this: " + eaters_text)
                print("  Each person must pays: THB " \
                    + str(round(shared_price, 2)))

                for person_name in eaters_list:
                    person_total_dict[person_name] = ( \
                        person_total_dict[person_name] \
                        + shared_price)
            else:
                print("\n" + dish_name + ": THB " \
                    + str(round(dish_price, 2)))
                print("  No one ate this dish")

        # Result
        print("\n" + "=" * 50)
        print("Bill Split for Each Person")
        print("=" * 50)

        for person_name in people_list:
            total_price = person_total_dict[person_name]
            print(person_name + ": THB "
                + str(round(total_price, 2)))

        total_bill = sum(menu_dictionary.values())
        print("\n   Total bill: THB " + str(round(total_bill, 2)))
        print("\n" + "*" * 50)
        print("                 PLEASE PAY NA KRUB               ")