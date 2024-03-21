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

# Kullanıcıdan fonksiyonu ve aralığı alma
func_str = input("Fonksiyonu giriniz (örn. x**3 - 6*x**2 + 11*x - 6): ")
f = lambda x: eval(func_str)

a = float(input("Aralık başlangıç değeri a: "))
b = float(input("Aralık bitiş değeri b: "))
tol = float(input("Toleransı giriniz (örn. 1e-6): "))
max_iter = int(input("Maksimum iterasyon sayısını giriniz: "))

# Kökü bulma
root = bisection(f, a, b, tol, max_iter)
if root is not None:
    print("Bulunan kök:", root)
else:
    print("Kök bulunamadı.")
