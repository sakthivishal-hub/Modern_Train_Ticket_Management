class BookingView:

    def get_booking_details(self):

        print("\n===== BOOK TICKET =====")

        u_id = int(input("Enter User ID: "))
        b_id = int(input("Enter Booking ID: "))
        b_time = input("Enter Booking Time: ")
        t_id = int(input("Enter Train ID: "))
        b_type = input("Enter Booking Type: ")
        seat_no = input("Enter Seat Number: ")
        p_id = int(input("Enter Passenger ID: "))
        p_service = input("Enter Passenger Service: ")

        return (u_id,b_id,b_time,t_id,b_type,seat_no,p_id,p_service)

    #
    def display_booking(self, booking):

        if booking is None:
            print("\nBooking not found.")
            return

        print("\n===== BOOKING DETAILS =====")
        print("Booking ID :", booking.b_id)
        print("User ID    :", booking.u_id)
        print("Train ID   :", booking.t_id)
        print("Booking Time:", booking.b_time)
        print("Booking Type:", booking.b_type)
        print("Seat Number:", booking.seat_no)
        print("Passenger ID:", booking.p_id)
        print("Service    :", booking.p_service)

    def display_bookings(self, bookings):

        if not bookings:
            print("\nNo bookings found.")
            return

        for booking in bookings:
            self.display_booking(booking)

  
    def get_fare_details(self):

        number_of_passengers = int(
            input("Enter Number of Passengers: ")
        )

        fare_per_passenger = float(
            input("Enter Fare Per Passenger: ")
        )

        return number_of_passengers, fare_per_passenger


    def display_fare(self, total_fare):

        print("\nTotal Fare: ₹", total_fare)


    def display_pnr(self, pnr):

        print("\n===== BOOKING CONFIRMED =====")
        print("PNR:", pnr)


    def display_seat_status(self, available):

        if available:
            print("Seat is available.")
        else:
            print("Seat is already booked.")