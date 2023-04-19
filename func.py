
def grow_one(self):  # Функция созревания
    print(self._state)  # Вывести данную стадию созревания
    self._index += 1  # Прибавим к индексу 1 для следующей стадии
    if self._state != 'red':  # если стадия ещё не красная
        self._state = self.states[self._index]  # то присвоим следующую стадию
        return self._state  # И вернём значение новой стадии

def grow_all_def(self): # Функция перевода всех плодов на следующюю стадию созревания
    for i in self.quantity:
        i.grow() # Путем обращения к методу внутри класса

def harvest_all(self): # Функция harvest_all(self) принимает объект self
    if self._plant.all_area_ripe(): # обратимся к self._plant внутри класс Gardener и вызовем модуль all_area_ripe() внутри TomatoBush
        print(f'Все плоды собраны')
        self._plant.give_away_all() # обратимся к self._plant внутри класс Gardener и вызовем модул give_away_all() внутри TomatoBush
    else:
        print('Ещё не созрели')

def funk_input(tomato, name): # Тесты по созреванию и сбору урожая
    tomato.all_area_ripe()
    name.work()
    name.harvest()
    name.work()
    name.harvest()
    name.work()
    name.work()
    name.harvest()


