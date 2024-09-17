import tkinter as tk
from tkinter import ttk
import requests

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/THB"
    response = requests.get(url)
    data = response.json()
    return data["rates"]["USD"]

def convert_currency():
    thb_amount = float(thb_entry.get())
    exchange_rate = get_exchange_rate()
    usd_amount = thb_amount * exchange_rate
    result_label.config(text=f"{usd_amount:.2f} USD")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Currency Converter")

# สร้างและจัดวางวิดเจ็ต
thb_label = ttk.Label(root, text="Amount in THB:")
thb_label.grid(column=0, row=0, padx=10, pady=10)

thb_entry = ttk.Entry(root)
thb_entry.grid(column=1, row=0, padx=10, pady=10)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="Result in USD:")
result_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# เริ่มการทำงานของ GUI
root.mainloop()