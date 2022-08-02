import sqlite3


class Seat:

    database = 'cineba.db'

    def __init__(self):
        pass

    def get_seat_id(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT seat_id FROM Seat 
        """)
        result = cursor.fetchall()

        cursor.commit()
        connection.close()

        return result

    def get_price(self):
        pass

    def get_available(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                SELECT seat_id FROM Seat WHERE taken=0
                """)
        result = cursor.fetchall()
        cursor.commit()
        connection.close()

        return result

    def is_free(self,seat_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT taken FROM Seat WHERE taken=0 AND seat_id=?
                        """,[seat_id])
        cursor.commit()
        result = cursor.fetchall()
        connection.close()
        if result == 0:
            return True
        else:
            return False

    def is_occupied(self):
        pass
