# **Задание 2. InvalidAgeError**Напишите свой класс `InvalidAgeError`
# для обработки исключений.
# Класс используется в следующем коде:

class InvalidAgeError(Exception):
    def __init__(self, message='Ошибка определения возраста'):
        super().__init__(message)  # Переопределяем от родительского класса данный метод

    # def __str__(self):  Можно использовать как вариант, если не переопределять метед __init__
    #     return self.message


if __name__ == '__main__':
    age = int(input('Введите ваш возраст: '))
    if age < 0:
        raise InvalidAgeError('Возраст не может быть отрицательным числом')
    if age > 120:
        raise InvalidAgeError
    print(f'Вам {age} :)')


# Введите ваш возраст: 25
# Вам 25 :)
# Введите ваш возраст: -255
# InvalidAgeError: Возраст не может быть отрицательным числом
# Введите ваш возраст: 255
# InvalidAgeError: Ошибка определения возраста
