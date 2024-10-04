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

    #Data for calculation---------------------------------------------
    locations = [
        ("คูคต (N24)", 1),
        ("แยก คปอ. (N23)", 2),
        ("พิพิธภัณฑ์กองทัพอากาศ (N22)", 3),
        ("โรงพยาบาลภูมิพลอดุลยเดช (N21)", 4),
        ("สะพานใหม่ (N20)", 5),
        ("สายหยุด (N19)", 6),
        ("พหลโยธิน 59 (N18)", 7),
        ("วัดพระศรีมหาธาตุ (N17)", 8),
        ("กรมทหารราบที่ 11 (N16)", 9),
        ("บางบัว (N15)", 10),
        ("กรมป่าไม้ (N14)", 11),
        ("มหาวิทยาลัยเกษตรศาสตร (N13)", 12),
        ("เสนานิคม (N12)", 13),
        ("รัชโยธิน (N11)", 14),
        ("พหลโยธิน 24 (N10)", 15),
        ("ห้าแยกลาดพร้าว (N9)", 16),
        ("หมอชิต (N8)", 17),
        ("สะพานควาย (N7)", 18),
        ("เสนาร่วม (N6)", 19),
        ("อารีย์ (N5)", 20),
        ("สนามเป้า (N4)", 21),
        ("อนุสาวรีย์ชัยสมรภูมิ (N3)", 22),
        ("พญาไท (N2)", 23),
        ("ราชเทวี (N1)", 24),
        ("สยาม (CEN)", 25),
        ("ชิดลม (E1)", 26),
        ("เพลินจิต (E2)", 27),
        ("นานา (E3)", 28),
        ("อโศก (E4)", 29),
        ("พร้อมพงษ์ (E5)", 30),
        ("ทองหล่อ (E6)", 31),
        ("เอกมัย (E7)", 32),
        ("พระโขนง (E8)", 33),
        ("อ่อนนุช (E9)", 34),
        ("บางจาก (E10)", 35),
        ("ปุณณวิถี (E11)", 36),
        ("อุดมสุข (E12)", 37),
        ("บางนา (E13)", 38),
        ("แบริ่ง (E14)", 39),
        ("สำโรง (E15)", 40),
        ("ปู่เจ้า (E16)", 41),
        ("ช้างเอราวัณ (E17)", 42),
        ("โรงเรียนนายเรือ (E18)", 43),
        ("ปากน้ำ (E19)", 44),
        ("ศรีนครินทร์ (E20)", 45),
        ("แพรกษา (E21)", 46),
        ("สายลวด (E22)", 47),
        ("เคหะฯ (E23)", 48)
    ]


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


