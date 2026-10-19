import datetime

name = input("enter your name:")
age = input("enter your age:")
hight = float(input("enter your hight:"))
fav_num = input("enter your favourit number:")

age = int(age)
hight = float(hight)
fav_num = int(fav_num)

current_year = datetime.date.today().year
birth_year = current_year - age

rounded_hight = int(hight)
print(birth_year)

#type 
print(type(name))
print(type(age))
print(type(hight))
print(type(fav_num))

#id
print(id(name))
print(id(age))
print(id(hight))
print(id(fav_num))
