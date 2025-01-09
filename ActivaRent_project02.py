database = {}
password ="qwert"

def active(rent):

    def tern_and_condition():
        print("Term and Condition")
        print(""" 
                    1.Aadhaar Card is Mandatory.
                    2.Driving Licence is Mandatory.
                    3.One Activa for One Day: 500/-
                    """)



    def bill(name,phone,aadhar,address,licenses,days,no_rent_activa,p):
        bills=open(r"E:\Python by Aman\Activahouse_bill.txt","w")
        bills.write(f''' 
                    ================================================================
                                        * ACTIVA RENT BILL *
                    ________________________________________________________________
                    NAME               :-  {name}                              
                    ADDRESS            :-  {address}
                    AADHAR NUMBER      :-  {aadhar}
                    LICENSES           :-  {licenses}
                    PHONE              :-  {phone}
                    days               :-  {days}
                    ________________________________________________________________
                    QUANTITY           :-  {no_rent_activa}
                    ________________________________________________________________
                    PRICE              :-  {p}
                    ________________________________________________________________
                                          * THANK YOU *
                    ================================================================

                    ''')
        bills.close()

    def rent_activa():
        tern_and_condition()
        nonlocal rent

        a = input("Y/N")
        print("Welcome to Rent Activa ")
        print("No of Activa Available: ", rent)
        if a == "y" or a == "Y":
            name = input("Enter Your Name :-")
            phone = input("Enter Your Phone Number  :-")
            address = input("Enter Your Address  :-")
            aadhar = input("Enter Your Aadhar Number :- ")
            licenses = input("Enter Your License :-")
            days = int(input("Enter Your days :-"))
            price = 500
            no_rent_activa = int(input("Enter Your Number of Activa in Rent :-"))
            if no_rent_activa <= rent:
                rent-=no_rent_activa
                database[aadhar]={
                    "name":name,
                    "phone":phone,
                    "address":address,
                    "licenses":licenses,
                    "days":days,
                    "no_rent_activa":no_rent_activa
                }

                p = (price*no_rent_activa*days)
                bill(name, phone, aadhar, address, licenses, days, no_rent_activa, p)
            else:
                print(f"only contain {rent} ")

        else:
            print("Please Gives permission yes and no ")
        print("Booked ")
        print("No of Activa Available: ", rent)

    def activa_return():
        nonlocal rent
        print("Welcome to the Return Activa ")
        aadhar= input("Enter Aadhar Number :- ")
        if aadhar in database:
            retur = int(input("Enter Return Activa : "))
            if retur <= database[aadhar]["no_rent_activa"]:
                rent += retur
                database[aadhar]["no_rented_activa"] = database[aadhar]["no_rent_activa"]+retur
            else:
                print(f"You are booked {database[aadhar]["no_rent_activa"]}")

        else:
            ("Invalid Aadhar Numver !")
        print("Successfully Return ")


    def owner_part():
        print("Welcome to Owner Access ")
        password = input("Enter your Password : ")
        if password == password:
            print(database)
            print("No of Activa Available: ", rent)
        else:
            print("Worng password ")

    while True:
        var = input("""
        1. Rent 
        2. Return 
        3. Owner
        4. Exist ____""")
        if var == "1":
            rent_activa()
        elif var == "2":
            activa_return()
        elif var == "3":
            owner_part()
        elif var == "4":
            break
        else:
            print(" PLease Enter Correct Option no")





active(20)