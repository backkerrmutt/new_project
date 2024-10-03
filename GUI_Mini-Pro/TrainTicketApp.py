import tkinter as tk
from contextlib import nullcontext
from tkinter import messagebox
from Ticket import Ticket
import GUI as cr

class TrainTicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Ticket System")

        self.start_station_var = tk.StringVar()
        self.end_station_var = tk.StringVar()
        self.distance_var = tk.IntVar()
        self.price_var = tk.IntVar()
        self.amount_paid_var = tk.IntVar()
        self.change_var = tk.IntVar()

        self.tickets = []
        self.revenue = []
        self.changes = []

        cr.create_widgets(self)


    def calculate_change(self):
        price = self.price_var.get()
        amount_paid = self.amount_paid_var.get()
        change = amount_paid - price
        self.change_var.set(change)

    def sell_ticket(self):
        start_station = self.start_station_var.get()
        end_station = self.end_station_var.get()
        distance = self.distance_var.get()
        price = self.price_var.get()
        amount_paid = self.amount_paid_var.get()
        change = self.change_var.get()

        if amount_paid < price:
            messagebox.showerror("Error", "Insufficient amount paid")
            return
        elif not self.start_station_var.get() or not self.end_station_var.get() or not self.distance_var.get() or not self.price_var.get() or not self.amount_paid_var.get():
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        ticket = Ticket(start_station, end_station, distance, price)
        self.tickets.append((start_station, end_station))
        self.revenue.append(price)
        self.changes.append(change)

        messagebox.showinfo("Success", "Ticket sold successfully")
        self.clear_fields()

    def clear_fields(self):
        self.start_station_var.set("")
        self.end_station_var.set("")
        self.distance_var.set(0)
        self.price_var.set(0)
        self.amount_paid_var.set(0)
        self.change_var.set(0)


