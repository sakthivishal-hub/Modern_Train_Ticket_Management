from models.Payment import Payment


class PaymentController:

    def __init__(self):
        self.payments = []

    def create_payment(self,p_id,u_id,amount,p_method):


        for payment in self.payments:
            if payment.p_id == p_id:
                return None

        payment = Payment(p_id,u_id,amount,p_method)

        self.payments.append(payment)

        return payment

    
    def get_payment(self, p_id):

        for payment in self.payments:

            if payment.p_id == p_id:
                return payment

        return None

    
    
    def get_user_payments(self, u_id):

        user_payments = []

        for payment in self.payments:

            if payment.u_id == u_id:
                user_payments.append(payment)

        return user_payments


    def process_payment(self, p_id):

        payment = self.get_payment(p_id)

        if payment is None:
            return None

        payment.status = "Successful"

        return payment

    def fail_payment(self, p_id):

        payment = self.get_payment(p_id)

        if payment is None:
            return None

        payment.status = "Failed"

        return payment


    def refund_payment(self, p_id):

        payment = self.get_payment(p_id)

        if payment is None:
            return None

        payment.status = "Refunded"

        return payment


    def update_payment(self,p_id,amount=None,p_method=None,status=None):

        payment = self.get_payment(p_id)

        if payment is None:
            return None

        if amount is not None:
            payment.amount = amount

        if p_method is not None:
            payment.p_method = p_method

        if status is not None:
            payment.status = status

        return payment


    def get_payment_status(self, p_id):

        payment = self.get_payment(p_id)

        if payment is None:
            return None

        return payment.status

    def get_all_payments(self):

        return self.payments