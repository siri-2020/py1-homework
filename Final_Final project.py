print("=== โปรแกรมหารค่าอาหาร ===\n")

# เก็บชื่อเมนูและราคาของอาหาร
menu_dictionary = {}

print("กรอกชื่อเมนูและราคา:")
print("**กด Enter ข้อความเปล่าเพื่อไปส่วนถัดไป**")

while True:
    dish_name = input("\nชื่อเมนู: ").strip()

    if dish_name == "":
        break

    # รับราคาของเมนู
    dish_price = -1
    while dish_price < 0:
        price_input = input(
            "ใส่ราคา " + dish_name + "(เป็นตัวเลข): THB "
        ).strip()
        dish_price = float(price_input)
        if dish_price < 0:
            print("ราคาต้องไม่ติดลบ")

    # เก็บราคาของเมนูใน dictionary
    menu_dictionary[dish_name] = dish_price

if len(menu_dictionary) == 0:
    print("ไม่มีเมนู")
else:
    # แสดงรายการอาหารทั้งหมด
    print("")
    print("--- รายการอาหาร (" + str(len(menu_dictionary)) + " เมนู) ---")
    for dish_name in menu_dictionary:
        dish_price = menu_dictionary[dish_name]
        print(dish_name + ": THB " + str(round(dish_price, 2)))

    # รับรายชื่อคนที่มากิน
    people_list = []
    print("\nกรอกชื่อ (ทีละคน):")
    print("**กด Enter ข้อความเปล่าเพื่อไปส่วนถัดไป**")

    while True:
        person_name = input("ชื่อ: ").strip()

        if person_name == "":
            break

        if person_name in people_list:
            print(person_name + " มีอยู่แล้ว")
        else:
            people_list.append(person_name)

    if len(people_list) == 0:
        print("โต๊ะนี้ไม่มีคน")
    else:
        # แสดงรายชื่อทั้งหมด
        print("")
        print("--- รายชื่อ (" + str(len(people_list)) + " คน) ---")
        for person_name in people_list:
            print("- " + person_name)

        # เก็บว่าใครกินเมนูไหน
        dish_eaters_dict = {}
        for dish_name in menu_dictionary:
            dish_eaters_dict[dish_name] = []

        print("")
        print("--- ใครกินอะไรบ้าง ---")

        dish_name_list = list(menu_dictionary.keys())

        for person_name in people_list:
            print("")
            print(person_name + " กินอะไรบ้าง?")

            # แสดงเมนูพร้อมหมายเลข
            for index in range(len(dish_name_list)):
                number_display = index + 1
                dish_name = dish_name_list[index]
                print(str(number_display) + ". " + dish_name)

            # ให้เลือกเมนู
            got_selected_dishes = False
            while not got_selected_dishes:
                prompt_text = (
                    "เมนูของ " + person_name
                    + " (ใส่เป็นตัวเลข เว้นด้วยลูกน้ำเท่านั้น เช่น 1,2,3): "
                )
                choice_input = input(prompt_text).strip()

                if choice_input == "":
                    got_selected_dishes = True
                else:
                    number_inputs = choice_input.split(',')
                    selected_dishes = []
                    is_valid = True

                    for number_input in number_inputs:
                        number_input = number_input.strip()
                        selected_index = int(number_input) - 1

                        if 0 <= selected_index < len(dish_name_list):
                            dish_name = dish_name_list[selected_index]
                            selected_dishes.append(dish_name)
                        else:
                            message = (
                                "กรอกไม่ถูกต้อง: ไม่มีเมนูที่ " + number_input + ". ใช้ 1-"
                                + str(len(dish_name_list))
                            )
                            print(message)
                            is_valid = False
                            break

                    if is_valid:
                        for dish_name in selected_dishes:
                            dish_eaters_dict[dish_name].append(person_name)
                        got_selected_dishes = True

        # ส่วนคำนวณ
        print("\n" + "=" * 50)
        print("รายละเอียดการคำนวณ")
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

                print("")
                print(dish_name + ": THB " + str(round(dish_price, 2)))

                eaters_text = ", ".join(eaters_list)
                print("  คนที่หาร: " + eaters_text)
                print("  คนละ: THB " + str(round(shared_price, 2)))

                for person_name in eaters_list:
                    person_total_dict[person_name] = (
                        person_total_dict[person_name] + shared_price
                    )
            else:
                print("")
                print(dish_name + ": THB " + str(round(dish_price, 2)))
                print("  ไม่มีใครกิน")

        # แสดงสรุปผลลัพธ์
        print("\n" + "=" * 50)
        print("สรุปยอด")
        print("=" * 50)

        for person_name in people_list:
            total_price = person_total_dict[person_name]
            print(person_name + ": THB " + str(round(total_price, 2)))

        total_bill = sum(menu_dictionary.values())
        print("")
        print("รวมทั้งหมด: THB " + str(round(total_bill, 2)))