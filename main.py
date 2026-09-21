from controllers.user_controller import UserController
from controllers.train_controller import TrainController
from controllers.booking_controller import BookingController
from controllers.payment_controller import PaymentController
from controllers.cancellation_controller import CancellationController

from views.user_view import UserView
from views.train_view import TrainView
from views.booking_view import BookingView
from views.payment_view import PaymentView
from views.cancellation_view import CancellationView


class RailwayApp:

    def __init__(self):

        
        self.user_controller = UserController()
        self.train_controller = TrainController()
        self.booking_controller = BookingController()
        self.payment_controller = PaymentController()
        self.cancellation_controller = CancellationController()

        # Views
        self.user_view = UserView()
        self.train_view = TrainView()
        self.booking_view = BookingView()
        self.payment_view = PaymentView()
        self.cancellation_view = CancellationView()

        
        self.current_user = None

        self.ADMIN_EMAIL = "admin@railway.com"
        self.ADMIN_PASSWORD = "admin123"

    def run(self):

        while True:

            print("\n======================================")
            print("      TRAIN TICKET BOOKING SYSTEM")
            print("======================================")
            print("1. Register")
            print("2. User Login")
            print("3. Admin Login")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "3":
                self.admin_login()

            elif choice == "4":
                print("\nThank you for using the system.")
                break

            else:
                print("\nInvalid choice.")


    def admin_login(self):

        print("\n===== ADMIN LOGIN =====")

        email = input("Enter Admin Email: ")
        password = input("Enter Admin Password: ")

        if (
            email == self.ADMIN_EMAIL
            and password == self.ADMIN_PASSWORD
            ):

            print("\nAdmin login successful!")

            self.admin_menu()

        else:

            print("\nInvalid admin credentials.")

    def register(self):

        details = self.user_view.get_registration_details()

        user = self.user_controller.register_user(*details)

        if user:
            self.user_view.show_message(
                "Registration successful!"
            )
        else:
            self.user_view.show_message(
                "Registration failed. Email already exists."
            )


    def login(self):

        email, password = self.user_view.get_login_details()

        user = self.user_controller.login_user(
            email,
            password
        )

        if user:

            self.current_user = user

            print(
                f"\nWelcome, {user.u_name}!"
            )

            self.user_menu()

        else:

            print("\nInvalid email or password.")


    def admin_menu(self):

        while True:

            print("\n======================================")
            print("              ADMIN MENU")
            print("======================================")
            print("1. Add Train")
            print("2. Update Train")
            print("3. Remove Train")
            print("4. View All Trains")
            print("5. View All Bookings")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.add_train()

            elif choice == "2":

                self.update_train()

            elif choice == "3":

                self.remove_train()

            elif choice == "4":

                self.view_all_trains()

            elif choice == "5":

                bookings = (
                    self.booking_controller.get_all_bookings())

                self.booking_view.display_bookings(
                    bookings
                )

            elif choice == "6":

                print("\nAdmin logged out.")

                break

            else:

                print("\nInvalid choice.")



    def user_menu(self):

        while self.current_user:

            print("\n======================================")
            print("              USER MENU")
            print("======================================")
            print("1. View Profile")
            print("2. Update Profile")
            print("3. Search Train")
            print("4. Book Ticket")
            print("5. My Bookings")
            print("6. Make Payment")
            print("7. Cancel Ticket")
            print("8. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_profile()

            elif choice == "2":
                self.update_profile()

            elif choice == "3":
                self.search_train()

            elif choice == "4":
                self.book_ticket()

            elif choice == "5":
                self.my_bookings()

            elif choice == "6":
                self.make_payment()

            elif choice == "7":
                self.cancel_ticket()

            elif choice == "8":

                self.current_user = None

                print("\nLogged out successfully.")

            else:

                print("\nInvalid choice.")



    def view_profile(self):

        user = self.user_controller.view_profile(
            self.current_user.u_id
        )

        self.user_view.display_profile(user)



    def update_profile(self):

        details = self.user_view.get_update_details()

        user = self.user_controller.update_profile(
            self.current_user.u_id,
            *details
        )

        if user:

            self.current_user = user

            print("\nProfile updated successfully.")

        else:

            print("\nUser not found.")



    def search_train(self):

        source, destination = (
            self.train_view.get_search_details()
        )

        trains = self.train_controller.search_train(
            source,
            destination
        )

        self.train_view.display_trains(trains)



    def book_ticket(self):

        print("\n===== BOOK TICKET =====")

        details = self.booking_view.get_booking_details()

        (
            u_id,
            b_id,
            b_time,
            t_id,
            b_type,
            seat_no,
            p_id,
            p_service
        ) = details

    
        if u_id != self.current_user.u_id:

            print("\nYou can only book tickets for yourself.")

            return

        train = None

        for t in self.train_controller.trains:

            if t.t_id == t_id:
                train = t
                break

        if train is None:

            print("\nTrain not found.")

            return

        # Check seat
        seat_available = (
            self.booking_controller.select_seat(
                t_id,
                seat_no
            )
        )

        if not seat_available:

            print("\nSeat already booked.")

            return

        # Create booking
        booking = self.booking_controller.create_booking(
            u_id,
            b_id,
            b_time,
            t_id,
            b_type,
            seat_no,
            p_id,
            p_service
        )

        if booking is None:

            print("\nBooking ID already exists.")

            return

        # Reduce available seats
        if train.available_seats > 0:

            train.available_seats -= 1

        else:

            print("\nNo seats available.")

            self.booking_controller.cancel_booking(b_id)

            return

        # Generate PNR
        pnr = self.booking_controller.generate_pnr(
            b_id
        )

        self.booking_view.display_booking(
            booking
        )

        self.booking_view.display_pnr(
            pnr
        )



    def my_bookings(self):

        bookings = self.booking_controller.get_user_bookings(
            self.current_user.u_id
        )

        self.booking_view.display_bookings(
            bookings
        )


    def make_payment(self):

        details = self.payment_view.get_payment_details()

        (
            p_id,
            u_id,
            amount,
            p_method
        ) = details

        if u_id != self.current_user.u_id:

            print("\nInvalid user.")

            return

        payment = self.payment_controller.create_payment(
            p_id,
            u_id,
            amount,
            p_method
        )

        if payment is None:

            print("\nPayment ID already exists.")

            return

        print("\nPayment created.")

        # Simulate successful payment
        payment = self.payment_controller.process_payment(
            p_id
        )

        self.payment_view.display_payment(
            payment
        )

    def update_train(self):

        t_id = int(
            input("\nEnter Train ID to update: ")
        )

        details = self.train_view.get_update_details()

        train = self.train_controller.update_train(
        t_id,
        *details
        )

        if train:

            print("\nTrain updated successfully.")

        else:

            print("\nTrain not found.")


    def cancel_ticket(self):

        details = (
            self.cancellation_view
            .get_cancellation_details()
        )

        (
            b_id,
            ticket_fare,
            cancellation_percentage,
            reason,
            c_id,
            c_time
        ) = details

        # Check booking
        booking = self.booking_controller.get_booking(
            b_id
        )

        if booking is None:

            print("\nBooking not found.")

            return

        # Check booking belongs to current user
        if booking.u_id != self.current_user.u_id:

            print("\nYou cannot cancel this booking.")

            return

        cancellation = (
            self.cancellation_controller.cancel_booking(
                b_id,
                ticket_fare,
                cancellation_percentage,
                reason,
                c_id,
                c_time
            )
        )

        if cancellation is None:

            print("\nBooking already cancelled.")

            return

        # Remove booking
        self.booking_controller.cancel_booking(
            b_id
        )

        self.cancellation_view.display_cancellation(
            cancellation
        )



    def admin_menu(self):

        while True:

            print("\n======================================")
            print("              ADMIN MENU")
            print("======================================")
            print("1. Add Train")
            print("2. Update Train")
            print("3. Remove Train")
            print("4. View All Trains")
            print("5. View All Bookings")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.add_train()

            elif choice == "2":

                self.update_train()

            elif choice == "3":

                self.remove_train()

            elif choice == "4":

                self.view_all_trains()

            elif choice == "5":

                bookings = (
                    self.booking_controller
                    .get_all_bookings()
                )

                self.booking_view.display_bookings(
                    bookings
                )

            elif choice == "6":

                break

            else:

                print("\nInvalid choice.")



    def add_train(self):

        details = self.train_view.get_train_details()

        train = self.train_controller.add_train(
            *details
        )

        if train:

            print("\nTrain added successfully.")

        else:

            print("\nTrain ID already exists.")



    def update_train(self):

        t_id = int(
            input("Enter Train ID to update: ")
        )

        details = self.train_view.get_update_details()

        train = self.train_controller.update_train(
            t_id,
            *details
        )

        if train:

            print("\nTrain updated successfully.")

        else:

            print("\nTrain not found.")



    def remove_train(self):

        t_id = int(
            input("Enter Train ID to remove: ")
        )

        success = self.train_controller.remove_train(
            t_id
        )

        if success:

            print("\nTrain removed successfully.")

        else:

            print("\nTrain not found.")



    def view_all_trains(self):

        trains = self.train_controller.trains

        self.train_view.display_trains(
            trains
        )




if __name__ == "__main__":

    app = RailwayApp()

    app.run()