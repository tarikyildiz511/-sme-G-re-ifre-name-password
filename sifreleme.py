import random

si1 = random.randint(1,9)
si2 = random.randint(1,9)
si3 = random.randint(1,9)
si4  = random.randint(1,9) 
si5 = random.randint(1,9)

si6 = (si1,si2,si3,si4,si5)


isminiz =input("isim giriniz")

if len(isminiz)>2 and  len(isminiz) <5:
    print("isme özel şifreniz",si1,si2,si3)
elif len(isminiz)>4 and len(isminiz)<10:
    print("isme özel şifreniz",si6)
