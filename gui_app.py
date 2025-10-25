import tkinter as tk
from tkinter import messagebox
from places_finder import find_places

def run_search():
    city = city_entry.get()
    api_key = api_key_entry.get()
    if not city or not api_key:
        messagebox.showerror("خطأ", "من فضلك أدخل اسم المدينة و API Key")
        return
    messagebox.showinfo("جاري المعالجة", "سيبدأ الآن البحث عن مواقع بدون بيانات اتصال..")
    find_places(api_key, city)

root = tk.Tk()
root.title("Find Missing Contact Places")

tk.Label(root, text="API Key:").pack()
api_key_entry = tk.Entry(root, width=50)
api_key_entry.pack()

tk.Label(root, text="City:").pack()
city_entry = tk.Entry(root, width=50)
city_entry.pack()

tk.Button(root, text="Start Search", command=run_search).pack(pady=10)

root.mainloop()
