# Mengambil input untuk panjang, lebar, tinggi, dan tinggi limas segiempat
panjang = float(input("Masukkan panjang alas limas segiempat: "))
lebar = float(input("Masukkan lebar alas limas segiempat: "))
tinggi_limas = float(input("Masukkan tinggi limas segiempat: "))
tinggi = float(input("Masukkan tinggi segitiga alas limas: "))

# Menghitung luas permukaan
luas_permukaan = panjang * lebar + 2 * (panjang * tinggi_limas / 2) + 2 * (lebar * tinggi_limas / 2)

# Menghitung volume
volume = (1/3) * panjang * lebar * tinggi

# Mencetak luas permukaan dan volume
print(f"Luas permukaan limas segiempat : {luas_permukaan}")
print(f"Volume limas segiempat : {volume}")
