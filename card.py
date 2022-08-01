class Card:

    database ='banking.db'

    def __init__(self,number,cvc,holder,type='credit'):
        self.holder = holder
        self.cvc = cvc
        self.number = number
        self.type = type

    def validate(self,price):
        pass


