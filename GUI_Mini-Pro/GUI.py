import tkinter as tk

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

    # สร้างตัวแปรสำหรับเก็บค่าที่เลือกขาไป
    selected_stationStart = tk.StringVar()
    selected_stationStart.set("สถานีต้นทาง")
    tk.Label(self.root, text="เลือกสถานี : ").grid(row=0, column=0)
    option_menu = tk.OptionMenu(self.root, selected_stationStart, *stations)
    option_menu.grid(row=0, column=1)
    self.start_station_var = selected_stationStart

    # สร้างตัวแปรสำหรับเก็บค่าที่เลือกขากลับ
    selected_stationEnd = tk.StringVar()
    selected_stationEnd.set("สถานีปลายทาง")
    tk.Label(self.root, text="เลือกสถานี : ").grid(row=1, column=0)
    option_menu = tk.OptionMenu(self.root, selected_stationEnd, *stations)
    option_menu.grid(row=1, column=1)
    self.end_station_var = selected_stationEnd

    selected_stationStart.trace_add("write", self.check_both_changed)
    selected_stationEnd.trace_add("write", self.check_both_changed)

    tk.Label(self.root, text="Distance : "  + " 0 " + " Station").grid(row=2, column=0)
    tk.Label(self.root, text="Price Of Ticket   :  " + "0" + " Bath").grid(row=3, column=0)



    # สร้างปุ่มเพื่อแสดงค่าที่เลือก
    tk.Button(self.root, text="Buy Ticket", command=self.sell_ticket).grid(row=5, column=0)

    tk.Button(self.root, text="History of tickets", command=self.Ticket_History).grid(row=6, column=3)



