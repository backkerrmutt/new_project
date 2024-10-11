import tkinter as tk
from math import radians

stations = [
        "คูคต (N24)", "แยก คปอ. (N23)", "พิพิธภัณฑ์กองทัพอากาศ (N22)", "โรงพยาบาลภูมิพลอดุลยเดช (N21)",
        "สะพานใหม่ (N20)", "สายหยุด (N19)", "พหลโยธิน 59 (N18)", "วัดพระศรีมหาธาตุ (N17)",
        "กรมทหารราบที่ 11 (N16)", "บางบัว (N15)", "กรมป่าไม้ (N14)", "มหาวิทยาลัยเกษตรศาสตร์ (N13)",
        "เสนานิคม (N12)", "รัชโยธิน (N11)", "พหลโยธิน 24 (N10)", "ห้าแยกลาดพร้าว (N9)",
        "หมอชิต (N8)", "สะพานควาย (N7)", "เสนาร่วม (N6)", "อารีย์ (N5)",
        "สนามเป้า (N4)", "อนุสาวรีย์ชัยสมรภูมิ (N3)", "พญาไท (N2)", "ราชเทวี (N1)",
        "สยาม (CEN)", "ชิดลม (E1)", "เพลินจิต (E2)", "นานา (E3)",
        "อโศก (E4)", "พร้อมพงษ์ (E5)", "ทองหล่อ (E6)", "เอกมัย (E7)",
        "พระโขนง (E8)", "อ่อนนุช (E9)", "บางจาก (E10)", "ปุณณวิถี (E11)",
        "อุดมสุข (E12)", "บางนา (E13)", "แบริ่ง (E14)", "สำโรง (E15)",
        "ปู่เจ้า (E16)", "ช้างเอราวัณ (E17)", "โรงเรียนนายเรือ (E18)", "ปากน้ำ (E19)",
        "ศรีนครินทร์ (E20)", "แพรกษา (E21)", "สายลวด (E22)", "เคหะฯ (E23)"
    ]

# ตัวแปรเพื่อติดตามการเปลี่ยนแปลง


def create_widgets(self):

    #windown background color
    self.root.configure(bg='#FCFAEE')

    # สร้างตัวแปรสำหรับเก็บค่าที่เลือกขาไป
    selected_stationStart = tk.StringVar()
    selected_stationStart.set("สถานีต้นทาง")
    tk.Label(self.root, text="เลือกสถานี : " ,font=("Arial", 20), background="#DA8359", bd=10, relief="flat").place(x=20, y=50)
    option_menu = tk.OptionMenu(self.root, selected_stationStart, *stations )
    option_menu.place(x=200, y=55)
    option_menu.configure(background="#ECDFCC",font=("Arial", 20))
    self.start_station_var = selected_stationStart

    # สร้างตัวแปรสำหรับเก็บค่าที่เลือกขากลับ
    selected_stationEnd = tk.StringVar()
    selected_stationEnd.set("สถานีปลายทาง")
    tk.Label(self.root, text="เลือกสถานี : " ,font=("Arial", 20), background="#DA8359", bd=10, relief="flat").place(x=20, y=130)
    option_menu = tk.OptionMenu(self.root, selected_stationEnd, *stations)
    option_menu.place(x=200, y=130)
    option_menu.configure(background="#ECDFCC",font=("Arial", 20))
    self.end_station_var = selected_stationEnd

    selected_stationStart.trace_add("write", self.check_both_changed)
    selected_stationEnd.trace_add("write", self.check_both_changed)

    tk.Label(self.root, text="Distance :  " + "0" + "  Station" ,font=("Arial", 20), background="#ECDFCC", bd=10).place(x=20, y=210)
    tk.Label(self.root, text="Price Of Ticket  :  " + "0" + "  Bath" ,font=("Arial", 20), background="#ECDFCC", bd=10).place(x=20, y=290)


    # # สร้างปุ่มเพื่อแสดงค่าที่เลือก
    tk.Button(self.root, text="Buy Ticket" ,font=("Arial", 20), background="#A5B68D", bd=10, command=self.sell_ticket).place(x=200, y=400)
    tk.Button(self.root, text="History of tickets",font=("Arial", 20), background="#A5B68D", bd=10, command=self.Ticket_History).place(x=300, y=600)




