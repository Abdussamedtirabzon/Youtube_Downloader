import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def indir():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Hata", "Lütfen bir YouTube linki girin.")
        return

    # İndirme klasörünü belirle (Müzik klasörü veya mevcut dizin)
    kayit_yeri = os.path.join(os.path.expanduser("~"), "Music")
    
    try:
        # yt-dlp komutunu terminaldeki gibi Python üzerinden çağırıyoruz
        # Dışarıdan kütüphane eklemek yerine kurulu olan yt-dlp scriptini kullanır
        komut = [
            "python3", "-m", "yt_dlp", 
            "-x", 
            "--audio-format", "mp3", 
            "--audio-quality", "0",
            "-o", f"{kayit_yeri}/%(title)s.%(ext)s",
            url
        ]
        
        lbl_durum.config(text="İndiriliyor... Lütfen bekleyin.", fg="blue")
        pencere.update()
        
        subprocess.run(komut, check=True)
        
        lbl_durum.config(text="Tamamlandı!", fg="green")
        messagebox.showinfo("Başarılı", f"Dosya Müzik klasörüne kaydedildi:\n{kayit_yeri}")
        
    except Exception as e:
        lbl_durum.config(text="Hata oluştu!", fg="red")
        messagebox.showerror("Hata", f"İndirme sırasında bir sorun oluştu:\n{e}")

# Arayüz Oluşturma
pencere = tk.Tk()
pencere.title("YT MP3 İndirici")
pencere.geometry("450x200")

tk.Label(pencere, text="YouTube Video Linkini Yapıştır:", font=("Arial", 11)).pack(pady=10)

entry_url = tk.Entry(pencere, width=50)
entry_url.pack(pady=5)

btn_indir = tk.Button(pencere, text="MP3 Olarak İndir", command=indir, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_indir.pack(pady=20)

lbl_durum = tk.Label(pencere, text="")
lbl_durum.pack()

pencere.mainloop()