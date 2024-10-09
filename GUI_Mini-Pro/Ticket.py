import tkinter
import tkinter as tk
from tkinter import Label

from django.db.models.expressions import result


class Ticket:
    def __init__(self,Num_tic ,start_station, end_station, distance, price):
        self.Num_tic = Num_tic
        self.start_station = start_station
        self.end_station = end_station
        self.distance = distance
        self.price = price

    def Display_Ticket(self):
        result =f"tickets : {self.Num_tic}, Start: {self.start_station}, End: {self.end_station}, Distance: {self.distance}, Price: {self.price}"
        return result