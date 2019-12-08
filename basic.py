import datetime
print('Waktu Sekarang adalah ',datetime.datetime.now())

# Variabel
mynow =  datetime.datetime.now()
print(mynow)

print(datetime.datetime.now())

# Menggabungkan INT & STR
number = 10
string = 'Agung Triyadi'
print(number, string)

# Simple Types
a = 10
b = '10'
c = 10.1

sum1 = a+a
sum2 = b+b
sum3 = c+c

print(sum1, sum2, sum3)
print(type(a), type(b), type(c))

# List
students_grades = [9,8,7,6,5,4,3,2,1]
print(list(range(1,10)))
print(list(range(1, 10, 2)))
print(list(range(1, 20, 3)))
dalam = [1.2, 5, '6',[0,9,8]]

# Calculating List
sum_list = sum(students_grades)
length = len(students_grades)
mean = sum_list / length
print(mean)

#Dictionary
my_dict = {'agung': 100, 'yanuar': 70, 'David': 80, 'Sabil': 85}

#Tupple
my_tupple = (4,3,2,1)
print(my_tupple)