print("=== American Share Calculator ===\n")

menu = {}
print("Enter dishes and prices: \n**empty name to finish**")

while True:
    dish = input("\nDish name: ").strip()
    
    if dish == "":
        break
    
    while True:
        price_input = input("Price for " + dish + ": THB ").strip()
        
        if price_input.replace(".", "").isdigit():
            price = float(price_input)
            if price >= 0:
                menu[dish] = price
                break
            else:
                print("Price cannot be negative.")
        else:
            print("Invalid input. Enter a number.")

if len(menu) == 0:
    print("No dishes entered.")
else:
    # Display menu
    print("")
    print("--- Menu (" + str(len(menu)) + " dishes) ---")
    for dish in menu:
        price = menu[dish]
        print(dish + ": THB " + str(round(price, 2)))
    
    # Step 2: Collect people (List)
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
    
    if len(people) == 0:
        print("No people entered.")
    else:
        # Display people
        print("")
        print("--- People (" + str(len(people)) + ") ---")
        for person in people:
            print("- " + person)
        
        # Step 3: Track who ate what
        dish_eaters = {}
        for dish in menu:
            dish_eaters[dish] = []
        
        print("")
        print("--- Who ate what? ---")
        
        dish_list = list(menu.keys())
        
        for person in people:
            print("")
            print("What did " + person + " eat?")
            
            # Show menu with numbers
            for i in range(len(dish_list)):
                number = i + 1
                dish = dish_list[i]
                print(str(number) + ". " + dish)
            
            # Get person's dishes
            while True:
                prompt = person + "'s dishes (e.g., 1,2,3): "
                choice = input(prompt).strip()
                
                if choice == "":
                    break
                
                numbers = choice.split(',')
                dishes = []
                valid = True
                
                for num in numbers:
                    num = num.strip()
                    
                    if num.isdigit():
                        index = int(num) - 1
                        
                        if index >= 0 and index < len(dish_list):
                            dish = dish_list[index]
                            dishes.append(dish)
                        else:
                            msg = "Invalid: " + num + ". Use 1-"
                            msg = msg + str(len(dish_list))
                            print(msg)
                            valid = False
                            break
                    else:
                        print("Invalid input. Use numbers like 1,2,3")
                        valid = False
                        break
                
                if valid:
                    for dish in dishes:
                        dish_eaters[dish].append(person)
                    break
        
        # Step 4: Calculate bill
        print("")
        print("=" * 50)
        print("CALCULATION")
        print("=" * 50)
        
        person_total = {}
        for person in people:
            person_total[person] = 0.0
        
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
            print(person + ": THB " + str(round(total, 2)))
        
        bill_total = sum(menu.values())
        print("")
        print("Total bill: THB " + str(round(bill_total, 2)))
