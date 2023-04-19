# КЛАСС TOMATO
# 1 Создать класс Tomato
# 2 Создать статическое свойство states, которое содержит все стадии созревания томата
# Создать метод __init__(), внутри которого два динамических protected(_впереди) свойства 1._index - предаётся параметром,
#    2._state - принимает первое значение из словаря states.
# 4. Создать метод grow() переводит томат на следующую стадию созревания
# 5. Создать метод is_ripe(),для проверки созревания томата

class Tomato: # Класс Tomato
    states = {1: 'planted', # Статические свойства
              2: 'green',
              3: 'yellow',
              4: 'red'}
    def __init__(self,index=1): # Метод __init__
        self._index = index # динамическое protected свойство _index равное 1
        self._state = self.states[self._index] # динамическое protected свойство _state принимает states[1]

    def grow(self): # Метод grow
        print(self._state) # Вывести данную стадию созревания
        self._index += 1 # Прибавим к индексу 1 для следующей стадии
        if self._state != 'red': # если стадия ещё не красная
            self._state = self.states[self._index] # то присвоим следующую стадию
            return self._state # И вернём значение новой стадии

    def is_ripe(self): # Метод is_ripe принимает значение
        return self._state == 'red' # возвращает значение созревания


class TomatoBush:
    def __init__(self, quantity):
        self.quantity = [Tomato() for i in  range(quantity)]

    def grow_all(self):
        for i in self.quantity:
            i.grow()

    def all_area_ripe(self):
        return all([i.is_ripe() for i in self.quantity])

    def give_away_all(self):
        return self.quantity.clear()

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_area_ripe():
            print(f'Все плоды собраны')
            self._plant.give_away_all()
        else:
            print('Ещё не созрели')

    @staticmethod
    def knowledge_base():
        print(f'Меня зовут {name.name} и у меня даже кактус завял.\n'
              f'В данный момент у нас {len(tomato.quantity)} помидора растут')

if __name__ == '__main__':
    tomato = TomatoBush(2)
    name = Gardener('Стас', tomato)
    Gardener.knowledge_base()
    tomato.all_area_ripe()
    name.work()
    name.harvest()
    name.work()
    name.harvest()
    name.work()
    name.work()
    name.harvest()
    Gardener.knowledge_base()
