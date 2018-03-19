print("Dönembaşı ve dönemsonu stok ortalaması hesaplama")

def donemBasiStokHesapla(ks=250,ys=250,ds=250):
    global donemBasiStok
    donemBasiStok=ks+ys+ds
    print("Dönem başı stok miktarı",donemBasiStok)
    return donemBasiStok
def girilenStokHesapla(donemBasiStok,kss,yss,dss):
    global girilenStok
    girilenStok=donemBasiStok+kss+yss+dss
    print("Dönem içi stok miktarı",girilenStok)
    return girilenStok
def donemSonuStokHesapla(girilenStok,ksy,ysy,dsy):
    global donemSonuStok
    donemSonuStok=girilenStok-(ksy+ysy+dsy)
    print("Dönem sonu toplam stok miktarı:",donemSonuStok)
    return donemSonuStok
    
def ortalamaStokHesapla(donemBasiStok,donemSonuStok):
    ortalamaStok=(donemBasiStok+donemSonuStok)/2
    print("Ortalama stok miktarı:",ortalamaStok)
    return ortalamaStok

kss=int(input("Stoğa eklenecek koltuk miktarı:"))
yss=int(input("Stoğa eklenecek yatak miktarı:"))
dss=int(input("Stoğa eklenecek dolap miktarı:"))
ksy=int(input("Stoktan düşülecek koltuk miktarı:"))
ysy=int(input("Stoktan düşülecek yatak miktarı:"))
dsy=int(input("Stoktan düşülecek dolap miktarı:"))

ilkStok=donemBasiStokHesapla(ks=250,ys=250,ds=250)
girilenStok=girilenStokHesapla(donemBasiStok,kss,yss,dss)
sonStok=donemSonuStokHesapla(girilenStok,ksy,ysy,dsy)
ortalamaStok=ortalamaStokHesapla(donemBasiStok,donemSonuStok)
