sayi1 = int(input("birinci sayi giriniz :"))
sayi2 = int(input("ikinci sayiyi giriniz :"))

#toplama
def toplama(sayi1 + sayi2):
    return sayi1+sayi2

#cıkarma
def cıkarma(sayi1 - sayi2):
    return sayi1-sayi2

#carpma
def carpma(sayi1 * sayi2):
    return sayi1*sayi2

#bolme
def bolme(sayi1 / sayi2):
    return sayi1/sayi2

print("Hangi işlemi yaptırmak istiyosunuz :")
print("1- Toplama")
print("2- Cıkarma")
print("3- Carpma")
print("4- Bolme")

secim =(input("Seçiminiz :"))

if toplama == "1":
    print(toplama)
if cıkarma == "2":
    print(cıkarma)
if carpma == "3":
    print(carpma)
if bolme == "4":
    print(bolme)
else:
    print("Geçersiz giriş")