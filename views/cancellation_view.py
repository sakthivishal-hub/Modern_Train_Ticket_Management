class CancellationView:

    def get_cancellation_details(self):

        print("\n===== CANCEL TICKET =====")

        b_id = int(input("Enter Booking ID: "))
        ticket_fare = float(input("Enter Ticket Fare: "))
        cancellation_percentage = float(input("Enter Cancellation Percentage: "))
        reason = input("Enter Cancellation Reason: ")
        c_id = int(input("Enter Cancellation ID: "))
        c_time = input("Enter Cancellation Time: ")

        return (b_id,ticket_fare,cancellation_percentage,reason,c_id,c_time)

    def display_cancellation(self, cancellation):

        if cancellation is None:
            print("\nCancellation failed.")
            return

        print("\n===== CANCELLATION DETAILS =====")
        print("Cancellation ID :", cancellation.c_id)
        print("Booking ID      :", cancellation.b_id)
        print("Cancellation Time:", cancellation.c_time)
        print("Reason          :", cancellation.reason)
        print("Cancellation Fee: ₹", cancellation.c_charge)
        print("Refund Amount   : ₹", cancellation.refund_amount)


    def display_refund(self, refund):

        print("\nRefund Amount: ₹", refund)