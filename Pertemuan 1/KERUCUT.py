import math

# Masukkan jari-jari dan tinggi kerucut
jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))

# Menghitung luas permukaan kerucut
luas = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))

# Menghitung volume kerucut
volume = (1/3) * math.pi * jari_jari**2 * tinggi

# Cetak luas dan volume kerucut
print(f"Luas kerucut adalah: {luas:.2f} satuan luas")
print(f"Volume kerucut adalah: {volume:.2f} satuan volume")