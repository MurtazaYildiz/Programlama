 1.
def gelirHesaplama(x,y,z):
    gelir=x+y+z
    return gelir
x=int(input("Finansman Gelirini Giriniz:"))
y=int(input("Pazar Gelirini Giriniz:"))
z=int(input("Kira Gelirini Giriniz:"))
k=gelirHesaplama(x,y,z)
print("Gelirlerinizin Toplamı:",k)
def giderHesaplama(q,w,e,r,t):
    gider=(q+w+e+r+t)
    return gider
q=int(input("Ücret Giriniz:"))
w=int(input("Finansman Giderini Girniz:"))
e=int(input("Pazar Giderini Giriniz:"))
r=int(input("Kira Giderini Giriniz:"))
t=int(input("Muhasebe Giderini Giriniz:"))
m=giderHesaplama(q,w,e,r,t)
print("Giderlerinizin Toplamı:",m)
def karHesaplama(k,m):
    kar=k-m
    return kar
o=karHesaplama(k,m)
print("Karınız:",o)
if (k-m)>1000:
    print("Şirketiniz karlıdır")
elif (k-m)==1000:
    print("Şirketiniz başabaş noktasındadır.")
else:
    print("Şirketinizin kar oranı düşüktür.")

    
    
    
 2.
 
 
    
    
    
    
    
