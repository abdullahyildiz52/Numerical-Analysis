import tkinter as tk

def f(x):
    return x*x - 4*x - 10

def bisection(a, b, hata):
    if f(a) * f(b) >= 0:
        return None

    c = a
    while (b-a) >= hata:
        c = (a+b)/2

        if f(c) == 0.0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    return c

def hesapla():
    a = -200
    b = 300
    hata = 0.0001
    kok = bisection(a, b, hata)
    if kok is not None:
        label_kok.config(text="Kök: " + str(kok))
    else:
        label_kok.config(text="Bu aralıkta kök yok")

# Arayüzü oluştur
root = tk.Tk()
root.title("Kök Bulma Uygulaması")

label_baslik = tk.Label(root, text="Kök Bulma Uygulaması")
label_baslik.pack()

button_hesapla = tk.Button(root, text="Kökü Hesapla", command=hesapla)
button_hesapla.pack()

label_kok = tk.Label(root, text="x*x-5")
label_kok.pack()

root.mainloop()
