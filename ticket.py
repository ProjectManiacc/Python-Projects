class Ticket:

    def __init__(self,user,price, seat):
        self.seat = seat
        self.price = price
        self.user = user

    def create_pdf(self,path):
        pass