my_dict = {"Artur" : 1980, 'Arsen' : 2009}
print(my_dict)
print(my_dict['Arsen'])
print(my_dict.get('Natalia'))
my_dict.update({'Lera' : 2003, 'Natalia' : 1981})
print(my_dict)
a = my_dict.pop('Lera')
print(my_dict)
print(a)
