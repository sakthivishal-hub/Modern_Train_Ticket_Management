from models.Cancellation import Cancellation


class CancellationController:

    def __init__(self):
        self.cancellations = []

    def create_cancellation(self,c_id,b_id,c_time,reason,c_charge,refund_amount):

        
        for cancellation in self.cancellations:
            if cancellation.c_id == c_id:
                return None

        cancellation = Cancellation(
            c_id,
            b_id,
            c_time,
            reason,
            c_charge,
            refund_amount
        )

        self.cancellations.append(Cancellation)

        return Cancellation


    def get_cancellation(self, c_id):

        for cancellation in self.cancellations:

            if cancellation.c_id == c_id:
                return cancellation

        return None

    def get_booking_cancellation(self, b_id):

        for cancellation in self.cancellations:

            if cancellation.b_id == b_id:
                return cancellation

        return None


    def calculate_cancellation_charge(self,ticket_fare,cancellation_percentage):

        if ticket_fare < 0:
            return 0

        if cancellation_percentage < 0:
            return 0

        charge = (
            ticket_fare
            * cancellation_percentage
            / 100
        )

        return charge


    def calculate_refund(
        self,
        ticket_fare,
        cancellation_charge
    ):

        refund = ticket_fare - cancellation_charge

        if refund < 0:
            return 0

        return refund


    def cancel_booking(
        self,
        b_id,
        ticket_fare,
        cancellation_percentage,
        reason,
        c_id,
        c_time
    ):

    
        existing = self.get_booking_cancellation(b_id)

        if existing is not None:
            return None

        cancellation_charge = self.calculate_cancellation_charge(
            ticket_fare,
            cancellation_percentage
        )

        refund_amount = self.calculate_refund(
            ticket_fare,
            cancellation_charge
        )

        cancellation = self.create_cancellation(
            c_id,
            b_id,
            c_time,
            reason,
            cancellation_charge,
            refund_amount
        )

        return cancellation


    def get_all_cancellations(self):

        return self.cancellations