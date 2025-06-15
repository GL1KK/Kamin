import potatoes, beds, gardener

info = input("Объекты: ").split()
try:
    for i in range(len(info)):
        print(info[i - 1])
        if "гряд" in info[i].lower():
            if info[i - 1].isdigit():
                count_beds = int(info[i - 1])
        elif "картош" in info[i].lower():
            if info[i - 1].isdigit():
                count_potatoes = int(info[i - 1])
    print(count_beds, count_potatoes)
except NameError as e:
    print(e)
else:
    print("уля")
    list_beds = []
    for i in range(count_beds):
        list_beds.append(beds.Beds([potatoes.Potatoes(i+1)
                                    for i in range(count_potatoes)]))
    
    # Создаем садовника
    gardener_obj = gardener.Gardener("Иван")
    
    for i in range(7):
        for j in list_beds:
            j.speak()
            j.grow()
            print("-------------------")
        if i in [2, 5]:
            gardener_obj.harvest(list_beds)
finally:
    print("я работаю")