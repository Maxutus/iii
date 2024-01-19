class country:
    def __init__(self,name,capital,population,area):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
    def __str__(self):
        return(f'Страна: {self.name:<25} Столица: {self.capital:<25} Население: {self.population:<20} Площадь: {self.area:<20}')
f = open('C:\\Users\\student\\Desktop\\данные.txt')
s = f.readlines()
f.close()

for i in range(len(s)):
    s[i] = s[i].replace('t','')
    s[i] = s[i].replace('n', '')
s = [x.split('\t') for x in s]

Countries = []
for x in s:
    Countries.append(country(x[0],x[1],int(x[2]),int(x[3])))


f = open('страны.txt','w',encoding='UTF-8')
for x in Countries:
    f.write(f'Страна: {x.name:<25} Столица: {x.capital:<25} Население: {x.population:<20} Площадь: {x.area:<20}\n')
f.close()

f = open('Население.txt','w',encoding='UTF-8')
Countries.sort(key= lambda x: -x.population)
for x in Countries:
    f.write(f'Население: {x.population:<20} Страна: {x.name:<25} Столица: {x.capital:<25} Площадь: {x.area:<20}\n')
f.close()

f = open('Площадь.txt','w',encoding='UTF-8')
Countries.sort(key= lambda x: x.area)
for x in Countries:
    f.write(f'Площадь: {x.area:<20} Страна: {x.name:<25} Столица: {x.capital:<25} Население: {x.population:<20}\n')
f.close()

d = dict()
for x in Countries:
    d[x.name] = x.capital
    d[x.capital] = x.name
N = input("Введите страну или столицу: ")
print(d[N])