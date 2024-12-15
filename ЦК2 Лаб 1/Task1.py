# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Drink:
    def __init__(self, name: str, volume: float, occupied_volume: float):
        if not isinstance(name,(str)):
            raise TypeError ("Назввание должно быть типа str")
        self.name = name

        if not isinstance(volume,(int,float)):
            raise TypeError("Объем должен быть типа int или float")
        if volume < 0:
            raise ValueError("Объем не может быть отрицательным числом")
        self.volume = volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume <= 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_drink(self) -> bool:
        """
               Функция которая проверяет является ли стакан пустым

               :return: Правда или ложь
        """
        ...

class Car:
    def __init__(self, colour: str, run: int, max_speed: float):
        if not isinstance(colour, str):
            raise TypeError("Назввание должно быть типа str")
        if colour != ('red','green', 'blue', 'white'):
            raise ValueError ("Данный цвет выбрать нельзя")
        self.colour = colour

        if not isinstance(run, int):
            raise TypeError("Пробег должен быть типа int ")
        self.run = run

        if not isinstance (max_speed, (int, float)):
            raise TypeError(" Максимальная скорость должна быть типа int или float ")
        if max_speed < 0:
            raise ValueError(" Скорость не может быть отрицательным числом ")
        self.max_speed = max_speed

    def exist_catalog(self) -> None:
        """
        Проверка наличия машины по заданным параметрам в каталоге

        """
        ...

class People:
   def __init__(self, name: str, age: int, sex: str):
       if not isinstance(name, str):
           raise TypeError("Имя должно быть типа str")
       self.name = name

       if not isinstance(age, int):
           raise TypeError("Возраст должен быть типа int ")
       if age <= 0:
           raise ValueError("Возраст не может быть отрицательным числом")
       self.age = age

       if not isinstance(sex, str):
           raise TypeError("Пол должен быть типа str")
       if sex != ('мужчина', 'женщина'):
           raise ValueError("Пол может быть только мужчина или женщина")
       self.sex = sex

   def list_of_people(self) -> list:
        """
        Функция которая составит список со всеми мужчинами
        """

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

