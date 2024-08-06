# Домашнее задание по уроку "Пространство имен"

# 1. Создайте новый проект в PyCharm
# 2. Запустите созданный проект

# Ваша задача:
# 1. Создайте новую функцию def test_function
# 2. Создайте другую функцию внутри функции inner_function, функция должна печатать значение
# "Я в области видимости функции test_function"
# 3. Вызовите функцию inner_function внутри функции test_function
# 4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы


def test_function():    # Создание функции test_function

    def inner_function():   # Создание функции inner_function
        print(f"Я в области видимости функции test_function")
    inner_function()  # Здесь ничего не выводит, т.к. не вызвана внешняя функция test_function

test_function()    # Вызов внешней функции test_function => Выводит значение внутренней функции inner_function
                   # т.к. функция inner_function поподает в область видимости функции test_function

# inner_function()  # Без табуляции (без TAB - отступ).
                    # Не выводит значение внутренней функции. Возникает ошибка:
                    # NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                    # Причина: вызов функции inner_function из глобального пространства имен невозвожен, т.к.
                    # inner_function находится в локальном пространстве функции test_function (т.е. внутри
                    # фукции test_function, а не снаружи). То есть функция inner_function находится
                    # не в области видимости функции test_function.

    # inner_function()  # C табуляцией (TAB - отступ).
                        # Выводит туже ошибку, что и с TAB. Причины теже.