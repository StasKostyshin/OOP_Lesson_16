import string
# 1 Создайте класс Human
# 2 Создайте для него два статических поля: default_name b default_age
# 3 Создайте метод __init__(), который по умолчанию помимо self принимает ещё
# два параметра: name и age. Для этих параметров задайте значения по умолчанию,
# используя свойства default_name и default_age. В методе __init__ определите четыре свойства:
# Публичные - name и age. Приватные - money и house
# 4 Реализуйте справочный метод info(), который будет выводить поля name, age, house, money
# 5 Реализуйте справочный статический метод default_info(), который будет выводить статические
# поля default_name и default_age
# 6 Реализуйте метод earn_money(), увеличивающий значение свойства money

# class Human:
#     # Статические поля
#     default_name = "No name"
#     default_age = 0
#
#     def __init__(self, name = default_name, age = default_age):
#         # Динамические поля
#         # Публичные
#         self.name = name
#         self.age = age
#         # Приватные
#         self.__money = 0
#         self.__house = None
# #
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.__house}')
#
#     @staticmethod
#     def default_info():
#         print(f'Default Name: {Human.default_name}')
#         print(f'Default Name: {Human.default_age}')
#
#
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earned {amount} money! Current value: {self.__money}')
#
#
#     def buy_house(self, house, discount):
#         price = house.final_price(discount)
#         if self.__money >=price:
#             self.__make_deal(house, price)
#         else:
#             print('Not enough money!')
#
#
#     def __make_deal(self, house, price):
#         self.__money -= price
#         self.__house = house

# Тесты
# 1 Вызовите справочный метод default_info() для класса Human()
# 2 Создайте объект класса Human
# 3 Выведите справочную информацию о созданном объекте (вызовите метод info()).
# 4 Поправьте финансовое положение объекта - вызовите метод earn_money()
# 5 Посмотрите, как изменилось состояние объекта класса Human

# Допишем
# 1 Создать класс House
# 2 Создать метод __init__() и определить внутри него два динамических свойства: _area и _price.
# 3 Свои начальные значения они получают из параметров метода __init__()
# 4 Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учётом данной скидки
#
# 1 Создать класс SmallHouse
# 2 Внутри класса SmallHouse переопределить метод __init__(), так что бы он создавал объект с площадью 40м2
#
# 1 Реализуйте приватный метод make_deal, который будет отвечать за техническую реализацию покупки дома:
# уменьшать кол-во денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов
# данный метод принимает объект дома и его цену
# 2 Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки,
# и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль.
# Параметры метода: ссылка на дом и размер скидки


# class House:
#     def __init__(self, area, price):
#         self._area = area
#         self._price = price
#
#     def final_price(self, discount):
#         final_price = self._price/100*discount
#         print(f'Final price: {final_price}')
#         return final_price
# #
# #
# class SmallHouse(House):
#     default_are = 40
#     def __init__(self, price):
#         super().__init__(SmallHouse.default_are, price)
# #
#
# if __name__ == '__main__':
#     Human.default_info()
#
#     alex = Human('Sasha', 27)
#     alex.info()
#
#     small_house = SmallHouse(8500) # Создали объект класса SmallHouse
#     alex.buy_house(small_house, 5)
#
#     alex.earn_money(5000)
#     alex.buy_house(small_house, 5)
#
#     alex.earn_money(20000)
#     alex.buy_house(small_house, 5)
#     alex.info()

class Alphabet: # Создали класс
    def __init__(self, lang, letters): # передаём два динамических свойства lang, letters
        self.lang = lang # Язык
        self.letters = list(letters) # Список букв

    def print(self): # Метод print
        return self.letters # для вывода в консоль букв из списка list(letters)

    def letters_num(self): # Метод для возврата кол-во букв
        return len(self.letters) # в списке list(letters)

class EngAlphabet(Alphabet): # Класс EngAlphabet наследует от класса Alphabet
    __letters_num = 26 # __Приватное Статическое свойство

    def __init__(self): # метод __init__ который вызывает родительский метод __init__ (super().__init__)
        super().__init__('Eng', string.ascii_letters) # Присвоим self.lang "En" и self.letters = string.ascii_letters

    def is_en_letter(self, letter): # Метод принимающий string.ascii_letters в качестве self и letter заданная пользователем
        if letter in self.letters: # Если letter есть в string.ascii_letters (self.letters)
            return f'{letter} in Eng' # Вернёт ответ, что есть
        return f'{letter} not in Eng' # Вернёт ответ, что нет

    def letters_num(self): # Переопределили метод и letters_num
        return EngAlphabet.__letters_num # Возвращает значение Приватного статического свойства __letters_num

    @staticmethod
    def example(): # Статический метод
        return f"I'm not understand you, dude !" # Вернёт текс на Английском языке

# Тесты
if __name__ == '__main__':
    search = EngAlphabet()
    print(search.print())
    print(search.letters_num())
    print(len(search.print()))
    print(search.is_en_letter('F'))
    print(search.is_en_letter('Щ'))
    print(EngAlphabet.example())













