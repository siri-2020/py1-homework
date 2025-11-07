print("╔════════════════════════════════════════════════════╗")
print("║                    Bill Splitter                   ║")
print("╚════════════════════════════════════════════════════╝\n")

# เก็บชื่อเมนูและราคาของอาหาร
dish_to_price_map = {}

print("Enter dish names and prices:")
print("**Press Enter on an empty line to continue**")

while True:
    dish_item_name = input("\nDish name: ").strip()
    if dish_item_name == "":
        break
    
    # รับราคาของเมนู
    item_price_value = -1
    while item_price_value < 0:
        price_input_str = input(
            "Enter price for " + dish_item_name +
            " (number only): THB "
        ).strip()
        item_price_value = float(price_input_str)
        if item_price_value < 0:
            print("Price must not be negative")

    dish_to_price_map[dish_item_name] = item_price_value

if len(dish_to_price_map) == 0:
    print("No dishes entered")
else:
    print("")
    print("*** Menu List (" + str(len(dish_to_price_map)) +
          " items) ***")
    for item_name in dish_to_price_map:
        price_value = dish_to_price_map[item_name]
        print(item_name + ": THB " + str(round(price_value, 2)))

    diner_names_list = []
    print("\nEnter people’s names (one per line):")
    print("**Press Enter on an empty line to continue**")

    while True:
        diner_name = input("Name: ").strip()
        if diner_name == "":
            break
        if diner_name in diner_names_list:
            print(diner_name + " is already in the list")
        else:
            diner_names_list.append(diner_name)

    if len(diner_names_list) == 0:
        print("No people at this table")
    else:
        print("")
        print("*** People List (" + str(len(diner_names_list)) +
              " total) ***")
        for diner_name in diner_names_list:
            print("- " + diner_name)

        item_eaters_map = {}
        for item_name in dish_to_price_map:
            item_eaters_map[item_name] = []

        print("")
        print("*** Who ate what ***")

        item_name_list = list(dish_to_price_map.keys())

        for diner_name in diner_names_list:
            print("")
            print("What did " + diner_name + " eat?")

            for item_index in range(len(item_name_list)):
                number_display = item_index + 1
                item_name = item_name_list[item_index]
                print(str(number_display) + ". " + item_name)

            selection_complete = False
            while not selection_complete:
                prompt_text = (
                    "Dishes for " + diner_name +
                    " (enter numbers or ranges, e.g. 1,2,4-6): "
                )
                selection_input = input(prompt_text).strip()

                if selection_input == "":
                    selection_complete = True
                else:
                    input_parts = selection_input.split(',')
                    dishes_selected = []
                    is_selection_valid = True

                    for part_str in input_parts:
                        part_str = part_str.strip()

                        if '-' in part_str:
                            range_components = part_str.split('-')
                            if len(range_components) == 2:
                                start_num_str = \
                                    range_components[0].strip()
                                end_num_str = \
                                    range_components[1].strip()

                                if start_num_str.isdigit() and \
                                   end_num_str.isdigit():
                                    start_num = int(start_num_str)
                                    end_num = int(end_num_str)

                                    for dish_number in \
                                            range(start_num, end_num + 1):
                                        selected_item_index = dish_number - 1
                                        max_item_index = \
                                            len(item_name_list)
                                        is_index_valid = \
                                            0 <= selected_item_index < \
                                            max_item_index
                                        if is_index_valid:
                                            item = \
                                                item_name_list[
                                                    selected_item_index
                                                ]
                                            is_not_duplicate = \
                                                item not in \
                                                dishes_selected
                                            if is_not_duplicate:
                                                dishes_selected.\
                                                    append(item)
                                        else:
                                            max_dish_num = \
                                                str(max_item_index)
                                            error_message = (
                                                "Invalid input: " +
                                                "no dish number " +
                                                str(dish_number) + " Use 1-"
                                                + max_dish_num
                                            )
                                            print(error_message)
                                            is_selection_valid = False
                                            break
                                else:
                                    error_message = (
                                        "Invalid range format: " +
                                        part_str
                                    )
                                    print(error_message)
                                    is_selection_valid = False
                                    break
                            else:
                                error_message = (
                                    "Invalid range format: " +
                                    part_str
                                )
                                print(error_message)
                                is_selection_valid = False
                                break
                        else:
                            if part_str.isdigit():
                                selected_item_index = int(part_str) - 1
                                max_item_index = len(item_name_list)
                                is_index_valid = \
                                    0 <= selected_item_index < max_item_index
                                if is_index_valid:
                                    item = item_name_list[
                                        selected_item_index
                                    ]
                                    is_not_duplicate = \
                                        item not in dishes_selected
                                    if is_not_duplicate:
                                        dishes_selected.append(item)
                                else:
                                    max_dish_num = str(max_item_index)
                                    error_message = (
                                        "Invalid input: " +
                                        "no dish number " + part_str +
                                        " Use 1-" + max_dish_num
                                    )
                                    print(error_message)
                                    is_selection_valid = False
                                    break
                            else:
                                error_message = "Invalid input: " + part_str
                                print(error_message)
                                is_selection_valid = False
                                break

                        if not is_selection_valid:
                            break

                    if is_selection_valid:
                        for item_name in dishes_selected:
                            item_eaters_map[item_name].append(
                                diner_name
                            )
                        selection_complete = True

        print("\n" + "=" * 50)
        print("Summarized Details")
        print("=" * 50)

        diner_running_total_map = {}
        for diner_name in diner_names_list:
            diner_running_total_map[diner_name] = 0.0

        for item_name in dish_to_price_map:
            item_price = dish_to_price_map[item_name]
            eaters_list = item_eaters_map[item_name]
            eater_count = len(eaters_list)

            if eater_count > 0:
                cost_per_eater = item_price / eater_count
                print("")
                print(item_name + ": THB " +
                      str(round(item_price, 2)))

                eaters_text = ", ".join(eaters_list)
                print(" Who ate this: " + eaters_text)
                print(" Each person must pay: THB " +
                      str(round(cost_per_eater, 2)))

                for diner_name in eaters_list:
                    diner_running_total_map[diner_name] += cost_per_eater
            else:
                print("")
                print(item_name + ": THB " +
                      str(round(item_price, 2)))
                print(" No one ate this dish")

        print("\n" + "=" * 50)
        print("Bill Split for Each Person")
        print("=" * 50)

        for diner_name in diner_names_list:
            final_owed_amount = diner_running_total_map[diner_name]
            print(diner_name + ": THB " +
                  str(round(final_owed_amount, 2)))

        total_bill_amount = sum(dish_to_price_map.values())
        print("\nTotal bill: THB " + str(round(total_bill_amount, 2)))
        print("\n" + "*" * 50)
        print("                 PLEASE PAY NA KRUB               ")