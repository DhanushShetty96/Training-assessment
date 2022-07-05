contact = {}

while True:
    choice = int(input(" 1-->Add Contact\n 2-->Search contact \n 3-->Display Contact \n 4-->Delete Contact \n "
                       "5-->Partial Search\n"))
    print("------------------------------------------------")
    if choice==1 :
        name = input("Enter Name \n")
        num =input('Enter Number \n')

        contact[name]=[name,num]
    elif choice == 2:
        if len(contact)==0 :
            print("Contact list is empty")

        else :
            search = input("Enter contact name \n")
            if search in contact :
                print(contact[search])
                op=0
                while op !=1:
                    print("1--> Edit\n 2--> Go back \n")
                    op=int(input())
                    if op==1:
                        new_num=input("Enter new number \n")
                        contact[search]=new_num
                    else :
                        break
            else :
                print("Entered name not found ")
    elif choice == 3 :
        if len(contact)==0 :
            print("Contact list is empty")

        else:
           for i in range(len(contact)) :
               print(contact)

    elif choice == 4 :
        if len(contact)==0 :
            print("Contact list is empty")
        else:
            search = input("Enter contact name ")
            if search in contact:
                del contact[search]
    elif choice ==5 :
        par_name=input("Enter name to search")
        for i in contact.keys():
            if contact[i][0].startswith(par_name):
                print(contact[i])

    else :
        exit()