# bankamatik  uygulaması

YusufHesap = {
    'ad' : 'Yusuf Can',
    'hesapNo' : 12345678,
    'bakiye' : 3000,
    'ekHesap' : 2000
}

# para cekme 
def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("paranızı alabilirsiniz")
        print(f"{hesap['hesapNo']} nolu hesabınızın bakiyesi {hesap['bakiye']} 'dir.")

    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if(toplam >= miktar):
            ekHesapKullanımı=input("ekhesabınızdan para kullannılsın mı (e/h) :")
           
            if ekHesapKullanımı == 'e':
               ekHesapKullanılıcakMikar = miktar - hesap['bakiye']
               bakiye= hesap['bakiye'] = 0
               hesap['ekHesap'] -=  ekHesapKullanılıcakMikar 
               print("paranızı alabilirsiniz.")
               bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızın {hesap['bakiye']} bulunmaktadır")
        else:
            print("üzgünüz bakiye yetersiz")
            bakiyeSorgula(hesap)

# para yatırma
def paraYatir(hesap):
    yatirilacakMikar = int(input("ne kadar yatırmak istiyorsunuz :"))
    hesap['bakiye'] += yatirilacakMikar
    bakiyeSorgula(hesap)


# bakiye sorgulama
def bakiyeSorgula(hesap):
     print(f"{hesap['hesapNo']} nolu hesabınızın {hesap['bakiye']} bulunmaktadır. Ek hesap liminiz {hesap['ekHesap']} bulunmaktadır")

               
paraCek(YusufHesap, 6000)
paraYatir(YusufHesap)