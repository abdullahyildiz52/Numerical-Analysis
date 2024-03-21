import tkinter as tk

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection(f, a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < tol:
            return c
    print("Maximum iterations reached. No convergence.")
    return None

def calculate_root():
    func_str = entry_func.get()
    f = lambda x: eval(func_str)
    a = float(entry_a.get())
    b = float(entry_b.get())
    tol = float(entry_tol.get())
    max_iter = int(entry_max_iter.get())
    root = bisection(f, a, b, tol, max_iter)
    if root is not None:
        result_label.config(text="Bulunan kök: " + str(root))
    else:
        result_label.config(text="Kök bulunamadı.")

# Arayüzü oluştur
root = tk.Tk()
root.title("Kiriş Yöntemi ile Kök Bulma")

label_func = tk.Label(root, text="Fonksiyonu giriniz (örn. x**3 - 6*x**2 + 11*x - 6):")
label_func.pack()
entry_func = tk.Entry(root)
entry_func.pack()

label_a = tk.Label(root, text="Aralık başlangıç değeri a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Aralık bitiş değeri b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_tol = tk.Label(root, text="Toleransı giriniz (örn. 1e-6):")
label_tol.pack()
entry_tol = tk.Entry(root)
entry_tol.pack()

label_max_iter = tk.Label(root, text="Maksimum iterasyon sayısını giriniz:")
label_max_iter.pack()
entry_max_iter = tk.Entry(root)
entry_max_iter.pack()

calculate_button = tk.Button(root, text="Kökü Hesapla", command=calculate_root)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
