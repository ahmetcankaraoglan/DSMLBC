def toplama_ıslemi():
     a = int(input("Lütfen birinci sayıyı giriniz:"))
     b = int(input("Lütfen ikinci sayıyı giriniz:"))
     print("Toplama İşlemi Sonucunuz:" + str(a+b))


def cıkarma_ıslemi():
     a = int(input("Lütfen birinci sayıyı giriniz:"))
     b = int(input("Lütfen ikinci sayıyı giriniz:"))
     print("Çıkarma İşlemi Sonucunuz:" + str(a-b))



def carpma_ıslemi():
     a = int(input("Lütfen birinci sayıyı giriniz:"))
     b = int(input("Lütfen ikinci sayıyı giriniz:"))
     print("Çarpma İşlemi Sonucunuz:" + str(a*b))



def bolme_ıslemi():   # Bölme işlemi yapan fonksiyon
    try:
     a = int(input("Lütfen birinci sayıyı giriniz:"))
     b = int(input("Lütfen ikinci sayıyı giriniz:"))
     print("Bölme İşlemi Sonucunuz:" + str(a/b))
    except:
        print("Sayı Sıfıra Bölünemez")


print("Lütfen yapmak istedğiniz işlemi giriniz:") 
print("Toplama işlemi için 1;")
print("Çıkarma işlemi için 2;")
print("Çarpma işlemi için 3;")
print("Bölme işlemi için 4'ü seçiniz.")

d = int(input())


if d == 1:
    toplama_ıslemi()
elif d == 2:
    cıkarma_ıslemi()
elif d == 3:
    carpma_ıslemi()
elif d == 4:
    bolme_ıslemi()
else:
    print("Hatalı seçim yaptınız, lütfen tekrar deneyiniz.")