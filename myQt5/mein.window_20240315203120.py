import tkinter as tk
from tkinter import messagebox

class AnaSayfa(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spor Lisans Başvuru Formu")
        self.geometry("400x300")
        self.configure(bg="lightblue")
        
        # Giriş alanları ve etiketler
        self.kur_giris_alanlari()
        
        # Devam butonu
        self.button_devam = tk.Button(self, text="Devam", bg="green", fg="white", command=self.spor_bilgileri_sayfasi_olustur)
        self.button_devam.pack(pady=(20, 20))

    def kur_giris_alanlari(self):
        alanlar = [("Ad Soyad", "entry_ad_soyad"), ("TC Kimlik No", "entry_tc_no"), 
                   ("Doğum Tarihi", "entry_dogum_tarihi"), ("Anne Adı", "entry_anne_adi"), 
                   ("Baba Adı", "entry_baba_adi")]

        for metin, alan_adi in alanlar:
            setattr(self, "label_" + alan_adi, tk.Label(self, text=metin + ":", bg="lightblue"))
            getattr(self, "label_" + alan_adi).pack(pady=(10, 5))
            setattr(self, alan_adi, tk.Entry(self))
            getattr(self, alan_adi).pack(pady=5)

    def spor_bilgileri_sayfasi_olustur(self):
        if all(getattr(self, attr).get() for attr in ['entry_ad_soyad', 'entry_tc_no', 'entry_dogum_tarihi', 'entry_anne_adi', 'entry_baba_adi']):
            self.withdraw()  # AnaSayfa penceresini gizle

            # Spor bilgileri penceresi
            self.spor_pencere = tk.Toplevel(self)
            self.spor_pencere.title("Spor Bilgileri")
            self.spor_pencere.geometry("400x300")
            self.spor_pencere.configure(bg="lightblue")
            
            # Lisans ve spor bilgileri giriş alanları
            self.kur_spor_giris_alanlari(self.spor_pencere)
            
            # Devam butonu
            self.button_spor_devam = tk.Button(self.spor_pencere, text="Devam", bg="green", fg="white", command=self.islem_sonu)
            self.button_spor_devam.pack(pady=(20, 20))

        else:
            messagebox.showerror("Hata", "Lütfen tüm bilgileri giriniz.")

    def kur_spor_giris_alanlari(self, pencere):
        alanlar = [("Lisans Türü", "entry_lisans_turu"), ("Federasyon", "entry_federasyon"), 
                   ("Spor Branşı", "entry_spor_bilgileri")]

        for metin, alan_adi in alanlar:
            setattr(self, "label_" + alan_adi, tk.Label(pencere, text=metin + ":", bg="lightblue"))
            getattr(self, "label_" + alan_adi).pack(pady=(10, 5))
            setattr(self, alan_adi, tk.Entry(pencere))
            getattr(self, alan_adi).pack(pady=5)

    def islem_sonu(self):
        if all(getattr(self, attr).get() for attr in ['entry_lisans_turu', 'entry_federasyon', 'entry_spor_bilgileri']):
            # İşlem sonu mesajı ve butonu
            self.sonuc_pencere = tk.Toplevel(self)
            self.sonuc_pencere.title("İşlem Sonu")
            self.sonuc_pencere.geometry("400x300")
            self.sonuc_pencere.configure(bg="lightblue")
            
            # Mesaj
            label_sonuc = tk.Label(self.sonuc_pencere, text="Lisans başvurunuz başarıyla tamamlandı", bg="lightblue", font=("Arial", 12))
            label_sonuc.pack(pady=(100, 20))

            # İşlem Sonu butonu
            button_islem_sonu = tk.Button(self.sonuc_pencere, text="İşlem Sonu", bg="green", fg="white", command=self.sonuc_pencere.destroy)
            button_islem_sonu.pack()

            # Center the button and message in the window
            self.center_window(self.sonuc_pencere)

            # Close the third page when the button is clicked
            self.sonuc_pencere.protocol("WM_DELETE_WINDOW", self.spor_pencere.destroy)

        else:
            messagebox.showerror("Hata", "Lütfen tüm spor bilgilerini giriniz.")

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    app = AnaSayfa()
    app.mainloop()