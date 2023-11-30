from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmLimasSegiempat:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Panjang:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Lebar:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Limas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtPanjang = Entry(mainFrame) 
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)  
        self.txtLebar = Entry(mainFrame) 
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5)
        self.txtTinggiLimas = Entry(mainFrame) 
        self.txtTinggiLimas.grid(row=3, column=1, padx=5, pady=5) 
        self.txtLuasPermukaan = Entry(mainFrame) 
        self.txtLuasPermukaan.grid(row=5, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=6, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=4, column=1, padx=5, pady=5)


    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        panjang = int(self.txtPanjang.get())
        lebar = int(self.txtLebar.get())
        tinggi = int(self.txtTinggi.get())
        tinggi_limas = int(self.txtTinggiLimas.get())
        luas_permukaan = panjang * lebar + 2 * (panjang * tinggi_limas / 2) + 2 * (lebar * tinggi_limas / 2)
        volume = (1/3) * panjang * lebar * tinggi
        self.txtLuasPermukaan.delete(0,END)
        self.txtLuasPermukaan.insert(END,str(luas_permukaan))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(volume))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasSegiempat(root, "Program Luas Permukaan Dan Volume Limas Segiempat")
    root.mainloop()