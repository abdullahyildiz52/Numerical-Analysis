# -- coding: latin-1 --

def pivot_bul(matris):
    p = len(matris[0])  # Sütun say?s?
    k = len(matris)     # Sat?r say?s?

    for i in range(min(p, k)):
        # Kö?egen eleman?n alt?nda kalan her bir eleman? kar??la?t?r?p maksimumunu bul
        max_deger = matris[i][i]
        max_satir = i
        for j in range(i+1, k):
            if abs(matris[j][i]) > abs(max_deger):
                max_deger = matris[j][i]
                max_satir = j

        # Maksimum de?erin oldu?u sat?r?, kö?egen eleman?n oldu?u sat?r ile yer de?i?tir
        if max_satir != i:
            matris[i], matris[max_satir] = matris[max_satir], matris[i]

    return matris

# Örnek bir 4x4 matris olu?tural?m
matris = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Pivot bulma i?lemi
sonuc = pivot_bul(matris)

# Sonucu yazd?rma
for row in sonuc:print(row)