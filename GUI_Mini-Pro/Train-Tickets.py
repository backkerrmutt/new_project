import tkinter as tk

# สร้างหน้าต่างหลัก
root = tk.Tk()

#ขนากหน้าต่างหลัก
root.geometry("430x740")

root.title("MRT")

# สร้าง label
label = tk.Label(root, text="Train Tickets")
label.pack()

# สร้างปุ่ม
Bt_Submit = tk.Button(root, text="OK", command=root.quit ,padx=20, pady=5).place(x=0.5, y=0.85)

# เริ่มต้น main loop
root.mainloop()
