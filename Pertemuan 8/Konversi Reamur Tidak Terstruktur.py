print("Konversi Suhu Reamur")

# Entry
suhu = input("Masukan Suhu Dalam Reamur")

# rumus
C = 5/4 * float(suhu)
F = (9/4 * float(suhu)) + 32
K = 5/4 * float(suhu) + 273

# output
print(suhu + "Reamur Sama Dengan")
print(str(C) + " Celcius ")
print(str(F) + " Fahrenheit ")
print(str(K) + " Kelvin ")