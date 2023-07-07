contact = {}


while True:
    choice = str(input("1.Add the contact\n2.Search contact\n3.Updating contact information "))
    if choice == 1:
        name = input("Enter the contact name ")
        phone = input("Enter the phone number")
        contact[name] = phone
    elif choice == 2: 
        search_name = input("enter the contact name ")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        update_contact = input("Enter the contact to be updated")
        if update_contact in contact:
            phone = input("Enter the phone number")
            contact[update_contact]=phone
            print("contact updated")
        else:
            print("Name is not found in contact book")
    else:
        break


     
    