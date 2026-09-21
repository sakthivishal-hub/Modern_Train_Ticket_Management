from models.booking import Booking


class BookingController:

    def __init__(self):
        self.bookings = []

    # -----------------------------------------
    # CREATE BOOKING
    # -----------------------------------------
    def create_booking(self,u_id,b_id,b_time,t_id,b_type,seat_no,p_id,p_service):

        for booking in self.bookings:
            if booking.b_id == b_id:
                return None

        booking = Booking(u_id,b_id,b_time,t_id,b_type,seat_no,p_id,p_service)

        self.bookings.append(booking)

        return booking

    # -----------------------------------------
    # GET BOOKING BY ID
    # -----------------------------------------
    def get_booking(self, b_id):

        for booking in self.bookings:

            if booking.b_id == b_id:
                return booking

        return None

    # -----------------------------------------
    # GET USER BOOKINGS
    # -----------------------------------------
    def get_user_bookings(self, u_id):

        user_bookings = []

        for booking in self.bookings:

            if booking.u_id == u_id:
                user_bookings.append(booking)

        return user_bookings


    def get_train_bookings(self, t_id):

        train_bookings = []

        for booking in self.bookings:

            if booking.t_id == t_id:
                train_bookings.append(booking)

        return train_bookings

 
    def is_seat_available(self, t_id, seat_no):

        for booking in self.bookings:

            if (
                booking.t_id == t_id
                and booking.seat_no == seat_no
            ):
                return False

        return True


    def select_seat(self, t_id, seat_no):

        if self.is_seat_available(t_id, seat_no):
            return True

        return False


    def calculate_fare(
        self,
        number_of_passengers,
        fare_per_passenger
    ):

        if number_of_passengers <= 0:
            return 0

        if fare_per_passenger < 0:
            return 0

        total_fare = (
            number_of_passengers
            * fare_per_passenger
        )

        return total_fare


    def generate_pnr(self, b_id):

        return f"PNR{b_id}"


    def update_booking(
        self,
        b_id,
        b_time=None,
        b_type=None,
        seat_no=None,
        p_id=None,
        p_service=None
    ):

        for booking in self.bookings:

            if booking.b_id == b_id:

                if b_time is not None:
                    booking.b_time = b_time

                if b_type is not None:
                    booking.b_type = b_type

                if seat_no is not None:
                    booking.seat_no = seat_no

                if p_id is not None:
                    booking.p_id = p_id

                if p_service is not None:
                    booking.p_service = p_service

                return booking

        return None

    def cancel_booking(self, b_id):

        booking = self.get_booking(b_id)

        if booking is None:
            return False

        self.bookings.remove(booking)

        return True


    def get_all_bookings(self):

        return self.bookings