print("Müşteri çalışma süreleri hesaplaması ve karşılaştırılması")
def ilkYil(cs,tms):
    global birinciYil
    birinciYil=cs/tms
    print("Birinci yıla ait müşteri çalışma süresi:",birinciYil)
    return birinciYil
def ikinciYill(ics,itms):
    global ikinciYil
    ikinciYil=ics/itms
    print("İkinci yıla ait müşteri çalışma süresi:",ikinciYil)
    return ikinciYil
def karsilastir(birinciYil,ikinciYil):
    sonuc=birinciYil-ikinciYil
    if sonuc>0:
        print("Müşterilerle çalışma süresi karşılaştırdığınız yıla göre artmıştır:",sonuc)
    elif sonuc==0:
        print("Müşterilerle çalışma süresinde herhangi bir değişiklik olmamıştır:",sonuc)
    else:
        print("Müşterilerle çalışma süresi karşılaştırdığınız yıla göre azalmıştır:",sonuc)
    return sonuc
birinciYil=int(input("Bir yıl giriniz:"))
cs=int(input("Yıla ait çaışılan süre:"))
tms=int(input("Yıla ait toplam müşteri sayısı:"))
ikinciYil=int(input("Karşılaştırmak istediğiniz yılı giriniz:"))
ics=int(input("Yıla ait çalışılan süre:"))
itms=int(input("Yıla ait toplam müşteri sayısı:"))

a=ilkYil(cs,tms)
b=ikinciYill(ics,itms)
c=karsilastir(birinciYil,ikinciYil)
