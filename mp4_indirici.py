import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def indir():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Uyarı", "Lütfen bir link girin!")
        return

    # Dosyayı senin 'Videolar' klasörüne kaydedecek şekilde ayarladım
    kayit_yolu = os.path.join(os.path.expanduser("~"), "Videolar")
    
    try:
        # Fedora sistemindeki yt-dlp yolu
        yt_dlp_path = os.path.expanduser("~/.local/bin/yt-dlp")
        
        # Video için en iyi kalite (bestvideo+bestaudio) parametreleri
        komut = [
            yt_dlp_path, 
            "-f", "bv+ba/b", # En iyi video ve sesi birleştir, olmazsa en iyi tek dosyayı al
            "--merge-output-format", "mp4", # Çıktıyı mp4 olarak birleştir
            "-o", f"{kayit_yolu}/%(title)s.%(ext)s",
            url
        ]
        
        lbl_durum.config(text="Video indiriliyor... Lütfen bekleyin.", fg="blue")
        pencere.update()
        
        subprocess.run(komut, check=True)
        
        lbl_durum.config(text="Tamamlandı!", fg="green")
        messagebox.showinfo("Başarılı", f"Video 'Videolar' klasörüne kaydedildi.")
        
    except Exception as e:
        lbl_durum.config(text="Hata oluştu!", fg="red")
        messagebox.showerror("Hata", f"İndirme sırasında bir sorun oluştu:\n{e}")

# Arayüz Oluşturma
pencere = tk.Tk()
pencere.title("Fedora Video Downloader")
pencere.geometry("450x220")

tk.Label(pencere, text="YouTube Video Linki:", font=("Arial", 11)).pack(pady=15)

entry_url = tk.Entry(pencere, width=50)
entry_url.pack(pady=5)

# Buton rengini videoyu temsil etmesi için mavi yaptım
btn_indir = tk.Button(pencere, text="Videoyu İndir (MP4)", command=indir, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_indir.pack(pady=20)

lbl_durum = tk.Label(pencere, text="")
lbl_durum.pack()

pencere.mainloop()