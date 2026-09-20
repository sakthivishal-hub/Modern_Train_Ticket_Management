from controllers.user_controller import UserController
from controllers.train_controller import TrainController
"""
user_controller = UserController()

user_controller.register_user(
    1,
    "Arun",
    21,
    "Male",
    "Coimbatore",
    "1234",
    "9876543210",
    "arun@gmail.com"
)


user_controller.login_user(
    "arun@gmail.com",
    "1234"
)

user=user_controller.view_profile(2)

user=user_controller.update_profile(1,"Sakthivishal",20,None,None,None,"6374803604",None)
print(user.age,user.phonenumber)
"""
train_controller=TrainController()

train_controller.add_train(178,"Tirupur Express","Tiruppur","coimbatore","10.00","12.00","Passenger",100)

train=train_controller.train_details(178)
print(train)
