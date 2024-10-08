import tkinter as tk
from tkinter import messagebox
import GUI as cr
from Rate_Of_Between_Station import Rate_Cal
from Ticket import Ticket



class TrainTicketApp:

    start_changed = False
    end_changed = False

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
        self.index_tic = 0
        cr.create_widgets(self)

    #Data for calculation---------------------------------------------
    locations = [
        ("คูคต (N24)", 1),("แยก คปอ. (N23)", 2),("พิพิธภัณฑ์กองทัพอากาศ (N22)", 3),("โรงพยาบาลภูมิพลอดุลยเดช (N21)", 4),("สะพานใหม่ (N20)", 5),("สายหยุด (N19)", 6),
        ("พหลโยธิน 59 (N18)", 7),("วัดพระศรีมหาธาตุ (N17)", 8),("กรมทหารราบที่ 11 (N16)", 9),("บางบัว (N15)", 10),("กรมป่าไม้ (N14)", 11),("มหาวิทยาลัยเกษตรศาสตร์ (N13)", 12),
        ("เสนานิคม (N12)", 13),("รัชโยธิน (N11)", 14),("พหลโยธิน 24 (N10)", 15),("ห้าแยกลาดพร้าว (N9)", 16),("หมอชิต (N8)", 17),("สะพานควาย (N7)", 18),("เสนาร่วม (N6)", 19),
        ("อารีย์ (N5)", 20),("สนามเป้า (N4)", 21),("อนุสาวรีย์ชัยสมรภูมิ (N3)", 22),("พญาไท (N2)", 23),("ราชเทวี (N1)", 24),("สยาม (CEN)", 25),("ชิดลม (E1)", 26),("เพลินจิต (E2)", 27),
        ("นานา (E3)", 28),("อโศก (E4)", 29),("พร้อมพงษ์ (E5)", 30),("ทองหล่อ (E6)", 31),("เอกมัย (E7)", 32),("พระโขนง (E8)", 33),("อ่อนนุช (E9)", 34),("บางจาก (E10)", 35),
        ("ปุณณวิถี (E11)", 36),("อุดมสุข (E12)", 37),("บางนา (E13)", 38),("แบริ่ง (E14)", 39),("สำโรง (E15)", 40),("ปู่เจ้า (E16)", 41),("ช้างเอราวัณ (E17)", 42),
        ("โรงเรียนนายเรือ (E18)", 43),("ปากน้ำ (E19)", 44),("ศรีนครินทร์ (E20)", 45),("แพรกษา (E21)", 46),("สายลวด (E22)", 47),("เคหะฯ (E23)", 48)]

    def calculate_change(self):
        s_station = self.cel_distance(self.start_station_var.get())
        e_station = self.cel_distance(self.end_station_var.get())
        self.price_var = Rate_Cal(s_station, e_station)
        tk.Label(self.root, text="Price Of Ticket   :  " + str(self.price_var) + " Bath").grid(row=3, column=0)
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


        # History of ticket
        self.tickets[self.index_tic] = Ticket(start_station, end_station, distance, price)
        self.tickets[self.index_tic].Display_Ticket()
        self.index_tic = self.index_tic + 1


        messagebox.showinfo("Success", "Ticket sold successfully")
        self.clear_fields()

    def clear_fields(self):
        self.start_station_var.set("")
        self.end_station_var.set("")
        self.distance_var.set(0)
        self.price_var.set(0)
        self.amount_paid_var.set(0)
        self.change_var.set(0)

    def show_selected(self):

        result_text = f"Selected Start Station: {self.start_station_var.get()} Selected End Station: {self.end_station_var.get()}"
        print(result_text)
        start_station = self.cel_distance(self.start_station_var.get())
        end_station = self.cel_distance(self.end_station_var.get())
        print(start_station, end_station)

        if start_station is not None and end_station is not None:
            self.distance_var.set(abs(start_station - end_station))
            print(f"distace : {self.distance_var.get()} station")
            self.calculate_change()
        else:
            print("Error: One of the stations is None")

    def cel_distance(self, find_station):
        for key, value in self.locations:
            if key == find_station:
                return value

    # ตรวจสอบการเปลี่ยนแปลงของ start , end
    def on_start_change(self, *args):
        global start_changed
        start_changed = True
        self.check_both_changed()

    def on_end_change(self, *args):
        global end_changed
        end_changed = True
        self.check_both_changed()

    def check_both_changed(self):
        global start_changed, end_changed
        start_station = self.cel_distance(self.start_station_var.get())
        end_station = self.cel_distance(self.end_station_var.get())

        if start_station is not None and end_station is not None:
            self.distance_var = (abs(start_station - end_station))
            if start_changed and end_changed:
                start_changed = False
                end_changed = False
                tk.Label(self.root, text="Distance : " + str(self.distance_var) + "Station").grid(row=2, column=0)

            self.calculate_change()
        else:
            return


