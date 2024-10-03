import tkinter as tk
from tkinter import messagebox


class Ticket:
    def __init__(self, start_station, end_station, distance, price):
        self.start_station = start_station
        self.end_station = end_station
        self.distance = distance
        self.price = price

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

        self.create_widgets()





    def create_widgets(self):
        tk.Label(self.root, text="Start Station:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.start_station_var).grid(row=0, column=1)

        tk.Label(self.root, text="End Station:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.end_station_var).grid(row=1, column=1)

        tk.Label(self.root, text="Distance (km):").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.distance_var).grid(row=2, column=1)

        tk.Label(self.root, text="Price (THB):").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.price_var).grid(row=3, column=1)

        tk.Label(self.root, text="Amount Paid (THB):").grid(row=4, column=0)
        tk.Entry(self.root, textvariable=self.amount_paid_var).grid(row=4, column=1)

        tk.Button(self.root, text="Calculate Change", command=self.calculate_change).grid(row=5, column=0, columnspan=2)
        tk.Label(self.root, text="Change (THB):").grid(row=6, column=0)
        tk.Entry(self.root, textvariable=self.change_var, state='readonly').grid(row=6, column=1)

        tk.Button(self.root, text="Sell Ticket", command=self.sell_ticket).grid(row=7, column=0, columnspan=2)

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




if __name__ == "__main__":
    root = tk.Tk()
    app = TrainTicketApp(root)
    root.mainloop()
