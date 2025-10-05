a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
natija = a > 0 and b > 0
print(natija)

c=int(input("yoshingizmi kiriting: "))
if 6>c :
    print("siz hali yosh bola ekansiz")
elif 18>c :
    print("siz balogat yoshiga yetmapsiz")
else 18<=c:
    print("siz avto maktabda oqiy olasiz")

h=input("1 ta son kiriting: ")
i=input("yana 1 ta son kiriting: ")
if h>i:
    print("Birinchi son katta")
elif h < i:
    print("Ikkinchi son katta")
else:
    print("Ikkalasi teng")

sa=int(input("bugun qanday baho oldingiz: "))
if sa=5 :
    print("yaxshi baho olibsiz")
elif sa=4 :
    print("normal baho olibsiz")
else sa=3,2 :
    print("siz yomon baho olibsiz")

w=int(input("Parolni kiriting: "))
p=int(input("Loginni kiriting: "))
if w=26049 and p=1388307:
    print("Xush kelibsiz!")
elif w<26049 and p>1388307:
    print("togri login parol kirgizing")
else:
    print("login parol togri kelmadi")