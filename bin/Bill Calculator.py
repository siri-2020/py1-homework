print("=== โปรแกรมหารค่าอาหาร === \n")
menu = {} # ทำ dict ระหว่างชื่ออาหารและราคา
print("กรอกชื่อเมนูและราคา: \n**กด Enter ข้อความเปล่าเพื่อไปส่วนถัดไป**")

while True:
    dish = input("\nชื่อเมนู: ").strip()
    
    if dish == "":
        break
    
    # รับค่าราคาอาหาร
    price = -1
    while price < 0:
        price_input = input("ใส่ราคา " + dish + "(เป็นตัวเลข): THB ").strip()
        price = float(price_input)
        if price < 0:
            print("ราคาต้องไม่ติดลบ")
    
    menu[dish] = price # ใส่ value ราคา ตาม key เป็นชื่อเมนู

if len(menu) == 0:
    print("ไม่มีเมนู")
else:
    # แสดงเมนู
    print("")
    print("--- รายการอาหาร (" + str(len(menu)) + " เมนู) ---")
    for dish in menu:
        price = menu[dish]
        print(dish + ": THB " + str(round(price, 2)))
    
    # รับค่าคนที่มากิน
    people = []
    print("\nกรอกชื่อ(ทีละคน):  \n**กด Enter ข้อความเปล่าเพื่อไปส่วนถัดไป**")
    
    while True:
        name = input("ชื่อ: ").strip()
        
        if name == "":
            break
        
        if name in people:
            print(name + " มีอยู่แล้ว")
        else:
            people.append(name)
    
    if len(people) == 0:
        print("ไม่มีใคร555")
    else:
        # แสดงรายชื่อ
        print("")
        print("--- รายชื่อ (" + str(len(people)) + " คน) ---")
        for person in people:
            print("- " + person)
        
        # รับค่าใครกินอะไรบ้าง ใส่ dict
        dish_eaters = {}
        for dish in menu:
            dish_eaters[dish] = []
        
        print("")
        print("--- ใครกินอะไรบ้าง ---")
        
        dish_list = list(menu.keys())
        
        for person in people:
            print("")
            print(person + " กินอะไรบ้าง?")
            
            # แสดงเมนูเป็นตัวเลขให้เลือก
            for i in range(len(dish_list)):
                number = i + 1
                dish = dish_list[i]
                print(str(number) + ". " + dish)
            
            # รับค่าชื่อคนไปยังเมนู
            got_dishes = False
            while got_dishes == False:
                prompt = "เมนูของ " + person + " (เว้นด้วยลูกน้ำเท่านั้น เช่น 1,2,3): "
                choice = input(prompt).strip()
                
                if choice == "":
                    got_dishes = True
                else:
                    numbers = choice.split(',')
                    dishes = []
                    valid = True
                    
                    for num in numbers:
                        num = num.strip()
                        index = int(num) - 1
                        
                        if index >= 0 and index < len(dish_list):
                            dish = dish_list[index]
                            dishes.append(dish)
                        else:
                            msg = "ไม่ถูกต้อง: " + num + ". ใช้ 1-"
                            msg = msg + str(len(dish_list))
                            print(msg)
                            valid = False
                            break
                    
                    if valid == True:
                        for dish in dishes:
                            dish_eaters[dish].append(person)
                        got_dishes = True
        
        # คำนวณ
        print("\n=" * 50)
        print("รายละเอียดการคำนวณ")
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
                print("  แชร์กันระหว่าง: " + eaters_text)
                print("  คนละ: THB " + str(round(share, 2)))
                
                for person in eaters:
                    person_total[person] = person_total[person] + share
            else:
                print("")
                print(dish + ": THB " + str(round(price, 2)))
                print("  ไม่มีใครกิน")
        
        # แสดงผลลัพธ์
        print("\n=" * 50)
        print("สรุปยอด")
        print("=" * 50)
        
        for person in people:
            total = person_total[person]
            print(person + ": THB " + str(round(total, 2)))
        
        bill_total = sum(menu.values())
        print("")
        print("รวมทั้งหมด: THB " + str(round(bill_total, 2)))