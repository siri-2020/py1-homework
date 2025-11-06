def bill_split():
    """Main function to run the bill split calculator."""
    print("=== Bill Split Calculator ===")
    print("")
    
    menu = collect_menu()
    if not menu:
        print("No dishes entered.")
        return
    
    display_menu(menu)
    
    people = collect_people()
    if not people:
        print("No people entered.")
        return
    display_people(people)
    
    dish_eaters = track_consumption(menu, people)
    calculate_bill(menu, people, dish_eaters)


def collect_menu():
    """Collect dish names and prices from user."""
    menu = {}
    print("Enter dishes and prices (empty name to finish):")
    
    while True:
        dish = input("\nDish name: ").strip()
        
        if dish == "":
            break
        
        price = get_valid_price(dish)
        menu[dish] = price
    
    return menu


def get_valid_price(dish):
    """Get a valid price from user input."""
    while True:
        price_input = input("Enter Price for " + dish + "in number: ฿").strip()
        
        # Check if input is a valid number
        if price_input == "":
            print("Please enter a price.")
            continue
        
        # Check if all characters are digits or decimal point
        is_valid = True
        has_dot = False
        
        for char in price_input:
            if char == ".":
                if has_dot:
                    is_valid = False
                    break
                has_dot = True
            elif char not in "0123456789":
                is_valid = False
                break
        
        if is_valid and price_input != ".":
            price = float(price_input)
            if price < 0:
                print("Price cannot be negative.")
            else:
                return price
        else:
            print("Invalid input. Enter a number.")


def display_menu(menu):
    """Display all dishes and prices."""
    count = len(menu)
    print("")
    print("--- Menu (" + str(count) + " dishes) ---")
    
    for dish in menu:
        price = menu[dish]
        price_str = str(round(price, 2))
        print(dish + ": THB " + price_str)


def collect_people():
    """Collect names of people sharing the bill."""
    people = []
    print("\nEnter people's names (empty name to finish):")
    
    while True:
        name = input("Name: ").strip()
        
        if name == "":
            break
        
        if name in people:
            print(name + " already added.")
        else:
            people.append(name)
    
    return people


def display_people(people):
    """Display all people."""
    count = len(people)
    print("")
    print("--- People (" + str(count) + ") ---")
    
    for person in people:
        print("- " + person)


def track_consumption(menu, people):
    """Track which dishes each person ate."""
    dish_eaters = {}
    
    for dish in menu:
        dish_eaters[dish] = []
    
    print("")
    print("--- Who ate what? ---")
    
    for person in people:
        print("")
        print("What did " + person + " eat?")
        show_menu_numbers(menu)
        
        dishes_eaten = get_person_dishes(menu, person)
        
        for dish in dishes_eaten:
            dish_eaters[dish].append(person)
    
    return dish_eaters


def show_menu_numbers(menu):
    """Display menu with numbers."""
    dish_list = list(menu.keys())
    
    for i in range(len(dish_list)):
        number = i + 1
        dish = dish_list[i]
        print(str(number) + ". " + dish)


def get_person_dishes(menu, person):
    """Get list of dishes a person ate."""
    dish_list = list(menu.keys())
    max_number = len(dish_list)
    
    while True:
        prompt = person + "'s dishes (e.g., 1,2,3): "
        choice = input(prompt).strip()
        
        if choice == "":
            return []
        
        numbers = choice.split(',')
        dishes = []
        valid = True
        
        for num in numbers:
            num = num.strip()
            
            # Check if num is all digits
            is_number = True
            for char in num:
                if char not in "0123456789":
                    is_number = False
                    break
            
            if is_number and num != "":
                index = int(num) - 1
                
                if index < 0 or index >= max_number:
                    msg = "Invalid: " + num + ". Use 1-" + str(max_number)
                    print(msg)
                    valid = False
                    break
                
                dish = dish_list[index]
                dishes.append(dish)
            else:
                print("Invalid input. Use numbers like 1,2,3")
                valid = False
                break
        
        if valid:
            return dishes


def calculate_bill(menu, people, dish_eaters):
    """Calculate how much each person owes."""
    print("")
    print("=" * 50)
    print("CALCULATION")
    print("=" * 50)
    
    # Dictionary to store each person's total
    person_total = {}
    for person in people:
        person_total[person] = 0.0
    
    # Calculate share for each dish
    for dish in menu:
        price = menu[dish]
        eaters = dish_eaters[dish]
        num_eaters = len(eaters)
        
        if num_eaters > 0:
            share = price / num_eaters
            
            print("")
            print(dish + ": THB " + str(round(price, 2)))
            
            eaters_text = ", ".join(eaters)
            print("  Split between: " + eaters_text)
            print("  Each pays: THB " + str(round(share, 2)))
            
            for person in eaters:
                person_total[person] = person_total[person] + share
        else:
            print("")
            print(dish + ": THB " + str(round(price, 2)))
            print("  Nobody ate this")
    
    # Display final totals
    print("")
    print("=" * 50)
    print("FINAL BILL")
    print("=" * 50)
    
    for person in people:
        total = person_total[person]
        total_str = str(round(total, 2))
        print(person + ": THB " + total_str)
    
    bill_total = sum(menu.values())
    print("")
    print("Total bill: THB " + str(round(bill_total, 2)))


if __name__ == "__main__":
    bill_split()