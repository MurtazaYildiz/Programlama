print("Katma Değer Ciro Hesaplama")
def katmaDegerCiro(tsm,hmm,bkog,svg,sah):
    global kdc
    kdc=tsm-(hm+bog+sg+sahg)
    if kdc>1000:
        print("işletme katma değer cirosu yüksek.",kdc)
    elif 500<kdc<999:
        print("işletme katma değer cirosu normal.",kdc)
    elif kdc<500:
        print("katma değer cirosu düşük.",kdc)
    return kdc
tsm=int(input("Toplam satış miktarı giriniz:"))
hm=int(input("Hammadde maliyeti giriniz:"))
bog=int(input("Bakım onarım giderlerinizi giriniz:"))
sg=int(input("Sevkiyat giderlerini giriniz:"))
sahg=int(input("Satın alınan hizmet giderleriniz:"))

katmaDegerCiro=katmaDegerCiro(tsm,hm,bog,sg,sahg)

