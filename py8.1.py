# Задание 1

pets = {input('Имя животного: '): {'type':input('Тип: '), 'age':int(input('Возраст животного: ')), 'owner_name':input('Имя владельца: ')}}

pets_l = list(pets.keys())
animal_l = list(pets[pets_l[0]].values())

print(f'Это {animal_l[0]}', end=' ')
print(f'по кличке "{pets_l[0]}".', end=' ')
    
if animal_l[1] > 4 and animal_l[1] < 21:
    print(f'Возраст: {animal_l[1]} лет.', end=' ')
else:
    i = animal_l[1] % 10
    if i==1:
        print(f'Возраст: {animal_l[1]} год.', end=' ')
    elif i < 5:
        print(f'Возраст: {animal_l[1]} года.', end=' ')
    else:
        print(f'Возраст: {animal_l[1]} лет.', end=' ')      

print(f'Имя хозяина: {animal_l[2]}')


# Другой вариан
'''
pets = {input('Имя животного: '): {'type':input('Тип: '), 'age':int(input('Возраст животного: ')), 'owner_name':input('Имя владельца: ')}}

for  a_name, a_info in pets.items():
    print(f'Это {a_info['type']}', end=' ')
    print(f'по кличке "{a_name}".', end=' ')
    
    if a_info['age'] > 4 and a_info['age'] < 21:
            print(f'Возраст: {a_info['age']} лет.', end=' ')
    else:
        i = a_info['age'] % 10
        if i==1:
            print(f'Возраст: {a_info['age']} год.', end=' ')
        elif i < 5:
            print(f'Возраст: {a_info['age']} года.', end=' ')
        else:
            print(f'Возраст: {a_info['age']} лет.', end=' ')      
   
    print(f'Имя хозяина: {a_info['owner_name']}')
'''
print()
# Задание 2

my_dict = {}

for i in range(10, -6, -1):
    j = 0

    if i >= 0:
        r = 1
        while j < i:
            r *= i
            j += 1
    else:
        r = 1
        if i % 2 == 0:
            while j > i:
                r /= i
                j -= 1
            r *= -1
        else:
            while j > i:
                r /= i
                j -= 1

    my_dict[i] = r
print(my_dict)

input()