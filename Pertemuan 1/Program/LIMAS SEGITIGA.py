# Mengambil input untuk panjang alas dan tinggi segitiga
panjang_alas = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Menghitung luas permukaan
luas_permukaan = (panjang_alas * tinggi_segitiga) + (3 * (1 / 2) * panjang_alas * tinggi_limas)

# Menghitung volume
volume = (1 / 3) * (1 / 2) * panjang_alas * tinggi_segitiga * tinggi_limas

# Mencetak luas permukaan dan volume limas segitiga
print(f"Luas permukaan limas segitiga : {luas_permukaan}")
print(f"Volume limas segitiga : {volume}")