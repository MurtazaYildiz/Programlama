print("İşletme karı tanımlama")

def ilkGelir(yg,fg,usg):
    global ilkDonemGelir
    ilkDonemGelir=yg+fg+usg
    print("İlk altı aydaki toplam geliriniz:",ilkDonemGelir)
    return ilkDonemGelir
def ilkGider(cm,kd,dm):
    global ilkDonemGider
    ilkDonemGider=cm+kg+dm
    print("İlk altı aydaki toplam gideriniz:",ilkDonemGider)
    return ilkDonemGider
def ilkKar(ilkDonemGelir,ilkDonemGider):
    global ilkDonemKar
    ilkDonemKar=ilkDonemGelir-ilkDonemGider
    print("İlk altı aydaki toplam karınız:",ilkDonemKar)
    return ilkDonemKar
def sonGelir(iyg,sgl,etg,iusg):
    global sonDonemGelir
    sonDonemGelir=iyg+sgl+etg+iusg
    print("Son altı aydaki toplam geliriniz:",sonDonemGelir)
    print()
    return sonDonemGelir
def sonGider(icm,ikd,bm):
    global sonDonemGider
    sonDonemGider=icm+ikd+bm
    print("Son altı aydaki toplam gideriniz:",sonDonemGider)
    return sonDonemGider
def sonKar(sonDonemGelir,sonDonemGider):
    global sonDonemKar
    sonDonemKar=sonDonemGelir-sonDonemGider
    print("Son altı aydaki toplam karınız:",sonDonemKar)
    return sonDonemKar
def isletmeKar(ilkDonemKar,sonDonemKar):
    yilSKar=ilkDonemKar-sonDonemKar
    if yilSKar>5000:
        print("İşletme çok karlı.",yilSKar)
    elif 1000<=yilSKar<=5000:
        print("işletme karı normal.",yilSKar)
    else:
        print("işletme yeterince karda değil.",yilSKar)
    return yilSKar

yg=int(input("İlk altı ayın yazılım geliri:"))
fg=int(input("İlk altı ayın finansman geliri:"))
usg=int(input("İlk altı ayın ürün satış geliri:"))
cm=int(input("İlk altı ayın çalışan maaşları:"))
kg=int(input("İlk altı ayın kira gideri:"))
dm=int(input("İlk altı ayın donanım maliyeti:"))
iyg=int(input("Son altı ayın yazılım geliri:"))
sgl=int(input("Son altı ayın sponsorluk gelir:"))
etg=int(input("Son altı ayın e-ticaret geliri:"))
iusg=int(input("Son altı ayın ürün satış geliri:"))
icm=int(input("Son altı ayın çalışan maaşları:"))
ikd=int(input("Son altı ayın kira gideri:"))
bm=int(input("Son altı ayın bakım maliyetleri:"))


birinciGelir=ilkGelir(yg,fg,usg)
birinciGider=ilkGider(cm,kg,dm)
birinciKar=ilkKar(ilkDonemGelir,ilkDonemGider)
ikinciGelir=sonGelir(iyg,sgl,etg,iusg)
ikinciGider=sonGider(icm,ikd,bm)
ikinciKar=sonKar(sonDonemGelir,sonDonemGider)
karZarar=isletmeKar(ilkDonemKar,sonDonemKar)
