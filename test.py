
data = {'Anna':{'city':'Moskva','temperature':'+2','wind':'east'},'Elena':{'city':'Voronezh','temperature':'+6','wind':'west'},'Vasya':{'city':'Vologda','temperature':'+5','wind':'east'}}
name = input('Введите имя: ')
print (data.get(name))