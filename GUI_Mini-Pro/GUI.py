import tkinter as tk

# สร้างหน้าต่างหลัก
root = tk.Tk()

#ขนากหน้าต่างหลัก
root.geometry("500x500")

root.title("Tkinter Demo")

# สร้าง label
label = tk.Label(root, text="Hello from Tkinter")
label.pack()

# สร้างปุ่ม
button = tk.Button(root, text="OK", command=root.quit )
button.place(x=230, y=460)


# เริ่มต้น main loop
root.mainloop()
