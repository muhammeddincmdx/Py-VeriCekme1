import socket
import time
import requests
from bs4 import BeautifulSoup
import tkinter as tk

def update_data():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.google.com", 80))
        s.close()
        
        url = "https://www.doviz.com/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content,"html.parser")
        
        altindata = soup.find("span", {"data-socket-key": "gram-altin"}).text
        dolardata = soup.find("span", {"data-socket-key": "USD"}).text
        eurodata = soup.find("span", {"data-socket-key": "EUR"}).text
        bistdata = soup.find("span", {"data-socket-key": "XU100"}).text
        
        gramaltinvalue.config(text=f"Gram Altın: {altindata} ₺")
        dolarvalue.config(text=f"Dolar: {dolardata} ₺")
        eurovalue.config(text=f"Euro: {eurodata} ₺")
        bistvalue.config(text=f"BIST100: {bistdata}")
        
        # Saat ve tarih bilgisini güncelle
        current_time = time.strftime("%d-%m-%Y %H:%M")
        timelabel.config(text=current_time)
        
        window.after(60000, update_data)  # 60000 milisaniye = 60 saniye (1 dakika)
    except Exception as e:
        print("Bir hata oluştu:", e)

# Ana pencere oluştur
window = tk.Tk()
window.geometry("310x270")
window.title("Borsa Takip")

# Başlık etiketi
label = tk.Label(window, text="Borsa Takip", font=("Helvetica", 16))
label.pack(pady=10)

# Tarih ve saat etiketi
timelabel = tk.Label(window, text="", font=("Helvetica", 10))
timelabel.pack()

# Gram Altın etiketi
gramaltinvalue = tk.Label(window, text="", font=("Helvetica", 12))
gramaltinvalue.pack()

# Dolar etiketi
dolarvalue = tk.Label(window, text="", font=("Helvetica", 12))
dolarvalue.pack()

# Euro etiketi
eurovalue = tk.Label(window, text="", font=("Helvetica", 12))
eurovalue.pack()

# BIST100 etiketi
bistvalue = tk.Label(window, text="", font=("Helvetica", 12))
bistvalue.pack()

# Verileri güncelle
update_data()  # İlk veri güncellemesi

# Pencereyi göster
window.mainloop()
