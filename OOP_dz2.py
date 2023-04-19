import func

class Tomato: # Класс Tomato
    states = {1: 'planted', # Статические свойства
              2: 'green',
              3: 'yellow',
              4: 'red'}
    def __init__(self,index=1): # Метод __init__
        self._index = index # динамическое protected свойство _index равное 1
        self._state = self.states[self._index] # динамическое protected свойство _state принимает states[1]

    def grow(self): # Метод перевода на следующую стадию созревания
        func.grow_one(self) # Вызов функции grow_one внутри funk.py

    def is_ripe(self): # Метод is_ripe принимает значение
        return self._state == 'red' # возвращает значение созревания

class TomatoBush: # Класс TomatoBush
    def __init__(self, quantity): # Медот __init__ принимает quantity(количество)
        self.quantity = [Tomato() for i in  range(quantity)] # Динамическое свойство quantity список объектов класса Tomato

    def grow_all(self): # Метод grow_all
        func.grow_all_def(self) #  Вызов функции grow_all_def внутри funk.py

    def all_area_ripe(self): # Метод all_area_ripe()
        return all([i.is_ripe() for i in self.quantity]) # Вернёт True если все плоды спелые

    def give_away_all(self): # Метод give_away_all()
        return self.quantity.clear() #Очистит список quantity от данных

class Gardener: # Класс Gardener
    def __init__(self, name, plant): # Метод __init__ принимает два динамических свойства
        self.name = name # Динамическое свойство self.name публичное
        self._plant = plant # Динамическое свойство self._plant prtected

    def work(self): # Метод work
        self._plant.grow_all() # Обратимся к методу внутри TomatoBush grow_all(self) - позволяющий перевести все плоды на стадию вверх

    def harvest(self): # Метод harvest
        func.harvest_all(self) # обратимся к функции harvest_all(self) внутри funk.py

    @staticmethod
    def knowledge_base():
        print(f'Меня зовут {name.name} и у меня даже кактус завял.\n'
              f'В данный момент у нас {len(tomato.quantity)} помидора растут')

tomato = TomatoBush(6)
name = Gardener('Стас', tomato)
Gardener.knowledge_base()
func.funk_input(tomato,name)
Gardener.knowledge_base()