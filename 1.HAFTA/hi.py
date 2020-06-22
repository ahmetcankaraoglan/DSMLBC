
def toplama_ıslemi():
     a = int(input("Lütfen birinci sayıyı giriniz"))
     b = int(input("Lütfen ikinci sayıyı giriniz"))
     print("Toplama İşlemi Sonucunuz:" + str(a+b))


def cıkarma_ıslemi():
     a = int(input("Lütfen birinci sayıyı giriniz"))
     b = int(input("Lütfen ikinci sayıyı giriniz"))
     print("Çıkarma İşlemi Sonucunuz:" + str(a-b))



def carpma_ıslemi():
     a = int(input("Lütfen birinci sayıyı giriniz"))
     b = int(input("Lütfen ikinci sayıyı giriniz"))
     print("Çarpma İşlemi Sonucunuz:" + str(a*b))



def bolme_ıslemi():
     a = int(input("Lütfen birinci sayıyı giriniz"))
     b = int(input("Lütfen ikinci sayıyı giriniz"))
     print("Bölme İşlemi Sonucunuz:" + str(a/b))


print("Lütfen yapmak istedğiniz işlemi giriniz: Toplama işlemi için 1, Çıkarma işlemi için 2, Çarpma işlemi için 3, Bölme işlemi için 4'ü seçiniz")
d = int(input())


if d == 1:
    toplama_ıslemi()
elif d == 2:
    cıkarma_ıslemi()
elif d == 3:
    carpma_ıslemi()
else:
    bolme_ıslemi()










    