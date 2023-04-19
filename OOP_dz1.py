from writer_csv import csv_
from writer_csv import print_
import csv
import time

############################################# OOP #########################################

####################################################################################################################
########################################### Домашка ####################################################################
# Два метода в классе, один принимает в себя либо строку, либо число.
# 1. Если передаём строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине
# слова, выводит все гласные, иначе согласные:
# 2. Если число то, произведение суммы чётных цифр на длину числа
# Длину строки и числа искать во втором методе

class Home_work: # Наш класс
    def __init__(self, num_or_str):
        self.num_or_str = num_or_str

    def int_str(self):
        if self.num_or_str.isalpha():
            count_vowels = []
            consonants = []
            for i in self.num_or_str:
                vowels_us = ['a','e','i','o','u']
                vowels_rus = ['а','я','у','ю','о','е','ё','э','и','ы']
                if i in vowels_us or i in vowels_rus:
                    count_vowels.append(i)
                elif i not in vowels_us or i not in vowels_rus:
                    consonants.append(i)
            if len(count_vowels) * len(consonants) <= final_len:
                return count_vowels
            else:
                return consonants
        elif self.num_or_str.isdigit():
            c = 0
            for i in self.num_or_str:
                if int(i) % 2 == 0:
                    c += int(i)
            return c * final_len
    def len_in(self):
        len_str_or_in = len(self.num_or_str)
        return len_str_or_in

input_user = Home_work(input('Введите слова либо число: ').strip().lower()) # Экземпляр класса
final_len = input_user.len_in() # Переменная принимающая длину строки (len_str_or_in)
print(input_user.int_str()) # Выведем результат функции int_str()

########################################Доп задаание ############################################################
# 1 Создать класс \Сотрудник\
# 2. Определить атрибуты класса: имя, фамилия, должность, зарплата
# 3. Определить конструктор класса для инициализации атрибутов
# 4. Реализовать методы для изменения и получения значений каждого атрибута
# 5. Реализовать метод для вывода информации о сотруднике на экран
# 6. Создать несколько объектов класса "Сотрудник"
# 7. Продемонстрировать работу методов на созданных объектах
#
# Расширение задачи:
# 8. Добавить в класс "Сотрудник" метод для изменения зарплаты на заданное значение
# 9. Добавить в класс "Сотрудник" метод для увеличения зарплаты на заданное процентное значение
# 10. Добавить в класс "Сотрудник" метод для сравнения зарплаты текущего объекта с зарплатой другого объекта класса "Сотрудник"
# 11. Продемонстрировать работу новых методов на созданных объектах.
#
# # **** реализовать метод, который будет записывать в CSV-файл изменение зарплаты по сотруднику
# (в момент изменения зарплаты - создается запись в CSV)

class Employee: # Создали класс сотрудник
    name = 'Petya' # Имеет имя
    last_name = 'Petrov' # Фамилию
    job_title = 'Sis admin' # Должность
    salary = 1500 # Зарплата

    def __init__(self, name, last_name, job_title, salary):  # (Модуль) Инициализация атрибутов
        self.name = name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary

    def change_(self, change_name,  change_last_name, change_job_title, change_salary): # Модуль изменеия данных сотрудников
        self.name = change_name
        self.last_name = change_last_name
        self.job_title = change_job_title
        self.salary = change_salary
        return self.name, self.last_name, self.job_title, self.salary

    def data_all(self): # Вывод все данных про сотрудника
        return self.name, self.last_name, self.job_title, self.salary

    def sharges(self): # Изменение ЗП(salary) в большую сторону числом
        self.salary += 200
        csv_(self, self.name, self.last_name, self.job_title, self.salary)
        return self.salary

    def sharges_procent(self): # Изменение ЗП(salary) в большую процентно
        self.salary = self.salary + self.salary/100*13
        csv_(self, self.name, self.last_name, self.job_title, self.salary)
        return self.salary

    def comparison(self, salary_two_employer): # Модуль сравнения ЗП(salary)
        if self.salary > salary_two_employer:
            return f'ЗП у сотрудника {self.name}, {self.last_name} больше на: {self.salary - salary_two_employer}'
        else:
            return f'ЗП у сотрудника {self.name}, {self.last_name} меньше на: {salary_two_employer- self.salary}'

employee_1 = Employee('Stas', 'Kostyshin', 'sesyrity', 1100) # Данные первого сотрудника
employee_2 = Employee('Keks', 'Pirogok', 'Tehnik', 1400) # Данные второго сотрудника
print(employee_1.salary) # Выведем имя первого сотрудника
printall = print_(employee_1, employee_2) # Функция внутри write_csv
print(Employee.name, Employee.job_title, Employee.salary) # Вывод данных о сотруднике внутри класса
print(employee_1.comparison(Employee.salary)) # Подсчёт Зп между сотрудником вне класса и внутри класса


#________________________________________________________________________________________________________________
#Ещё задачка, если той будет мало. ДЕЛАТЬ ТОЛЬКО ТЕМ, КТО ВЫПОЛНИТ ДЗ И ЗАДАНИЕ ВЫШЕ.
#
# Создайте программу для учета продаж в магазине.
# Создайте классы "Товар", "Покупатель" и "Продавец".
# Класс "Товар" будет содержать свойства: название, цена, количество.
# Класс "Покупатель" будет содержать свойства: имя, фамилия, адрес, номер телефона.
# Класс "Продавец" будет содержать свойства: имя, фамилия, должность, номер телефона.
# Когда покупатель приходит в магазин, он может выбрать товары и купить их у продавца.
# Продавец должен учитывать продажи и хранить информацию о проданных товарах и покупателях.
# Также необходимо добавить методы для поиска товаров по названию и для вывода списка всех проданных товаров.
#
# Возможный дополнительный функционал:
# 1. Добавить возможность добавления новых товаров в магазин.
# 2. Добавить возможность изменения цены и количества товаров.
# 3. Добавить возможность скидок на определенные товары или для определенных покупателей.
# 4. Добавить возможность вывода отчета о продажах за определенный период времени.
# 5. Добавить возможность работы с несколькими продавцами и учета продаж каждого из них отдельно.
# 6. Добавить возможность работы с несколькими магазинами и учета продаж каждого из них отдельно.
# 7. Добавить возможность работы с различными формами оплаты (наличные, карта, онлайн-платежи и т.д.).
# 8. Добавить возможность работы с доставкой товаров (адрес доставки, стоимость доставки и т.д.).
# 9. Добавить возможность работы с различными поставщиками и учета поставок товаров.
# 10. Добавить возможность работы с программой лояльности для покупателей (накопление бонусов за покупки,
# обмен бонусов на скидки и т.д.).
#
#
class Product:
    name = ['Яблоко', 'Груша', 'Слива', 'Онега Чыпсы', 'Импортный ЛЭЙЗ']
    price = [10, 15, 20, 3, 9]
    quantity = [100, 100 , 150, 200, 50]

    def __init__(self, sale):
        self.sale = sale

    def sale_product(self):
        if self.sale in Product.name:
            print(f'Вы купили {self.sale}')
            with open('Salesman.csv', 'a', newline='\n', encoding='UTF-8') as sales:
                write_new = csv.writer(sales)
                text = [time.ctime(), 'Имя:', buyer.name, 'Фамилия: ', buyer.last_name, 'Адрес: ', buyer.address,
                        'Телефон: ', buyer.phone_number, 'купил: ', self.sale]
                write_new.writerow(text)
            return self.sale
        else:
            print(f'Такого товара нет, есть только {self.name}')

class Buyer:
    name = 'Педро'
    last_name = 'Иванов'
    address = 'Челябинская.стрит дом 15'
    phone_number = 8017_323_11_02
    def __init__(self, name, last_name, address, phone_number):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number

class Salesman:
    name = 'Галина'
    last_name = 'Петровна'
    job_title = 'Продавец'
    phone_number = 8029_666_13_66

    def __init__(self):
        self.change = input('Какой проданный товар вы хотите найти?: ')
        with open('Salesman.csv', 'r', encoding='UTF-8') as sales:
            reader = csv.reader(sales)
            for row in reader:
                for i in row:
                    if self.change == i:
                        print(','.join(row))

    @staticmethod
    def all_sales_product():
        with open('Salesman.csv', 'r', encoding='UTF-8') as sales:
            reader = csv.reader(sales)
            for row in reader:
                print(row)


print(Salesman.name,Salesman.last_name,Salesman.job_title,Salesman.phone_number) # Узнать данные продавщицы
# Из класса Salesman

# buyer = Buyer # Назначить главного покупателя из класса Buyer

buyer = Buyer(input('Какой персонаж хочет пойти в магазин Имя: '), input('Фамилия: '),
              input('Адрес проживания: '), input('Телефон '))# Изменить покупателя

print(Product.name) # Узнать наименование продуктов из класса Product

sale = Product(input(f'Какой товар хочет купить {buyer.name}:')).sale_product()

change = Salesman # Присвоим переенной данные класса Salesman
all_sale = Salesman.all_sales_product() # Вывести все проданные товары
change() # Вывести конкретный проданный товар



