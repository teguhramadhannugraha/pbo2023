print("Konversi Suhu Celcius")

# Entry
suhu = input("Masukkan Suhu Dalam Celcius:")

# rumus
F = (9/5 * float (suhu)) + 32
R = (4/5 * float(suhu))
K = float(suhu) + 273

#output
print(suhu + " Celcius sama dengan ")
print(str (F)+ " Fahrenheit ")
print(str (R) + " Reamur ")
print (str(K) + " Kelvin ")