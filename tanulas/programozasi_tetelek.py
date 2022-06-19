
'''
Írj programot, amely bekéri a jegyeidet, kiírja őket egy sorban, vesszővel elválasztva, majd kiírja az átlagodat!
'''
# 3 2 4 5 1 
mark = input('jegyeid? ')
listmark = mark.split()
print(','.join(listmark))
listmark_int = list(map(int, listmark))
print(sum(listmark_int)/len(listmark_int))

'''
Egy árucikk 5 éve X (felhasználótól megkérdezett) forintba került a boltban.
Az elmúlt években többnyire emelkedett az ára, de volt, amikor csökkent.
A változások százalékos értéke az egyes években: +12%, +3%, -4%, +8%, +9%. Mennyibe kerül az árucikk idén?
A százalékokat tárold listában, százalékjel nélkül!
'''
price_change = [0,12, 0.03, -0.04, 0.08, 0.09]
base_price = int(input('What was the price? '))

for change in price_change:
  base_price = base_price * (1+change)

print(base_price)

'''
Adott a hét napjainak listája. Döntsd el, hogy a felhasználó rendes napnevet adott-e meg!
'''
alldays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturnday', 'Sunday']

day = False

days = input('day? ')

for dayz in alldays:
  if days in alldays:
    print(not day)
    break
  else:
    print(day)

'''
Adott egy lista: [1, 54, 35, 67, 12]. Melyik az első páros szám?
Hányadik az első héttel osztható szám?
Melyik az első 60 és 70 közé eső szám? Hányadik szám a 12? Mi a 12 indexe?
'''
number_list = [1, 54, 35, 67, 12]

for number in number_list:
  if number % 2 == 0:
    print(number)
    break

number_list = [1, 54, 35, 67, 12]

position = 0

for number in number_list:
  position += 1
  if number % 7 == 0:
    print(position)
    print(number)

number_list = [1, 54, 35, 67, 12]

for number in number_list:
  if number > 60 and number < 70:
    print(number)
    break

number_list = [1, 54, 35, 67, 12]

position = 0

for number in number_list:
  position += 1
  index = number_list.index(12)
  if number == 12:
    print(position)
    print(index)
    break

'''
Adott az 5, 4, 3, 4, 5, 4, 4, 5, 3, 1 sorozat. Van-e benne egymás mellett két azonos szám? Ha igen, hol?
'''
number_list = [5, 4, 3, 4, 5, 4, 4, 5, 3, 1]

for number in range(len(number_list)):
 
  if number == len(number_list) - 1:
    break
  #print('elso ' + str(number_list[number]))
  #print('masodik ' + str(number_list[number + 1]))

  print((number_list[number]) == (number_list[number + 1]))

#MASOLAS

'''
Adott egy lista az elmúlt hónap napi átlaghőmérsékleteivel. Meleg nap az, ahol 20℃ feletti a hőmérséklet.
Írj másik listát, amelyben a “rendes” hőmérsékletek esetén az eredeti adat, “meleg” napok esetén egy felkiáltójel szerepel!
Az eredeti listát véletlenszerű, 15 és 25 közötti számokkal feltöltve hozd létre.
'''
import random

def hot_day(temperature):
    if temperature > 20:
      return('!')
    else:
      return(temperature)

random_temperature_list = [random.randrange(15, 25) for temperature in range(30)]

new_temperature_list = []

for temperature in random_temperature_list:
    new_temperature_list.append(hot_day(temperature))


print(random_temperature_list)
print(new_temperature_list)

'''
Adott az előző, hőmérsékleteket tartalmazó lista.
Hozz létre egy listát, amely a hónap első napjánál egy 0-t, egyébként pedig +, -, 
illetve = jelet tartalmaz, aszerint, hogy az adott nap hőmérséklete az előzőnél nagyobb, kisebb, vagy azzal megegyező!
'''
import random

random_temperature_list = [random.randrange(15, 25) for temperature in range(30)]
print(random_temperature_list)

new_temperature_list = []

def day_difference(temperature_index):
    if (temperature_index == 0): 
      return "0"
    elif random_temperature_list[temperature_index - 1] < random_temperature_list[temperature_index]:
      return "+"
    elif random_temperature_list[temperature_index - 1] > random_temperature_list[temperature_index]:
      return "-"
    elif random_temperature_list[temperature_index - 1] == random_temperature_list[temperature_index]:
      return "="

for temperature_index in range(len(random_temperature_list)):
    new_temperature_list.append(day_difference(temperature_index))

print(new_temperature_list)
