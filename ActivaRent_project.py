database = {}
password = "qwert"

def active(rent):
    print("Welcome To Activa Rental House. ")
    while True:
        print("No of Activa Available: ",rent)
        var = input("""
        1. Rent 
        2. Return 
        3. Owner
        4. Exist ____""")

        if var == "1":
            print("Term and Condition")
            print(""" 
            1.Aadhaar Card is Mandatory.
            2.Driving Licence is Mandatory.
            3.One Activa for One Day: 500/-
            """)
            a = input("Y/N :")
            if a == "Y" or a == "y":
                name = input("Enter your name : ")
                phone = input("enter your phone no : ")
                address = input("Enter your Address : ")
                aadhar= input("Enter your Adhar No : ")
                license = input("Enter your license : ")
                days = int(input("Enter"))
                rented_activa = int(input("Enter Number of Activa in rent : "))
                price = 500
                if rented_activa <= rent:
                    rent = rent - rented_activa
                    database[aadhar] ={"name":name,"phone":phone,"address":address,"license":license,"rented_activa":rented_activa}
                    bill = open(r"E:\Python by Aman\ActiveHouseDB.txt","w")
                    bill.write("\n")


                    p = price * rented_activa
                    bill.write(f''' 
                    ================================================================
                                        * ACTIVA RENT BILL *
                    ________________________________________________________________
                    NAME               :-  {name}                              
                    ADDRESS            :-  {address}
                    AADHAR NUMBER      :-  {aadhar}
                    LICENSES           :-  {license}
                    PHONE              :-  {phone}
                    ________________________________________________________________
                    QUANTITY           :-  {rented_activa}
                    ________________________________________________________________
                    PRICE              :-  {p}
                    ________________________________________________________________
                                          * THANK YOU *
                    ================================================================

                    ''')
                    bill.close()



                else:
                    print(f"only {rent} activa ")
                    print()


        elif var == "2":
            print("Welcome to Return ")
            aadhar_no = input("Emter your Aadhar No : ")
            if aadhar_no in database:
                retur = int(input("Enter your retrun activa : "))
                if retur <= database[aadhar]["rented_activa"]:
                    rent = rent + retur

                    bill = open(r"E:\Python by Aman\ActiveHouseDB.txt", "w")
                    bill.write("\n")
                    bill.write(
                        f"name : {name}, phone :{phone}, address :{address}, Aadhar :{aadhar}, license :{license}, Rented_activa:{rented_activa} ")
                    print(bill)
                    bill.close()
                else:
                    print(f" Your Booked activa  {database[aadhar]["rented_activa"]}")
            else:
                print("You doest not Rented Activa ")



        elif var == "3":
            print("Welcome to Owner")
            owner = input("Enter your password :  ")
            if owner == password:
                print(database)
            else:
                print("wrong password ")

        elif var == "4":
            break
        else:
            print("Enter the correct No ")

active(20)