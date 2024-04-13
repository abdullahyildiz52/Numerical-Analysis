import tkinter as tk
from tkinter import messagebox


def pivot_bul(matris):
    p = len(matris[0])  # Sütun sayısı
    k = len(matris)  # Satır sayısı

    for i in range(min(p, k)):
        # Köşegen elemanın altında kalan her bir elemanı karşılaştırıp maksimumunu bul
        max_deger = matris[i][i]
        max_satir = i
        for j in range(i + 1, k):
            if abs(matris[j][i]) > abs(max_deger):
                max_deger = matris[j][i]
                max_satir = j

        # Maksimum değerin olduğu satırı, köşegen elemanın olduğu satır ile yer değiştir
        if max_satir != i:
            matris[i], matris[max_satir] = matris[max_satir], matris[i]

    return matris
matris = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Pivot bulma işlemi
sonuc = pivot_bul(matris)

# Sonucu yazdırma
for row in sonuc:print(row)

def get_matrix():
    rows = int(row_entry.get())
    cols = int(col_entry.get())

    matris = []
    for i in range(rows):
        row = []
        for j in range(cols):
            try:
                value = int(entry_list[i][j].get())
                row.append(value)
            except ValueError:
                messagebox.showerror("Hata", "Geçersiz değer: {}".format(entry_list[i][j].get()))
                return
        matris.append(row)

    sonuc = pivot_bul(matris)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    for row in sonuc:
        result_text.insert(tk.END, " ".join(map(str, row)) + "\n")
    result_text.config(state=tk.DISABLED)


# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Pivot Bulma")

# Matris boyutunu girmek için giriş alanları oluşturma
row_label = tk.Label(root, text="Satır Sayısı:")
row_label.grid(row=0, column=0)
row_entry = tk.Entry(root)
row_entry.grid(row=0, column=1)

col_label = tk.Label(root, text="Sütun Sayısı:")
col_label.grid(row=1, column=0)
col_entry = tk.Entry(root)
col_entry.grid(row=1, column=1)

# Matris elemanlarını girmek için giriş alanları oluşturma
entry_list = []
for i in range(4):
    row = []
    for j in range(4):
        entry = tk.Entry(root, width=7)
        entry.grid(row=i +2, column=j)
        row.append(entry)
    entry_list.append(row)
# Pivot bulma butonu oluşturma
button = tk.Button(root, text="Pivot Bul", command=get_matrix)
button.grid(row=6, columnspan=4)

# Sonuçları göstermek için metin alanı oluşturma
result_text = tk.Text(root, height=4, width=20, state=tk.DISABLED)
result_text.grid(row=7, columnspan=4)

# Tkinter penceresini gösterme
root.mainloop()