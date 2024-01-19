class food:
    def __init__(self,name,fats,proteins,carbohydrates,calories):
        self.name = name
        self.fats = fats
        self.proteins = proteins
        self.carbohydrates = carbohydrates
        self.calories = calories
    def __str__(self):
        return(f'Название: {self.name}\n'
               f'Жиры: {self.fats} г.\n'
               f'Белки: {self.proteins} г.\n'
               f'Углеводы: {self.carbohydrates} г.\n'
               f'Калорийность: {self.calories} г.')
f = open('C:\\Users\\student\\Desktop\\food.csv')
s = f.readlines()
f.close()
s = s[1:]
for i in range(len(s)):
    s[i] = s[i].replace(',','.')
s = [x.split(';') for x in s]
Product = []
for x in s:
    Product.append(food(x[0],float(x[1]),float(x[2]),float(x[3]),float(x[4])))
print('---------------------Номер 2------------------------')
Product.sort(key= lambda x: x.calories)
Product = Product[::-1]
sk = 0
for x in Product:
    sk+=1
    print(x)
    print('----------------')
    if sk == 5:
        break
print('---------------------Номер 3------------------------')
k = 0
cal = []
for x in Product:
    if x.carbohydrates!=0:
        if x.fats/x.carbohydrates > 60:
            k+=1
            cal.append(x)
cal.sort(key= lambda x: x.calories)
sk = 0
for x in cal:
    sk+=1
    print(x)
    print('----------------')
    if sk == 10:
        break
print(k)
print('---------------------Номер 4------------------------')
k = 0
for x in Product:
    if x.carbohydrates == 0 and x.fats == 0 and x.proteins == 0:
        k+=1
        print(x)
        print('----------------')
print(k)
print('---------------------Номер 5------------------------')
d = dict()
for x in Product:
    d[x.name] = ('Жиры: ' + str(x.fats) , 'Белки: ' + str(x.proteins))
print(d)
N = input('Введите продукт: ')
print(d[N])