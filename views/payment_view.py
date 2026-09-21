class PaymentView:


    def get_payment_details(self):

        print("\n===== PAYMENT =====")

        p_id = int(input("Enter Payment ID: "))
        u_id = int(input("Enter User ID: "))
        amount = float(input("Enter Amount: "))
        p_method = input("Enter Payment Method: ")

        return p_id, u_id, amount, p_method

 
    def display_payment(self, payment):

        if payment is None:
            print("\nPayment not found.")
            return

        print("\n===== PAYMENT DETAILS =====")
        print("Payment ID :", payment.p_id)
        print("User ID    :", payment.u_id)
        print("Amount     : ₹", payment.amount)
        print("Method     :", payment.p_method)
        print("Status     :", payment.status)


    def display_status(self, status):

        print("\nPayment Status:", status)