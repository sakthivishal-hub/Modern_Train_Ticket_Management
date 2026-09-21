from models.user import User


class UserController:

    def __init__(self):
        self.users = []

    def register_user(self,u_id,u_name,age,gender,u_address,password,phonenumber,email):
        
        for user in self.users:
            if user.email == email:
                return None

        user = User(
            u_id,
            u_name,
            age,
            gender,
            u_address,
            password,
            phonenumber,
            email
        )

        self.users.append(user)

        return user

    def login_user(self, email, password):

        for user in self.users:

            if user.email == email and user.password == password:
                print("Login successful")
                return user

        print("Invalid email or password")
        return None

    def view_profile(self, u_id):

        for user in self.users:
            if user.u_id == u_id:
                return user

        return "User not found"

    def update_profile(self,u_id,u_name=None,u_address=None,phonenumber=None,email=None):

        for user in self.users:
            if user.u_id==u_id:
                if u_name is not None:
                    user.u_name=u_name
                if u_address is not None:
                    user.u_address=u_address
                if phonenumber is not None:
                    user.phonenumber=phonenumber
                if email is not None:
                    user.email=email
                return user
            return None

    
            



    