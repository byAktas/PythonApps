import tkinter as hm
import math

cal = hm.Tk()
cal.title('HESAP MAKİNESİ')
cal.geometry("300x530+500+100")
cal.resizable(0,0)
cal.configure(background='BEIGE')

def topla():
    if sayi1.get() and sayi2.get():
        veri1=int(sayi1.get())
        veri2=int(sayi2.get())
        sonuc.configure(text=str(veri1+veri2))
def cıkar():
    if sayi1.get() and sayi2.get():
        veri1=int(sayi1.get())
        veri2=int(sayi2.get())
        sonuc.configure(text=str(veri1-veri2))
def çarpma():
    if sayi1.get() and sayi2.get():
        veri1=int(sayi1.get())
        veri2=int(sayi2.get())
        sonuc.configure(text=str(veri1*veri2))
def bölme():
    if sayi1.get() and sayi2.get():
        veri1=int(sayi1.get())
        veri2=int(sayi2.get())
        sonuc.configure(text=str(veri1/veri2))
def fak():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.factorial(veri1)))
def karekök():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.sqrt(veri1)))
def mutlak():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.fabs(veri1)))
def log():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.log10(veri1)))
def sin():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.sin(math.radians(veri1))))
def cos():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.cos(math.radians(veri1))))
def tan():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.tan(math.radians(veri1))))
def degres():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.degrees(veri1)))
def radyan():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(math.radians(veri1)))
def kare():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(veri1**2))
def küp():
    if sayi3.get():
        veri1=int(sayi3.get())
        sonuc.configure(text=str(veri1**3))
def yüzde():
    if  sayi2.get() and sayi3.get():
         veri1=int(sayi2.get())
         veri2=int(sayi3.get())
         sonuc.configure(text=str((veri1*veri2)/100))
def comb():
    if  sayi2.get() and sayi3.get():
         veri1=int(sayi2.get())
         veri2=int(sayi3.get())
         sonuc.configure(text=str(math.comb(veri1,veri2)))
def pow():
    if  sayi2.get() and sayi3.get():
         veri1=int(sayi2.get())
         veri2=int(sayi3.get())
         sonuc.configure(text=str(math.pow(veri1,veri2)))
def ebob():
    if  sayi2.get() and sayi3.get():
         veri1=int(sayi2.get())
         veri2=int(sayi3.get())
         sonuc.configure(text=str(math.gcd(veri1,veri2)))
def yuvarla():
    if  sayi3.get():
         veri1=float(sayi3.get())
         sonuc.configure(text=str(math.ceil(veri1)))

### VERİ GİRİŞLERİ


sonuc =hm.Label(cal, text="|----------|", width=30,background="BEIGE")
sonuc.place(x=110, y=70)
sayi1 = hm.Label(text="|1.|>").place(x=20,y=34)
sayi1 = hm.Entry(cal,  width=40)
sayi1.place(x=50, y=30,width=100,height=30)
sayi2 = hm.Label(text="|2.|>").place(x=20,y=74)
sayi2 = hm.Entry(cal,  width=40)
sayi2.place(x=50, y=70,width=100,height=30)
sayi3 = hm.Label(text="|3.|>").place(x=20,y=114)
sayi3 = hm.Entry(cal,  width=40,)
sayi3.place(x=50, y=110,width=100,height=30)
giris = hm.Label(text="Bilimsel hesaplar için\nyanlızca 3.girişi kullanın!",font="Times 8",bg="gray")
giris.place(x=155,y=110)
giris2= hm.Label(text="% , nr , üs, ve EBOB için 2.ve 3.girişi kullanın!",font="Times 10",bg="gray")
giris2.place(x=27,y=400)
### BUTONLAR

toplama    = hm.Button(cal, text='+'   , command=topla).place(x=22, y=150,width=60,height=60)
cıkarma    = hm.Button(cal, text='-'   , command=cıkar).place(x=87, y=150,width=60,height=60)
çarp       = hm.Button(cal, text='*'   , command=çarpma).place(x=153, y=150,width=60,height=60)
böl        = hm.Button(cal, text='/'   , command=bölme).place(x=219, y=150,width=60,height=60)
faktoriyel = hm.Button(cal, text="n!"  , command=fak).place(x=22,y=210,width=60,height=60)
karkök     = hm.Button(cal, text="√¯"  , command=karekök).place(x=87,y=210,width=60,height=60)
mutlakdeğer= hm.Button(cal, text="|n|" , command=mutlak).place(x=153,y=210,width=60,height=60)
logaritma  = hm.Button(cal, text="log" , command=log).place(x=219,y=210,width=60,height=60)
sinüs      = hm.Button(cal, text="sin" , command=sin).place(x=22,y=270,width=60,height=60)
kosinüs    = hm.Button(cal, text="cos" , command=cos).place(x=87,y=270,width=60,height=60)
tanjant    = hm.Button(cal, text="tan" , command=tan).place(x=153,y=270,width=60,height=60)
derecehesp = hm.Button(cal, text="°"   , command=degres).place(x=219,y=270,width=60,height=60)
radyanhesp = hm.Button(cal, text="rad" , command=radyan).place(x=22,y=330,width=60,height=60)
sayıkaresi = hm.Button(cal, text="n²"  , command=kare).place(x=87,y=330,width=60,height=60)
sayıküpü   = hm.Button(cal, text="n³"  , command=küp).place(x=153,y=330,width=60,height=60)
sayıyüzde  = hm.Button(cal, text="%"   , command=yüzde).place(x=219,y=426,width=60,height=60)
kombinasyon= hm.Button(cal, text="nr"  , command=comb).place(x=22,y=426,width=60,height=60)
özelüs     = hm.Button(cal, text="üs"  , command=pow).place(x=87,y=426,width=60,height=60)
ikisayıebob= hm.Button(cal, text="EBOB", command=ebob).place(x=153,y=426,width=60,height=60)
yuvarlama  = hm.Button(cal, text= "~"  , command=yuvarla).place(x=219,y=330,width=60,height=60)


cal.mainloop()