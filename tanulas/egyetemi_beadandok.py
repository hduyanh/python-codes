'''
5 hatványok

    Írjon kódot, ami eldönti, hogy egy szám öthatvány-e!
    Foglalja függvénybe!
    Írjon függvényt, ami megadja az öthatványok listáját n-ig!
'''
n2 = 125
n3 = 126
n4 = 0

# 1
r = False
maradek = n3
while (maradek % 5 == 0):
  maradek = maradek / 5
if maradek == 1:
  r = True

# 2
def othatvany(m):
  r = False
  maradek = m
  while (maradek % 5 == 0):
    maradek = maradek / 5
  if maradek == 1:
    r = True
  return r

# 3
def othatvany_lista(n):

  def othatvany(m):
    r = False
    maradek = m
    while (maradek % 5 == 0):
      maradek = maradek / 5
    if maradek == 1:
      r = True
    return r

  l1 = [i for i in range(1, n + 1) if othatvany(i)]
  return l1

'''
2-gizda számok

A számjegyek kétszeresét fölemeljük a kétszeresére annak a számnak, ahányadik helyen áll a számjegy az eredeti számban. Ha ezeknek a hatványoknak az összege egyenlő az eredeti számmal, a számot 2-gizda számnak nevezzük.

    Írjon kódot, ami eldönti, hogy egy szám 2-gizda szám-e!
    Foglalja függvénybe!
    Írjon függvényt, ami megadja az 2-gizda számok listáját n-ig!
'''
#n az eredeti szám, m a kereset számjegy a számban
def gizda_e(n, m):
  s1 = str(n)
  s2 = str(m)
# ahányadik helyen áll a számjegy az eredeti számban
  hely = 0
  for i in s1:
    hely += 1
    if i == s2:
      break
# számjegyek kétszeresét fölemeljük a kétszeresére annak a számnak
  l1 = []
  for j in s1:
    l1.append((2*int(j)) * (2* hely))
# ezeknek a hatványoknak az összege
  osszeg = 0
  for x in l1:
    osszeg += x
# egyenlő az eredeti számmal
  return osszeg == n

def gizda_e_listaja(n, m):
    gizda_lista = []
    for i in range(n):
        if (gizda_e(i, m)):
            gizda_lista.append(i)
    return gizda_lista
    
gizda_e_listaja(10000, 2)


'''
Függeszkedő számok¶

Egy szám függeszkedő szám, ha legalább háromjegyű, az első és utolsó számjegye egyenlő, a közbülsők pedig kisebbek ezeknél.

    Írjon kódot, ami eldönti, hogy egy szám függeszkedő szám-e!
    Foglalja függvénybe!
    Írjon függvényt, ami megadja a függeszkedő számok listáját n-ig!
'''
n1, n2 = 95439, 37835463
l1 = list(str(n1))
l2 = [int(i) for i in l1]

def fuggeszkedo(n):
  r = False
  l1 = list(str(n))
  l2 = [int(i) for i in l1]
  if len(l2) >= 3 and l2[0] == l2[-1] and l2[0] > max(l2[1:-1]):
    r = True
  return r

def fuggeszkedolista(m):

  def fuggeszkedo(n):
    r = False
    l1 = list(str(n))
    l2 = [int(i) for i in l1]
    if len(l2) >= 3 and l2[0] == l2[-1] and l2[0] > max(l2[1:-1]):
      r = True
    return r

  l3 = [i for i in range(m + 1) if fuggeszkedo(i)]
  return l3

fuggeszkedolista(10000)

'''
Emelkedő számok

Olyan számok, amelyek legalább kétjegyűek és minden számjegyük nagyobb, mint a megelőző számjegy.

    Írjon kódot, ami eldönti, hogy egy szám emelkedő szám-e!
    Foglalja függvénybe!
    Írjon függvényt, ami megadja a emelkedő számok listáját n-ig!
'''
n1 = 654321
n2 = 123456
l1 = [int(i) for i in list(str(n1))]

r = True
for i in range(len(l1) - 1):
  if l1[i] >= l1[i+1]:
    r = False

def emelkedo(n):
  r = True
  l1 = [int(i) for i in list(str(n))]
  if len(l1) < 2:
    r = False
  else:
    for i in range(len(l1) - 1):
      if l1[i] >= l1[i+1]:
        r = False
        break
  return r

def emelkedo2(n):
  l1 = [int(i) for i in list(str(n))]
  return (len(l1) >= 2) and all((l1[i] < l1[i+1]) for i in range(len(l1) - 1))

def emelkedolista(n):

  def emelkedo(n):
    r = True
    l1 = [int(i) for i in list(str(n))]
    if len(l1) < 2:
      r = False
    else:
      for i in range(len(l1) - 1):
        if l1[i] >= l1[i+1]:
          r = False
          break
    return r

  l2 = [i for i in range(n + 1) if emelkedo(i)]
  return l2 

emelkedolista(1000)


'''
Teszt adatbázis

Készítsen egy szótárat! A kulcsok legyenek egy cég 30 üzleti partnerének nevei, az egyszerűség kedvéért ebben a formában: Cég_1, Cég_2, ...stb. 
Minden üzleti partnerhez tartozzon egy 15 számot tartalmazó lista, az egyszerűség kedvééért minden szám legyen 200 és 500 közötti véletlenszám.
'''
import random as rnd
l1 = ["Ceg_"+str(i) for i in range(30)]
l2 = [rnd.randint(200, 500) for i in range(15)]
l3 = [[rnd.randint(200, 500) for i in range(15)] for j in range(30)]
d1 = dict(zip(l1, l3))
print(d1)
