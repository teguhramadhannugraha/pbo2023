from gtts import gTTS
import os

# Teks yang ingin diubah menjadi suara
teks = "PERKENALKAN NAMA SAYA TEGUH RAMADHAN NUGRAHA"

# Inisialisasi objek gTTS dengan teks dan bahasa yang diinginkan (dalam contoh ini, bahasa Indonesia)
tts = gTTS(text=teks, lang='id')

# Simpan suara ke dalam file 'output.mp3'
tts.save("output.mp3")

# Putar suara menggunakan aplikasi default di sistem
os.system("output.mp3")