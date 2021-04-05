# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
# Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

sayi=int(input("Sayi giriniz: "))
mukemmelmi=1
bolenler=[]

for i in range(1,sayi):
    if sayi%i==0:
        bolenler.append(i)

for i in bolenler:
    mukemmelmi*=i

if sayi==mukemmelmi:
    print("Sayi mukemmeldir.")
else:
    print("sayi mukemmel degildir.")


# Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
# Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin
# toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

sayi=input("Sayi giriniz.")

basamak= len(str(sayi))

armstrongmu=0

for i in range(basamak):
    armstrongmu+=int(sayi[i])**basamak

if(int(sayi) == armstrongmu):
    print("Bu Bir Armstrong Sayısıdır.")
else:
    print("Armstong Sayısı Degildir.")


# 1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
# İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
i=1
j=1
for i in range(1,11):
    for j in range(1,11):
        print("{}*{}={}".format(i,j,i*j))


# Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir
# değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
# İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

toplam=0
while True:
    sayi=input("Sayi Giriniz: \nCikmak icin 'q' tusuna basin.")
    if sayi=="q":
        break
    toplam+=int(sayi)

print(toplam)

# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

for i in range(1,100):
    if i%3!=0:
        continue
    else:
        print(i)


# Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik.
# Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan
# sadece çift sayıları bir listeye atmayı yapmayı çalışın.
# Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur.
# Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.
# İpucu: Basit düşünmeye çalışın.

ciftsayilar=[]
for i in range(1,100):
    if i%2==0:
        ciftsayilar.append(i)

print(ciftsayilar)


