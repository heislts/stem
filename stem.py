import math
import tkinter as tk
from datetime import date
from tkinter import messagebox



def day_of_year(day, month, year=2024): #Tính số thứ tự của ngày trong năm
    return (date(year, month, day) - date(year, 1, 1)).days + 1


def solar_declination(n): #Tính độ lệch Mặt Trời (δ) theo ngày trong năm. Công thức gần đúng (đơn vị: radian)
    return math.radians(23.44) * math.sin(
        math.radians(360 / 365 * (n - 81))
    )


def day_night_length(latitude, day, month): #Tính số giờ ban ngày và ban đêm latitude: vĩ độ (độ, Bắc dương – Nam âm)
    phi = math.radians(latitude) #đổi độ sang radian của vĩ độ 
    n = day_of_year(day, month)
    delta = solar_declination(n)

    cos_h = -math.tan(phi) * math.tan(delta)

    if cos_h >= 1:
        day_length = 0
    elif cos_h <= -1:
        day_length = 24
    else:
        h = math.acos(cos_h)
        day_length = 2 * math.degrees(h) / 15

    night_length = 24 - day_length
    return round(day_length, 2), round(night_length, 2) #làm tròn 2 chữ số sau dấu phẩy 

#Tính toán 

def calculate():
    try:
        lat = float(entry_lat.get())
        day = int(entry_day.get())
        month = int(entry_month.get())

        day_length, night_length = day_night_length(lat, day, month) # thế giá trị nhập ban đâu đầu vào hàm 

        result_label.config(
            text=f"🌞 Ban ngày: {day_length} giờ\n🌙 Ban đêm: {night_length} giờ"
        )
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập dữ liệu hợp lệ!")

# Dao diện 

root = tk.Tk()
root.title("Ứng dụng tính độ dài ngày – đêm") #Tiêu đề
root.geometry("720x600") #Kích cỡ ban đầu
root.resizable(True, True) #Có thể điều chỉnh độ dày trục x, y 

#Tiêu đề, ô nhập dữ liệu, nút bấm

tk.Label(root, text="TÍNH ĐỘ DÀI NGÀY / ĐÊM", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Vĩ độ (°):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_lat = tk.Entry(frame)
entry_lat.grid(row=0, column=1)

tk.Label(frame, text="Ngày:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_day = tk.Entry(frame)
entry_day.grid(row=1, column=1)

tk.Label(frame, text="Tháng:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_month = tk.Entry(frame)
entry_month.grid(row=2, column=1)

tk.Button(root, text="TÍNH TOÁN", command=calculate, width=15).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
