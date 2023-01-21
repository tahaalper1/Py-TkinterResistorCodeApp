import tkinter as tk
# -*- coding: utf-8 -*-
from tkinter import messagebox
from tkinter.ttk import Combobox
#messagebox ve combobox kullanabilmek için önceki projeden farklı olarak bunları ekledim.

form = tk.Tk()
form.title("Direnç Değeri Hesaplama")
form.config(bg="LightSteelBlue3")
form.geometry("950x800")
form.resizable(False, False)
#Burada bir form sayfası oluşturdum.


# label----------------------------------------------------------------------
label_4bant = tk.Label(form, text="4 BANTLI DİRENÇ BANTLARI", bg="LightSteelBlue3", fg="white",
                       font=("Comic Sans MS", 18))
label_4bant.place(x=10, y=75)

# Combobox-------------------------------------------------------------------
liste = ["Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Mor", "Gri", "Beyaz"]
kutu1 = Combobox(form, values=liste, font=("bold", 15))
kutu1.place(x=10, y=125, width=100)
#liste içine combobox kutumun içerisine koyacağım şeyleri ekledim.
#Combobox oluşturdum ve values kısmına liste verip içine listedeki değerleri yerleştirdim.
#Place komutuyla formda istediğim bir yere yerleştirdim ve width ile en boyunu verdim.

liste1 = ["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Mor", "Gri", "Beyaz"]
kutu2 = Combobox(form, values=liste1, font=("bold", 15))
kutu2.place(x=130, y=125, width=100)
liste2 = ["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Altın", "Gümüş"]
kutu3 = Combobox(form, values=liste2, font=("bold", 15))
kutu3.place(x=250, y=125, width=100)
liste3 = ["Kahverengi", "Kırmızı", "Altın", "Gümüş"]
kutu4 = Combobox(form, values=liste3, font=("bold", 15))
kutu4.place(x=370, y=125, width=100)

# button-----------------------------------------------------------
def hesapla():
    #Burada hesapla fonksiyonu oluşturdum. Kutuların boş veya dolu olduğunu kontrol ettim ve boş bırakıldığı
    #taktirde boş alanları doldurun diye bir mesaj yolladım.
    if (len(kutu1.get()) == 0 or len(kutu2.get()) == 0 or len(kutu3.get()) == 0 or len(kutu4.get()) == 0):
        messagebox.showinfo(title="Lütfen boş alan bırakmayın!!!", message="Boş alanları doldurun!!!")
    else:
    #Eğer boş alan yoksa hesap sonucunu ekrana getirdim.
    #Burada renklerin değerlerini tanımladım.
        sozluk1 = {"Siyah": 0, "Kahverengi": 1, "Kırmızı": 2, "Turuncu": 3, "Sarı": 4, "Yeşil": 5, "Mavi": 6, "Mor": 7,
                   "Gri": 8, "Beyaz": 9}
        sozluk2 = {"Siyah": 1, "Kahverengi": 10, "Kırmızı": 100, "Turuncu": 1000, "Sarı": 10000, "Yeşil": 100000,
                   "Mavi": 1000000, "Altın": 0.1,
                   "Gümüş": 0.01}
        sozluk3 = {"Kahverengi": 1, "Kırmızı": 2, "Altın": 5, "Gümüş": 10}

        deger1 = kutu1.get()
        deger2 = kutu2.get()
        deger3 = kutu3.get()
        deger4 = kutu4.get()
    #Bu kısımda 4 renkli direnç kodu okuyacağımız için comboboxtan aldığım renkleri deger1,deger2,deger3,deger4
    #olarak atama yaptım.

        hesap = str(sozluk1[deger1]) + str(sozluk1[deger2]) + "x" + str(sozluk2[deger3]) + "=" + str(
            sozluk1[deger1]) + str(sozluk1[deger2]) + str(sozluk2[deger3])[1:]+ "ohm"
        tolerans = "%" + str(sozluk3[deger4])
        label_sonuc = tk.Label(form, text="Hesap sonucu: " + hesap, bg="LightSteelBlue3", fg="white",
                               font=("Comic Sans MS", 24))
        label_sonuc.place(x=10, y=180)
        label_tolerans = tk.Label(form, text="Tolerans: " + tolerans, bg="LightSteelBlue3", fg="white",
                                  font=("Comic Sans MS", 24))
        label_tolerans.place(x=10, y=230)
    #Burda hesap sonucu hesaplanıyor ve labellara yazılyor. Bu kısım için biraz yardım aldım.
    #5 ve 6 renkli direnç renk kodu hesaplayıcılar içinde bu işlemleri kod halinde yazdım.

button1 = tk.Button(text="Hesapla", bg="LightSteelBlue3", fg="white", font=("Comic Sans MS", 18), command=hesapla)
button1.place(x=775, y=110)
#Hesapla butonu koydum ve butona basıldığında command kısmına hesapla fonksiyonu verdim.
#Butona basıldığında hesapla fonksiyonu çalışacak.


# ------------------------------------------------------------------------------------
# label----------------------------------------------------------------------
label_4bant = tk.Label(form, text="5 BANTLI DİRENÇ BANTLARI", bg="LightSteelBlue3", fg="white",
                       font=("Comic Sans MS", 18))
label_4bant.place(x=10, y=300)

# Combobox-------------------------------------------------------------------
liste4 = ["Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Mor", "Gri", "Beyaz"]
kutu5 = Combobox(form, values=liste, font=("bold", 15))
kutu5.place(x=10, y=375, width=100)
liste5 = ["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Mor", "Gri", "Beyaz"]
kutu6 = Combobox(form, values=liste1, font=("bold", 15))
kutu6.place(x=130, y=375, width=100)
liste6 = ["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Altın", "Gümüş"]
kutu7 = Combobox(form, values=liste2, font=("bold", 15))
kutu7.place(x=250, y=375, width=100)
liste7 = ["Kahverengi", "Kırmızı", "Altın", "Gümüş"]
kutu8 = Combobox(form, values=liste3, font=("bold", 15))
kutu8.place(x=370, y=375, width=100)
liste13 = ["Kahverengi", "Kırmızı", "Altın", "Gümüş"]
kutu13 = Combobox(form, values=liste3, font=("bold", 15))
kutu13.place(x=490, y=375, width=100)


# button-----------------------------------------------------------
def hesapla1():
    if (len(kutu5.get()) == 0 or len(kutu6.get()) == 0 or len(kutu7.get()) == 0 or len(kutu8.get()) == 0 or len(kutu13.get())==0):
        messagebox.showinfo(title="Lütfen boş alan bırakmayın!!!", message="Boş alanları doldurun!!!")
    else:
        sozluk4 = {"Siyah": 0, "Kahverengi": 1, "Kırmızı": 2, "Turuncu": 3, "Sarı": 4, "Yeşil": 5, "Mavi": 6, "Mor": 7,
                   "Gri": 8, "Beyaz": 9}
        sozluk5 = {"Siyah": 1, "Kahverengi": 10, "Kırmızı": 100, "Turuncu": 1000, "Sarı": 10000, "Yeşil": 100000,
                   "Mavi": 1000000, "Altın": 0.1,
                   "Gümüş": 0.01}
        sozluk6 = {"Kahverengi": 1, "Kırmızı": 2, "Altın": 5, "Gümüş": 10}

        deger5 = kutu5.get()
        deger6 = kutu6.get()
        deger7 = kutu7.get()
        deger8 = kutu8.get()
        deger13 = kutu13.get()

        hesap1 = str(sozluk4[deger5]) + str(sozluk4[deger6]) +str(sozluk4[deger7])+ "x" + str(sozluk5[deger8]) + "=" + str(sozluk4[deger5]) +str(sozluk4[deger6])+ str(sozluk4[deger7]) + str(sozluk5[deger7])[1:]+ "ohm"
        tolerans1 = "%" + str(sozluk6[deger13])
        label_sonuc1 = tk.Label(form, text="Hesap sonucu: " + hesap1, bg="LightSteelBlue3", fg="white",
                               font=("Comic Sans MS", 24))
        label_sonuc1.place(x=10, y=430)
        label_tolerans1 = tk.Label(form, text="Tolerans: " + tolerans1, bg="LightSteelBlue3", fg="white",
                                  font=("Comic Sans MS", 24))
        label_tolerans1.place(x=10, y=480)


button2 = tk.Button(text="Hesapla", bg="LightSteelBlue3", fg="white", font=("Comic Sans MS", 18), command=hesapla1)
button2.place(x=775, y=360)

# label----------------------------------------------------------------------
label_4bant = tk.Label(form, text="6 BANTLI DİRENÇ BANTLARI", bg="LightSteelBlue3", fg="white",
                       font=("Comic Sans MS", 18))
label_4bant.place(x=10, y=550)

# Combobox-------------------------------------------------------------------
liste8 = ["Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Mor", "Gri", "Beyaz"]
kutu9 = Combobox(form, values=liste, font=("bold", 15))
kutu9.place(x=10, y=625, width=100)
liste9 = ["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Mor", "Gri", "Beyaz"]
kutu10 = Combobox(form, values=liste1, font=("bold", 15))
kutu10.place(x=130, y=625, width=100)
liste10 = ["Siyah", "Kahverengi", "Kırmızı", "Turuncu", "Sarı", "Yeşil", "Mavi", "Altın", "Gümüş"]
kutu11 = Combobox(form, values=liste2, font=("bold", 15))
kutu11.place(x=250, y=625, width=100)
liste11 = ["Kahverengi", "Kırmızı", "Altın", "Gümüş"]
kutu12 = Combobox(form, values=liste3, font=("bold", 15))
kutu12.place(x=370, y=625, width=100)
liste12 = ["Kahverengi", "Kırmızı", "Altın", "Gümüş"]
kutu16 = Combobox(form, values=liste3, font=("bold", 15))
kutu16.place(x=490, y=625, width=100)
liste15 = ["Kahverengi", "Kırmızı", "Altın", "Gümüş"]
kutu15 = Combobox(form, values=liste3, font=("bold", 15))
kutu15.place(x=610, y=625, width=100)




# button-----------------------------------------------------------
def hesapla():
    if (len(kutu9.get()) == 0 or len(kutu10.get()) == 0 or len(kutu11.get()) == 0 or len(kutu12.get()) == 0 or len(kutu12.get())==0 or len(kutu15.get())==0):
        messagebox.showinfo(title="Lütfen boş alan bırakmayın!!!", message="Boş alanları doldurun!!!")
    else:
        sozluk7 = {"Siyah": 0, "Kahverengi": 1, "Kırmızı": 2, "Turuncu": 3, "Sarı": 4, "Yeşil": 5, "Mavi": 6, "Mor": 7,
                   "Gri": 8, "Beyaz": 9}
        sozluk8 = {"Siyah": 1, "Kahverengi": 10, "Kırmızı": 100, "Turuncu": 1000, "Sarı": 10000, "Yeşil": 100000,
                   "Mavi": 1000000, "Altın": 0.1,
                   "Gümüş": 0.01}
        sozluk9 = {"Kahverengi": 1, "Kırmızı": 2, "Altın": 5, "Gümüş": 10}
        sozluk10 = {"Siyah":250, "Kahverengi":100, "Kırmızı":50, "Turuncu":15, "Sarı":25, "Yeşil":20, "Mavi":10, "Mor":5, "Gri": 1}


        deger9 = kutu9.get()
        deger10 = kutu10.get()
        deger11 = kutu11.get()
        deger12 = kutu12.get()
        deger15 = kutu15.get()
        deger16 = kutu16.get()

        hesap2 = str(sozluk7[deger9]) + str(sozluk7[deger10]) +str(sozluk7[deger11])+ "x" + str(sozluk8[deger12]) + "=" + str(sozluk7[deger9]) + str(sozluk7[deger10]) +str(sozluk7[deger11])+ str(sozluk8[deger11])[1:]+ "ohm"
        tolerans2 = "%" + str(sozluk9[deger16])
        label_sonuc2 = tk.Label(form, text="Hesap sonucu: " + hesap2, bg="LightSteelBlue3", fg="white",
                               font=("Comic Sans MS", 24))
        label_sonuc2.place(x=10, y=670)
        label_tolerans2 = tk.Label(form, text="Tolerans: " + tolerans2, bg="LightSteelBlue3", fg="white",
                                  font=("Comic Sans MS", 24))
        label_tolerans2.place(x=10, y=720)


button3 = tk.Button(text="Hesapla", bg="LightSteelBlue3", fg="white", font=("Comic Sans MS", 18), command=hesapla)
button3.place(x=775, y=610)

# ---------------------------------------------------------------------------------------------------

form.mainloop()
