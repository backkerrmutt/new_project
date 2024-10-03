import tkinter as tk

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