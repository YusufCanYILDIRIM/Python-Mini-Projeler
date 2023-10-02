#toplama
def toplama(sayi1, sayi2):
    return sayi1 + sayi2

#cıkarma
def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

#carpma
def carpma(sayi1, sayi2):
    return sayi1 * sayi2

#bolme
def bolme(sayi1, sayi2):
    if sayi2 == 0:
        return "Bir sayıyı sıfıra bölemezsiniz."
    return sayi1 / sayi2

print("Hangi işlemi yaptırmak istiyosunuz :")
print("1- Toplama")
print("2- Cıkarma")
print("3- Carpma")
print("4- Bolme")

secim =(input("Seçiminiz :"))

sayi1 = int(input("birinci sayi giriniz :"))
sayi2 = int(input("ikinci sayiyi giriniz :"))

if secim == "1":
    print(sayi1,"+",sayi2,"=",toplama(sayi1,sayi2))
elif secim == "2":
    print(sayi1,"-",sayi2,"=",cikarma(sayi1,sayi2))
elif secim == "3":
    print(sayi1,"*",sayi2,"=",carpma(sayi1,sayi2))
elif secim == "4":
    print(sayi1,"/",sayi2,"=",bolme(sayi1,sayi2))
else:
    print("Geçersiz giriş")