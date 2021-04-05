#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

sayi1 = int(input("1.sayiyi giriniz: "))
sayi2 = int(input("2.sayiyi giriniz: "))
sayi3 = int(input("3.sayiyi giriniz: "))

sayilar = [sayi1, sayi2, sayi3]
carpim = sayi1 * sayi2 * sayi3
print("Sayilarin carpimi: ", carpim)

#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m)*Boy(m)

boy=float(input("Boyunuzu giriniz(or:1.72) : "))
kilo=int(input("Kilonuzu giriniz: "))

bki=kilo/(boy*boy)

print("Beden Kitle Endeksiniz: ",bki)

#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar
#ödemesini gerektiğini hesaplayın.

kmbasiyakit=float(input("Araciniz km basi kac tl yakiyor? : "))
gidilenyol=float(input("Kac km yol gittiniz? : "))

odenecekmiktar=kmbasiyakit*gidilenyol

print("Odemeniz gereken miktar: ",odenecekmiktar)

#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad=input("Adiniz:")
soyad=input("Soyadiniz:")
numara=input("Numaraniz:")
bilgiler=[ad,soyad,numara]

for i in bilgiler:
    print(i)


#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

sayi1=int(input("1.sayiyi giriniz:"))
sayi2=int(input("2.sayiyi giriniz:"))

print("Sayi1 : {}\nSayi2 : {}\nSayilar degistiriliyor...".format(sayi1,sayi2))

sayi1=sayi1+sayi2
sayi2=sayi1-sayi2
sayi1=sayi1-sayi2

print("Sayi1 : {}\nSayi2 : {}\nSayilar degistirildi.".format(sayi1,sayi2))

#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2
import math

kenar1=float(input("Dik ucgenin birinci dik kenarini giriniz: "))
kenar2=float(input("Dik ucgenin ikinci dik kenarini giriniz: "))

hipotenusunkaresi=(kenar1*kenar1)+(kenar2*kenar2)
hipotenus=math.sqrt(hipotenusunkaresi)

print("Kenar1:{}\nKenar2:{}\nHipotenus:{}".format(kenar1,kenar2,hipotenus))

