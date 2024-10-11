import tkinter as tk
from locale import windows_locale
from tkinter import messagebox

from requests import delete

import GUI as cr
from Rate_Of_Between_Station import Rate_Cal
from Ticket import Ticket
from tkinter import simpledialog
import openpyxl



class TrainTicketApp:

    #Data for calculation---------------------------------------------
    locations = [
        ("คูคต (N24)", 1),("แยก คปอ. (N23)", 2),("พิพิธภัณฑ์กองทัพอากาศ (N22)", 3),("โรงพยาบาลภูมิพลอดุลยเดช (N21)", 4),("สะพานใหม่ (N20)", 5),("สายหยุด (N19)", 6),
        ("พหลโยธิน 59 (N18)", 7),("วัดพระศรีมหาธาตุ (N17)", 8),("กรมทหารราบที่ 11 (N16)", 9),("บางบัว (N15)", 10),("กรมป่าไม้ (N14)", 11),("มหาวิทยาลัยเกษตรศาสตร์ (N13)", 12),
        ("เสนานิคม (N12)", 13),("รัชโยธิน (N11)", 14),("พหลโยธิน 24 (N10)", 15),("ห้าแยกลาดพร้าว (N9)", 16),("หมอชิต (N8)", 17),("สะพานควาย (N7)", 18),("เสนาร่วม (N6)", 19),
        ("อารีย์ (N5)", 20),("สนามเป้า (N4)", 21),("อนุสาวรีย์ชัยสมรภูมิ (N3)", 22),("พญาไท (N2)", 23),("ราชเทวี (N1)", 24),("สยาม (CEN)", 25),("ชิดลม (E1)", 26),("เพลินจิต (E2)", 27),
        ("นานา (E3)", 28),("อโศก (E4)", 29),("พร้อมพงษ์ (E5)", 30),("ทองหล่อ (E6)", 31),("เอกมัย (E7)", 32),("พระโขนง (E8)", 33),("อ่อนนุช (E9)", 34),("บางจาก (E10)", 35),
        ("ปุณณวิถี (E11)", 36),("อุดมสุข (E12)", 37),("บางนา (E13)", 38),("แบริ่ง (E14)", 39),("สำโรง (E15)", 40),("ปู่เจ้า (E16)", 41),("ช้างเอราวัณ (E17)", 42),
        ("โรงเรียนนายเรือ (E18)", 43),("ปากน้ำ (E19)", 44),("ศรีนครินทร์ (E20)", 45),("แพรกษา (E21)", 46),("สายลวด (E22)", 47),("เคหะฯ (E23)", 48)]

    def __init__(self, root):
        self.root = root
        self.root.title("Train Ticket Application")

        self.start_station_var = tk.StringVar()
        self.end_station_var = tk.StringVar()
        self.distance_var = tk.IntVar()
        self.price_var = tk.IntVar()
        self.amount_paid_var = tk.IntVar()
        self.change_var = tk.IntVar()
        self.tickets = []

        cr.create_widgets(self)

    # คำนวนหาค่าโดยสารตามระยะสถานี
    def calculate_price(self):
        s_station = self.cel_distance(self.start_station_var.get())
        e_station = self.cel_distance(self.end_station_var.get())
        self.price_var = Rate_Cal(s_station, e_station)
        tk.Label(self.root, text="Price Of Ticket  :  " + str(self.price_var) + "  Baht" ,font=("Arial", 20), background="#ECDFCC", bd=10).place(x=20, y=290)

    # ติดตามการเปลี่ยนแปลงการเลือกสถานีใน DropDown-List
    def check_both_changed(self, *args):
        start_station = self.cel_distance(self.start_station_var.get())
        end_station = self.cel_distance(self.end_station_var.get())

        if start_station is not None and end_station is not None:
            self.distance_var = (abs(start_station - end_station))
            tk.Label(self.root, text="Distance  :  " + str(self.distance_var) + "  Station" ,font=("Arial", 20), background="#ECDFCC", bd=10).place(x=20, y=210)
            self.calculate_price()

    # ขายตั๋ว
    def sell_ticket(self):
        self.amount_paid_var = simpledialog.askinteger("Make a payment", "Please enter your amount paid:")

        if self.amount_paid_var < self.price_var:
            messagebox.showerror("Error", "Insufficient amount paid")
            return
        elif not self.start_station_var.get() or not self.end_station_var.get()  or not self.price_var or not self.amount_paid_var:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        # ถอนเงิน
        self.change_var = self.amount_paid_var - self.price_var

        #History of ticket
        Tic = Ticket(self.start_station_var.get(), self.end_station_var.get(), self.distance_var, self.price_var)
        self.tickets.append(Tic)
        Tic.Save_To_Excel()

        # แสดงผลการชื้อ เมื่อซื้อสำเร็จ
        messagebox.showinfo("Success", f"Ticket bought successfully \n Change : {self.change_var}  Baht")
        self.clear_fields()

    # ดูข้อมูลการขายตั๋ว
    def Ticket_History(self, *args):
        # Prompt for username and password
        username = simpledialog.askstring("Login", "Enter username:")
        password = simpledialog.askstring("Login", "Enter password:", show='*')
        mywindows = tk.Tk()
        row = 0
        if username == "admin" and password == "admin":
            mywindows.title("Ticket History")
            # mywindows.geometry("600x700+800+50")
            try:
                # Load the workbook and select the active worksheet
                workbook = openpyxl.load_workbook('excel/ticket_info.xlsx')
                sheet = workbook.active

             # Iterate through the rows and print the data
                for row_idx, row in enumerate(sheet.iter_rows(values_only=True)):
                    for col_idx, value in enumerate(row):
                        tk.Label(mywindows, text=value, font=("Arial", 12)).grid(row=row_idx, column=col_idx)
                    row = row_idx + 1

            except FileNotFoundError:
                print(f"File not found: {'ticket_info.xlsx'}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")
        if self.tickets:
            self.delete_history(mywindows,row)
        else:
            return

    def delete_history (self,mywindows_root,row):
        tk.Button(mywindows_root, text="History of tickets", font=("Arial", 10),command=lambda: self.tickets[0].delete_all_data()).grid(row=row, column=4, sticky='se', padx=10, pady=10)

    # ลบข้อมูลเมื่อกดซื้อสำเร็จ
    def clear_fields(self):
        self.start_station_var.set("")
        self.end_station_var.set("")
        self.distance_var = 0
        self.price_var = 0
        self.amount_paid_var = 0
        self.change_var = 0

    # หาค่าของสถานี เพื่อใช้ในการคำนวณระยะห่างระหว่างสถานี
    def cel_distance(self, find_station):
        for key, value in self.locations:
            if key == find_station:
                return value





