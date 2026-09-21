class UserView:

    def get_registration_details(self):

        print("\n===== USER REGISTRATION =====")

        u_id = int(input("Enter User ID: "))
        u_name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        u_address = input("Enter Address: ")
        password = input("Enter Password: ")
        phonenumber = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        return (u_id,u_name,age,gender,u_address,password,phonenumber,email)


    def get_login_details(self):

        print("\n===== USER LOGIN =====")

        email = input("Enter Email: ")
        password = input("Enter Password: ")

        return email, password


    def display_profile(self, user):

        if user is None:
            print("\nUser not found.")
            return

        print("\n===== USER PROFILE =====")
        print("User ID    :", user.u_id)
        print("Name       :", user.u_name)
        print("Age        :", user.age)
        print("Gender     :", user.gender)
        print("Address    :", user.u_address)
        print("Phone      :", user.phonenumber)
        print("Email      :", user.email)


    def get_update_details(self):

        print("\n===== UPDATE PROFILE =====")
        
        u_name = input("Enter new name (Enter to skip): ")
        u_address = input("Enter new address (Enter to skip): ")
        phonenumber = input("Enter new phone (Enter to skip): ")
        email = input("Enter new email (Enter to skip): ")

        return (
            u_name if u_name else None,
            u_address if u_address else None,
            phonenumber if phonenumber else None,
            email if email else None
        )


    def show_message(self, message):

        print("\n" + message)