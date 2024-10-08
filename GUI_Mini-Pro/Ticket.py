class Ticket:
    def __init__(self, start_station, end_station, distance, price):
        self.start_station = start_station
        self.end_station = end_station
        self.distance = distance
        self.price = price

    def Display_Ticket(self):
        print(self.start_station, self.end_station, self.distance, self.price)