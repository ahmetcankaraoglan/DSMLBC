def hesapla():
    dersler = ["Matematik","Fizik","Biyoloji","Tarih","Felsefe"]
    vize_notlar = [100,85,75,50,15]
    liste_copy = dersler.copy() #Liste 1.Method
    for i in range(0,len(dersler)):
        k = liste_copy[i]
        b = k.upper() #String 1.Method
        c = k.replace("a","e") #String 2.Method
        liste_copy.append(vize_notlar[i]) #Liste 2.Method
        #print(liste_copy)
        #print(c)
        
    toplam=0
    ortalama=0
    for i in vize_notlar:
        toplam+=i*40/100
    return toplam



ortalama = (hesapla()/5)
print("Vize sınavı sınıf ortalaması:"  + str(ortalama)) 
