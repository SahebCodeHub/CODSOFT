contacts = []
while True:
    print("\n1.Add  2.View  3.Search  4.Delete  5.Exit")
    ch = input("Choice: ")
    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.append([name, phone])
        print("Added!")
    elif ch == "2":
        for c in contacts:
            print(c[0], "-", c[1])
    elif ch == "3":
        key = input("Search name/phone: ")
        found = False
        for c in contacts:
            if key in c:
                print("Found:", c[0], c[1])
                found = True
        if not found:
            print("Not found.")
    elif ch == "4":
        key = input("Name to delete: ")
        for c in contacts:
            if c[0] == key:
                contacts.remove(c)
                print("Deleted!")
                break
        else:
            print("Not found.")
    elif ch == "5":
        break
    else:
        print("Invalid choice")