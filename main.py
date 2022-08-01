from user import User
from card import Card
from seat import Seat
from ticket import Ticket

user = User('John')
seat = Seat()
card = Card('12345678','098',user)
ticket = Ticket(user,seat.get_price(),seat)