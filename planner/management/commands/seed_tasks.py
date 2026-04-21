from django.core.management.base import BaseCommand

from planner.models import Task
import textwrap


def d(text: str) -> str:
    return textwrap.dedent(text).strip()


TASKS = [
    # Day 1
    {
        "day_index": 1,
        "order": 1,
        "title": "Сумма чётных",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `sum_even(nums)`, которая возвращает сумму всех чётных чисел
            в списке. Если список пустой, верните 0.
            """
        ),
        "starter_code": d(
            """
            def sum_even(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert sum_even([1, 2, 3, 4]) == 6
            assert sum_even([]) == 0
            assert sum_even([2, 2, 2]) == 6
            assert sum_even([1, 3, 5]) == 0
            """
        ),
    },
    {
        "day_index": 1,
        "order": 2,
        "title": "Подсчёт гласных",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `count_vowels(s)`, которая считает количество гласных
            букв в строке. Гласные: a, e, i, o, u, y. Регистр не важен.
            """
        ),
        "starter_code": d(
            """
            def count_vowels(s):
                pass
            """
        ),
        "tests": d(
            """
            assert count_vowels("Hello") == 2
            assert count_vowels("sky") == 1
            assert count_vowels("AEIOU") == 5
            """
        ),
    },
    {
        "day_index": 1,
        "order": 3,
        "title": "Максимум без max",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `max_without_builtin(nums)`, которая возвращает максимум
            списка без использования `max`. Гарантируется, что список не пустой.
            """
        ),
        "starter_code": d(
            """
            def max_without_builtin(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert max_without_builtin([1, 5, 2]) == 5
            assert max_without_builtin([-3, -7]) == -3
            assert max_without_builtin([10]) == 10
            """
        ),
    },
    {
        "day_index": 1,
        "order": 4,
        "title": "Фибоначчи",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `fibonacci(n)`, которая возвращает список из первых `n`
            чисел Фибоначчи, начиная с 0. Примеры: n=0 -> [], n=1 -> [0].
            """
        ),
        "starter_code": d(
            """
            def fibonacci(n):
                pass
            """
        ),
        "tests": d(
            """
            assert fibonacci(0) == []
            assert fibonacci(1) == [0]
            assert fibonacci(5) == [0, 1, 1, 2, 3]
            """
        ),
    },
    {
        "day_index": 1,
        "order": 5,
        "title": "Квадраты положительных",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `square_positives(nums)`, которая возвращает список
            квадратов положительных чисел. Ноль и отрицательные числа игнорируются.
            """
        ),
        "starter_code": d(
            """
            def square_positives(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert square_positives([-2, 0, 3, 4]) == [9, 16]
            assert square_positives([]) == []
            """
        ),
    },
    {
        "day_index": 1,
        "order": 6,
        "title": "Нормализация",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `normalize(nums)`, которая делит каждый элемент на сумму
            списка и возвращает новый список. Если сумма равна 0, верните список из
            нулей той же длины.
            """
        ),
        "starter_code": d(
            """
            def normalize(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert normalize([1, 1, 2]) == [0.25, 0.25, 0.5]
            assert normalize([0, 0]) == [0.0, 0.0]
            """
        ),
    },
    {
        "day_index": 1,
        "order": 7,
        "title": "Слияние и сортировка",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `merge_and_sort(a, b)`, которая объединяет два списка
            чисел и возвращает отсортированный результат.
            """
        ),
        "starter_code": d(
            """
            def merge_and_sort(a, b):
                pass
            """
        ),
        "tests": d(
            """
            assert merge_and_sort([3, 1], [2]) == [1, 2, 3]
            assert merge_and_sort([], [1, 0]) == [0, 1]
            assert merge_and_sort([-1], [-2]) == [-2, -1]
            """
        ),
    },
    {
        "day_index": 1,
        "order": 8,
        "title": "Счётчик",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Counter`. Он должен начинаться с 0 и иметь методы:
            `inc()` (+1), `dec()` (-1) и `value()` (текущее значение).
            """
        ),
        "starter_code": d(
            """
            class Counter:
                def __init__(self):
                    self._value = 0

                def inc(self):
                    pass

                def dec(self):
                    pass

                def value(self):
                    pass
            """
        ),
        "tests": d(
            """
            c = Counter()
            assert c.value() == 0
            c.inc()
            assert c.value() == 1
            c.dec()
            assert c.value() == 0
            """
        ),
    },
    {
        "day_index": 1,
        "order": 9,
        "title": "Точка",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Point(x, y)` с методом `distance_to_origin()`, который
            возвращает расстояние до начала координат.
            """
        ),
        "starter_code": d(
            """
            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

                def distance_to_origin(self):
                    pass
            """
        ),
        "tests": d(
            """
            p = Point(3, 4)
            assert p.distance_to_origin() == 5
            assert Point(0, 0).distance_to_origin() == 0
            """
        ),
    },
    {
        "day_index": 1,
        "order": 10,
        "title": "Банковский счёт",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `BankAccount` с начальным балансом. Методы:
            `deposit(amount)` увеличивает баланс, `withdraw(amount)` снимает деньги
            если хватает средств (возвращает True/False), `get_balance()` возвращает баланс.
            """
        ),
        "starter_code": d(
            """
            class BankAccount:
                def __init__(self, balance=0):
                    self.balance = balance

                def deposit(self, amount):
                    pass

                def withdraw(self, amount):
                    pass

                def get_balance(self):
                    pass
            """
        ),
        "tests": d(
            """
            acc = BankAccount(100)
            acc.deposit(50)
            assert acc.get_balance() == 150
            assert acc.withdraw(70) is True
            assert acc.get_balance() == 80
            assert acc.withdraw(100) is False
            assert acc.get_balance() == 80
            """
        ),
    },
    # Day 2
    {
        "day_index": 2,
        "order": 1,
        "title": "Частоты слов",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `word_frequencies(text)`, которая возвращает словарь
            частот слов. Слова разделены пробелами, регистр не важен.
            """
        ),
        "starter_code": d(
            """
            def word_frequencies(text):
                pass
            """
        ),
        "tests": d(
            """
            assert word_frequencies("One two two") == {"one": 1, "two": 2}
            assert word_frequencies("") == {}
            """
        ),
    },
    {
        "day_index": 2,
        "order": 2,
        "title": "Плоский список",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `flatten(matrix)`, которая превращает список списков
            в плоский список.
            """
        ),
        "starter_code": d(
            """
            def flatten(matrix):
                pass
            """
        ),
        "tests": d(
            """
            assert flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
            assert flatten([]) == []
            """
        ),
    },
    {
        "day_index": 2,
        "order": 3,
        "title": "Палиндром",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `is_palindrome(s)`, которая проверяет, является ли
            строка палиндромом, игнорируя пробелы и регистр.
            """
        ),
        "starter_code": d(
            """
            def is_palindrome(s):
                pass
            """
        ),
        "tests": d(
            """
            assert is_palindrome("А роза упала на лапу Азора") is True
            assert is_palindrome("Python") is False
            """
        ),
    },
    {
        "day_index": 2,
        "order": 4,
        "title": "Две суммы",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `two_sum(nums, target)`, которая возвращает кортеж
            индексов (i, j) таких, что nums[i] + nums[j] == target. Если пары нет,
            верните None. Ищите первую пару в порядке увеличения i, затем j.
            """
        ),
        "starter_code": d(
            """
            def two_sum(nums, target):
                pass
            """
        ),
        "tests": d(
            """
            assert two_sum([2, 7, 11, 15], 9) == (0, 1)
            assert two_sum([3, 2, 4], 6) == (1, 2)
            assert two_sum([1, 2, 3], 7) is None
            """
        ),
    },
    {
        "day_index": 2,
        "order": 5,
        "title": "Длинные слова",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `filter_long(words, n)`, которая возвращает список
            слов длиной больше n.
            """
        ),
        "starter_code": d(
            """
            def filter_long(words, n):
                pass
            """
        ),
        "tests": d(
            """
            assert filter_long(["hi", "python", "code"], 3) == ["python", "code"]
            assert filter_long([], 2) == []
            """
        ),
    },
    {
        "day_index": 2,
        "order": 6,
        "title": "Длины слов",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `map_to_lengths(words)`, которая возвращает список
            длин слов.
            """
        ),
        "starter_code": d(
            """
            def map_to_lengths(words):
                pass
            """
        ),
        "tests": d(
            """
            assert map_to_lengths(["a", "bb", "ccc"]) == [1, 2, 3]
            assert map_to_lengths([]) == []
            """
        ),
    },
    {
        "day_index": 2,
        "order": 7,
        "title": "Сортировка по последней букве",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `sorted_by_last_char(words)`, которая сортирует список
            слов по последнему символу.
            """
        ),
        "starter_code": d(
            """
            def sorted_by_last_char(words):
                pass
            """
        ),
        "tests": d(
            """
            assert sorted_by_last_char(["cat", "dog", "ant"]) == ["dog", "cat", "ant"]
            assert sorted_by_last_char(["a"]) == ["a"]
            """
        ),
    },
    {
        "day_index": 2,
        "order": 8,
        "title": "Стек",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Stack` с методами `push(item)`, `pop()` и `size()`.
            `pop()` должен возвращать None, если стек пуст.
            """
        ),
        "starter_code": d(
            """
            class Stack:
                def __init__(self):
                    self._items = []

                def push(self, item):
                    pass

                def pop(self):
                    pass

                def size(self):
                    pass
            """
        ),
        "tests": d(
            """
            s = Stack()
            assert s.pop() is None
            s.push(1)
            s.push(2)
            assert s.size() == 2
            assert s.pop() == 2
            assert s.pop() == 1
            assert s.pop() is None
            """
        ),
    },
    {
        "day_index": 2,
        "order": 9,
        "title": "Пользователь",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `User` с полями `first_name`, `last_name` и методом
            `full_name()` который возвращает имя и фамилию через пробел.
            """
        ),
        "starter_code": d(
            """
            class User:
                def __init__(self, first_name, last_name):
                    self.first_name = first_name
                    self.last_name = last_name

                def full_name(self):
                    pass
            """
        ),
        "tests": d(
            """
            u = User("Ivan", "Petrov")
            assert u.full_name() == "Ivan Petrov"
            """
        ),
    },
    {
        "day_index": 2,
        "order": 10,
        "title": "Прямоугольник",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Rectangle(width, height)` с методами `area()` и
            `perimeter()`.
            """
        ),
        "starter_code": d(
            """
            class Rectangle:
                def __init__(self, width, height):
                    self.width = width
                    self.height = height

                def area(self):
                    pass

                def perimeter(self):
                    pass
            """
        ),
        "tests": d(
            """
            r = Rectangle(3, 4)
            assert r.area() == 12
            assert r.perimeter() == 14
            """
        ),
    },
    # Day 3
    {
        "day_index": 3,
        "order": 1,
        "title": "Бинарный поиск",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `binary_search(nums, target)` для отсортированного
            списка. Возвращайте индекс или -1, если элемента нет.
            """
        ),
        "starter_code": d(
            """
            def binary_search(nums, target):
                pass
            """
        ),
        "tests": d(
            """
            assert binary_search([1, 3, 5, 7], 5) == 2
            assert binary_search([1, 3, 5, 7], 2) == -1
            """
        ),
    },
    {
        "day_index": 3,
        "order": 2,
        "title": "Пузырьковая сортировка",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `bubble_sort(nums)`, которая возвращает новый список
            с отсортированными значениями.
            """
        ),
        "starter_code": d(
            """
            def bubble_sort(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert bubble_sort([3, 2, 1]) == [1, 2, 3]
            assert bubble_sort([]) == []
            """
        ),
    },
    {
        "day_index": 3,
        "order": 3,
        "title": "Количество простых",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `count_primes(n)`, которая считает количество простых
            чисел от 2 до n включительно.
            """
        ),
        "starter_code": d(
            """
            def count_primes(n):
                pass
            """
        ),
        "tests": d(
            """
            assert count_primes(1) == 0
            assert count_primes(10) == 4
            assert count_primes(20) == 8
            """
        ),
    },
    {
        "day_index": 3,
        "order": 4,
        "title": "НОД",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `gcd(a, b)`, которая вычисляет НОД двух чисел
            алгоритмом Евклида.
            """
        ),
        "starter_code": d(
            """
            def gcd(a, b):
                pass
            """
        ),
        "tests": d(
            """
            assert gcd(48, 18) == 6
            assert gcd(7, 3) == 1
            """
        ),
    },
    {
        "day_index": 3,
        "order": 5,
        "title": "Факториал",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `factorial(n)`, которая вычисляет факториал числа n.
            Используйте рекурсию.
            """
        ),
        "starter_code": d(
            """
            def factorial(n):
                pass
            """
        ),
        "tests": d(
            """
            assert factorial(0) == 1
            assert factorial(5) == 120
            """
        ),
    },
    {
        "day_index": 3,
        "order": 6,
        "title": "Композиция функций",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `compose(f, g)`, которая возвращает новую функцию h,
            где h(x) = f(g(x)).
            """
        ),
        "starter_code": d(
            """
            def compose(f, g):
                pass
            """
        ),
        "tests": d(
            """
            def f(x):
                return x + 1

            def g(x):
                return x * 2

            h = compose(f, g)
            assert h(3) == 7
            """
        ),
    },
    {
        "day_index": 3,
        "order": 7,
        "title": "Уникальные и сортировка",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `unique_sorted(nums)`, которая возвращает отсортированный
            список уникальных значений.
            """
        ),
        "starter_code": d(
            """
            def unique_sorted(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert unique_sorted([3, 1, 2, 3, 1]) == [1, 2, 3]
            assert unique_sorted([]) == []
            """
        ),
    },
    {
        "day_index": 3,
        "order": 8,
        "title": "Таймер",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Timer(seconds)` с методами `tick()` (уменьшает счётчик
            на 1, но не ниже 0), `remaining()` и `is_done()`.
            """
        ),
        "starter_code": d(
            """
            class Timer:
                def __init__(self, seconds):
                    self._seconds = seconds

                def tick(self):
                    pass

                def remaining(self):
                    pass

                def is_done(self):
                    pass
            """
        ),
        "tests": d(
            """
            t = Timer(2)
            assert t.is_done() is False
            t.tick()
            t.tick()
            t.tick()
            assert t.remaining() == 0
            assert t.is_done() is True
            """
        ),
    },
    {
        "day_index": 3,
        "order": 9,
        "title": "Книга",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Book(title, author, pages)` с методом `is_long()`
            (возвращает True, если страниц больше 300).
            """
        ),
        "starter_code": d(
            """
            class Book:
                def __init__(self, title, author, pages):
                    self.title = title
                    self.author = author
                    self.pages = pages

                def is_long(self):
                    pass
            """
        ),
        "tests": d(
            """
            b = Book("Title", "Author", 350)
            assert b.is_long() is True
            assert Book("S", "A", 120).is_long() is False
            """
        ),
    },
    {
        "day_index": 3,
        "order": 10,
        "title": "Температура",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Temperature` с полем celsius. Методы:
            `to_fahrenheit()` и `from_fahrenheit(f)` (classmethod), который
            возвращает экземпляр Temperature.
            """
        ),
        "starter_code": d(
            """
            class Temperature:
                def __init__(self, celsius):
                    self.celsius = celsius

                def to_fahrenheit(self):
                    pass

                @classmethod
                def from_fahrenheit(cls, f):
                    pass
            """
        ),
        "tests": d(
            """
            t = Temperature(0)
            assert t.to_fahrenheit() == 32
            t2 = Temperature.from_fahrenheit(212)
            assert t2.celsius == 100
            """
        ),
    },
    # Day 4
    {
        "day_index": 4,
        "order": 1,
        "title": "Слияние словарей",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `merge_dicts(a, b)`, которая объединяет два словаря.
            Если ключи совпадают, значения суммируются.
            """
        ),
        "starter_code": d(
            """
            def merge_dicts(a, b):
                pass
            """
        ),
        "tests": d(
            """
            assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 1}) == {"a": 1, "b": 5, "c": 1}
            assert merge_dicts({}, {"x": 1}) == {"x": 1}
            """
        ),
    },
    {
        "day_index": 4,
        "order": 2,
        "title": "Группировка по первой букве",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `group_by_first_letter(words)`, которая возвращает
            словарь: первая буква -> список слов, сохраняя порядок.
            """
        ),
        "starter_code": d(
            """
            def group_by_first_letter(words):
                pass
            """
        ),
        "tests": d(
            """
            assert group_by_first_letter(["apple", "apricot", "banana"]) == {"a": ["apple", "apricot"], "b": ["banana"]}
            assert group_by_first_letter([]) == {}
            """
        ),
    },
    {
        "day_index": 4,
        "order": 3,
        "title": "Поворот списка",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `rotate_list(nums, k)`, которая поворачивает список
            вправо на k шагов. Если k больше длины, используйте остаток.
            """
        ),
        "starter_code": d(
            """
            def rotate_list(nums, k):
                pass
            """
        ),
        "tests": d(
            """
            assert rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]
            assert rotate_list([1, 2, 3, 4], 5) == [4, 1, 2, 3]
            assert rotate_list([], 3) == []
            """
        ),
    },
    {
        "day_index": 4,
        "order": 4,
        "title": "Самая длинная серия",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `longest_run(nums)`, которая возвращает длину самой
            длинной серии одинаковых подряд идущих элементов.
            """
        ),
        "starter_code": d(
            """
            def longest_run(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert longest_run([1, 1, 2, 2, 2, 3]) == 3
            assert longest_run([5]) == 1
            assert longest_run([]) == 0
            """
        ),
    },
    {
        "day_index": 4,
        "order": 5,
        "title": "Применение функций",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `apply_funcs(x, funcs)`, которая применяет список
            функций к значению x и возвращает список результатов.
            """
        ),
        "starter_code": d(
            """
            def apply_funcs(x, funcs):
                pass
            """
        ),
        "tests": d(
            """
            def f(x):
                return x + 1

            def g(x):
                return x * 2

            assert apply_funcs(3, [f, g]) == [4, 6]
            assert apply_funcs(5, []) == []
            """
        ),
    },
    {
        "day_index": 4,
        "order": 6,
        "title": "Удаление None",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `filter_none(values)`, которая возвращает список
            без значений None.
            """
        ),
        "starter_code": d(
            """
            def filter_none(values):
                pass
            """
        ),
        "tests": d(
            """
            assert filter_none([1, None, 2, None, 3]) == [1, 2, 3]
            assert filter_none([]) == []
            """
        ),
    },
    {
        "day_index": 4,
        "order": 7,
        "title": "Сумма по ключу",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `sum_by_key(items, key)`, которая суммирует значения
            указанного ключа в списке словарей. Отсутствующие ключи игнорируются.
            """
        ),
        "starter_code": d(
            """
            def sum_by_key(items, key):
                pass
            """
        ),
        "tests": d(
            """
            items = [{"a": 2}, {"a": 3, "b": 1}, {"b": 5}]
            assert sum_by_key(items, "a") == 5
            assert sum_by_key(items, "b") == 6
            """
        ),
    },
    {
        "day_index": 4,
        "order": 8,
        "title": "Сотрудник и менеджер",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Employee(name, salary)` с методом `annual_salary()`.
            Создайте подкласс `Manager` с дополнительным полем `bonus`.
            `annual_salary()` у менеджера = 12 * salary + bonus.
            """
        ),
        "starter_code": d(
            """
            class Employee:
                def __init__(self, name, salary):
                    self.name = name
                    self.salary = salary

                def annual_salary(self):
                    pass

            class Manager(Employee):
                def __init__(self, name, salary, bonus):
                    super().__init__(name, salary)
                    self.bonus = bonus

                def annual_salary(self):
                    pass
            """
        ),
        "tests": d(
            """
            e = Employee("A", 1000)
            assert e.annual_salary() == 12000
            m = Manager("B", 2000, 5000)
            assert m.annual_salary() == 29000
            """
        ),
    },
    {
        "day_index": 4,
        "order": 9,
        "title": "Вектор 2D",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Vector2D(x, y)` с методом `add(other)` (возвращает новый
            Vector2D) и методом `as_tuple()`.
            """
        ),
        "starter_code": d(
            """
            class Vector2D:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

                def add(self, other):
                    pass

                def as_tuple(self):
                    pass
            """
        ),
        "tests": d(
            """
            v1 = Vector2D(1, 2)
            v2 = Vector2D(3, 4)
            v3 = v1.add(v2)
            assert v3.as_tuple() == (4, 6)
            """
        ),
    },
    {
        "day_index": 4,
        "order": 10,
        "title": "Логирующий список",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `LoggedList` с методом `add(item)` и свойством `log`
            (список строк вида "add:<item>" для каждой операции).
            """
        ),
        "starter_code": d(
            """
            class LoggedList:
                def __init__(self):
                    self.items = []
                    self.log = []

                def add(self, item):
                    pass
            """
        ),
        "tests": d(
            """
            l = LoggedList()
            l.add("a")
            l.add("b")
            assert l.items == ["a", "b"]
            assert l.log == ["add:a", "add:b"]
            """
        ),
    },
    # Day 5
    {
        "day_index": 5,
        "order": 1,
        "title": "Парсинг CSV",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `parse_csv_line(line)`, которая разбивает строку по
            запятым и возвращает список значений без лишних пробелов.
            """
        ),
        "starter_code": d(
            """
            def parse_csv_line(line):
                pass
            """
        ),
        "tests": d(
            """
            assert parse_csv_line("a, b, c") == ["a", "b", "c"]
            assert parse_csv_line("one") == ["one"]
            """
        ),
    },
    {
        "day_index": 5,
        "order": 2,
        "title": "Подсчёт символа",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `count_char(s, ch)`, которая возвращает количество
            вхождений символа ch в строке.
            """
        ),
        "starter_code": d(
            """
            def count_char(s, ch):
                pass
            """
        ),
        "tests": d(
            """
            assert count_char("banana", "a") == 3
            assert count_char("", "a") == 0
            """
        ),
    },
    {
        "day_index": 5,
        "order": 3,
        "title": "Пропущенное число",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Дан список чисел от 1 до n с одной пропущенной. Напишите функцию
            `find_missing(nums)` которая возвращает пропущенное число.
            """
        ),
        "starter_code": d(
            """
            def find_missing(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert find_missing([1, 2, 4, 5]) == 3
            assert find_missing([2, 3, 1, 5, 6]) == 4
            """
        ),
    },
    {
        "day_index": 5,
        "order": 4,
        "title": "Слияние интервалов",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `merge_intervals(intervals)` для объединения
            пересекающихся интервалов. Интервалы могут быть не отсортированы.
            """
        ),
        "starter_code": d(
            """
            def merge_intervals(intervals):
                pass
            """
        ),
        "tests": d(
            """
            result = merge_intervals([(1, 3), (2, 6), (8, 10)])
            assert [tuple(x) for x in result] == [(1, 6), (8, 10)]
            result = merge_intervals([(5, 7), (1, 2)])
            assert [tuple(x) for x in result] == [(1, 2), (5, 7)]
            """
        ),
    },
    {
        "day_index": 5,
        "order": 5,
        "title": "Фабрика умножителей",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `make_multiplier(k)`, которая возвращает функцию
            умножения на k.
            """
        ),
        "starter_code": d(
            """
            def make_multiplier(k):
                pass
            """
        ),
        "tests": d(
            """
            times3 = make_multiplier(3)
            assert times3(4) == 12
            """
        ),
    },
    {
        "day_index": 5,
        "order": 6,
        "title": "Конвейер",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `pipeline(x, funcs)`, которая применяет список функций
            последовательно к x.
            """
        ),
        "starter_code": d(
            """
            def pipeline(x, funcs):
                pass
            """
        ),
        "tests": d(
            """
            def inc(x):
                return x + 1

            def double(x):
                return x * 2

            assert pipeline(3, [inc, double]) == 8
            assert pipeline(3, []) == 3
            """
        ),
    },
    {
        "day_index": 5,
        "order": 7,
        "title": "Сумма через reduce",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `reduce_sum(nums)`, которая суммирует список, используя
            `functools.reduce` (без встроенной `sum`).
            """
        ),
        "starter_code": d(
            """
            def reduce_sum(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert reduce_sum([1, 2, 3]) == 6
            assert reduce_sum([]) == 0
            """
        ),
    },
    {
        "day_index": 5,
        "order": 8,
        "title": "Очередь",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Queue` с методами `enqueue(item)`, `dequeue()` и `size()`.
            `dequeue()` возвращает None, если очередь пустая.
            """
        ),
        "starter_code": d(
            """
            class Queue:
                def __init__(self):
                    self._items = []

                def enqueue(self, item):
                    pass

                def dequeue(self):
                    pass

                def size(self):
                    pass
            """
        ),
        "tests": d(
            """
            q = Queue()
            assert q.dequeue() is None
            q.enqueue(1)
            q.enqueue(2)
            assert q.size() == 2
            assert q.dequeue() == 1
            assert q.dequeue() == 2
            assert q.dequeue() is None
            """
        ),
    },
    {
        "day_index": 5,
        "order": 9,
        "title": "Задача",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `TodoItem(text)` с полем `done` (False по умолчанию)
            и методом `toggle()` для переключения состояния.
            """
        ),
        "starter_code": d(
            """
            class TodoItem:
                def __init__(self, text):
                    self.text = text
                    self.done = False

                def toggle(self):
                    pass
            """
        ),
        "tests": d(
            """
            t = TodoItem("task")
            assert t.done is False
            t.toggle()
            assert t.done is True
            """
        ),
    },
    {
        "day_index": 5,
        "order": 10,
        "title": "Круг",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Circle(radius)` с методами `area()` и `circumference()`.
            Используйте math.pi.
            """
        ),
        "starter_code": d(
            """
            class Circle:
                def __init__(self, radius):
                    self.radius = radius

                def area(self):
                    pass

                def circumference(self):
                    pass
            """
        ),
        "tests": d(
            """
            c = Circle(1)
            assert round(c.area(), 5) == 3.14159
            assert round(c.circumference(), 5) == 6.28319
            """
        ),
    },
    # Day 6
    {
        "day_index": 6,
        "order": 1,
        "title": "Анаграммы",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `is_anagram(a, b)`, которая проверяет, являются ли строки
            анаграммами, игнорируя пробелы и регистр.
            """
        ),
        "starter_code": d(
            """
            def is_anagram(a, b):
                pass
            """
        ),
        "tests": d(
            """
            assert is_anagram("Listen", "Silent") is True
            assert is_anagram("Hello", "World") is False
            """
        ),
    },
    {
        "day_index": 6,
        "order": 2,
        "title": "Транспонирование матрицы",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `matrix_transpose(matrix)`, которая транспонирует
            прямоугольную матрицу (список списков).
            """
        ),
        "starter_code": d(
            """
            def matrix_transpose(matrix):
                pass
            """
        ),
        "tests": d(
            """
            result = matrix_transpose([[1, 2, 3], [4, 5, 6]])
            assert [list(row) for row in result] == [[1, 4], [2, 5], [3, 6]]
            assert matrix_transpose([]) == []
            """
        ),
    },
    {
        "day_index": 6,
        "order": 3,
        "title": "Минимум и максимум",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `min_max(nums)`, которая возвращает кортеж (min, max).
            Список гарантированно не пустой.
            """
        ),
        "starter_code": d(
            """
            def min_max(nums):
                pass
            """
        ),
        "tests": d(
            """
            assert min_max([3, 1, 2, 5, 4]) == (1, 5)
            assert min_max([-1, -5, 0]) == (-5, 0)
            """
        ),
    },
    {
        "day_index": 6,
        "order": 4,
        "title": "RLE кодирование",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `run_length_encode(s)`, которая возвращает список
            пар (символ, количество подряд).
            """
        ),
        "starter_code": d(
            """
            def run_length_encode(s):
                pass
            """
        ),
        "tests": d(
            """
            result = run_length_encode("aaabbc")
            assert [tuple(x) for x in result] == [("a", 3), ("b", 2), ("c", 1)]
            assert run_length_encode("") == []
            """
        ),
    },
    {
        "day_index": 6,
        "order": 5,
        "title": "take_while",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `take_while(nums, predicate)`, которая возвращает
            префикс списка до первого элемента, который не удовлетворяет predicate.
            """
        ),
        "starter_code": d(
            """
            def take_while(nums, predicate):
                pass
            """
        ),
        "tests": d(
            """
            assert take_while([2, 4, 1, 6], lambda x: x % 2 == 0) == [2, 4]
            assert take_while([1, 2, 3], lambda x: x < 0) == []
            """
        ),
    },
    {
        "day_index": 6,
        "order": 6,
        "title": "any_match",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `any_match(nums, predicate)`, которая возвращает True,
            если есть хотя бы один элемент, удовлетворяющий predicate.
            """
        ),
        "starter_code": d(
            """
            def any_match(nums, predicate):
                pass
            """
        ),
        "tests": d(
            """
            assert any_match([1, 3, 5], lambda x: x % 2 == 0) is False
            assert any_match([1, 4, 5], lambda x: x % 2 == 0) is True
            """
        ),
    },
    {
        "day_index": 6,
        "order": 7,
        "title": "partition",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `partition(nums, predicate)`, которая возвращает кортеж
            (trues, falses), сохраняя порядок элементов.
            """
        ),
        "starter_code": d(
            """
            def partition(nums, predicate):
                pass
            """
        ),
        "tests": d(
            """
            assert partition([1, 2, 3, 4], lambda x: x % 2 == 0) == ([2, 4], [1, 3])
            assert partition([], lambda x: True) == ([], [])
            """
        ),
    },
    {
        "day_index": 6,
        "order": 8,
        "title": "Полином",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Polynomial(coeffs)` где coeffs — список коэффициентов
            от свободного члена. Метод `evaluate(x)` вычисляет значение.
            """
        ),
        "starter_code": d(
            """
            class Polynomial:
                def __init__(self, coeffs):
                    self.coeffs = coeffs

                def evaluate(self, x):
                    pass
            """
        ),
        "tests": d(
            """
            p = Polynomial([1, 2, 3])  # 1 + 2x + 3x^2
            assert p.evaluate(2) == 17
            """
        ),
    },
    {
        "day_index": 6,
        "order": 9,
        "title": "Инвентарь",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `InventoryItem(name, qty)` с методами `add(n)` и
            `remove(n)` (если n > qty, возвращает False и не меняет qty).
            """
        ),
        "starter_code": d(
            """
            class InventoryItem:
                def __init__(self, name, qty):
                    self.name = name
                    self.qty = qty

                def add(self, n):
                    pass

                def remove(self, n):
                    pass
            """
        ),
        "tests": d(
            """
            item = InventoryItem("apples", 5)
            item.add(3)
            assert item.qty == 8
            assert item.remove(10) is False
            assert item.qty == 8
            assert item.remove(4) is True
            assert item.qty == 4
            """
        ),
    },
    {
        "day_index": 6,
        "order": 10,
        "title": "Простой кэш",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `SimpleCache(capacity)` с методами `set(key, value)` и
            `get(key)`. Когда размер превышает capacity, удаляется самый старый ключ
            по времени добавления/обновления. `get` не влияет на порядок.
            Если ключ уже есть, значение обновляется и считается новым.
            """
        ),
        "starter_code": d(
            """
            class SimpleCache:
                def __init__(self, capacity):
                    self.capacity = capacity
                    self._items = {}
                    self._order = []

                def set(self, key, value):
                    pass

                def get(self, key):
                    pass
            """
        ),
        "tests": d(
            """
            cache = SimpleCache(2)
            cache.set("a", 1)
            cache.set("b", 2)
            assert cache.get("a") == 1
            cache.set("c", 3)
            assert cache.get("a") is None
            assert cache.get("b") == 2
            cache.set("a", 10)
            assert cache.get("a") == 10
            """
        ),
    },
    # Day 7
    {
        "day_index": 7,
        "order": 1,
        "title": "Сбалансированные скобки",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `balanced_brackets(s)`, которая проверяет корректность
            скобочной последовательности с символами (), [], {}.
            """
        ),
        "starter_code": d(
            """
            def balanced_brackets(s):
                pass
            """
        ),
        "tests": d(
            """
            assert balanced_brackets("([]){}") is True
            assert balanced_brackets("([)]") is False
            assert balanced_brackets("(((") is False
            """
        ),
    },
    {
        "day_index": 7,
        "order": 2,
        "title": "Топ K",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `top_k(nums, k)`, которая возвращает k наибольших
            элементов в порядке убывания. Если k больше длины, верните все.
            """
        ),
        "starter_code": d(
            """
            def top_k(nums, k):
                pass
            """
        ),
        "tests": d(
            """
            assert top_k([3, 1, 5, 2, 4], 3) == [5, 4, 3]
            assert top_k([1, 2], 5) == [2, 1]
            """
        ),
    },
    {
        "day_index": 7,
        "order": 3,
        "title": "Разложение на множители",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `prime_factors(n)`, которая возвращает список простых
            множителей числа n в порядке возрастания.
            """
        ),
        "starter_code": d(
            """
            def prime_factors(n):
                pass
            """
        ),
        "tests": d(
            """
            assert prime_factors(60) == [2, 2, 3, 5]
            assert prime_factors(13) == [13]
            """
        ),
    },
    {
        "day_index": 7,
        "order": 4,
        "title": "Слова по длине",
        "style": Task.STYLE_PROCEDURAL,
        "description": d(
            """
            Напишите функцию `count_words_by_length(text)`, которая возвращает словарь
            длина -> количество слов.
            """
        ),
        "starter_code": d(
            """
            def count_words_by_length(text):
                pass
            """
        ),
        "tests": d(
            """
            assert count_words_by_length("one two three") == {3: 2, 5: 1}
            assert count_words_by_length("") == {}
            """
        ),
    },
    {
        "day_index": 7,
        "order": 5,
        "title": "map_dict",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `map_dict(values, func)`, которая применяет func
            к каждому элементу и возвращает новый список.
            """
        ),
        "starter_code": d(
            """
            def map_dict(values, func):
                pass
            """
        ),
        "tests": d(
            """
            assert map_dict([1, 2, 3], lambda x: x * x) == [1, 4, 9]
            assert map_dict([], lambda x: x) == []
            """
        ),
    },
    {
        "day_index": 7,
        "order": 6,
        "title": "flat_map",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `flat_map(values, func)`, где func возвращает список,
            а результатом будет один плоский список.
            """
        ),
        "starter_code": d(
            """
            def flat_map(values, func):
                pass
            """
        ),
        "tests": d(
            """
            assert flat_map([1, 2, 3], lambda x: [x, -x]) == [1, -1, 2, -2, 3, -3]
            assert flat_map([], lambda x: [x]) == []
            """
        ),
    },
    {
        "day_index": 7,
        "order": 7,
        "title": "Каррирование",
        "style": Task.STYLE_FUNCTIONAL,
        "description": d(
            """
            Напишите функцию `curry_add(a)`, которая возвращает функцию, добавляющую a.
            """
        ),
        "starter_code": d(
            """
            def curry_add(a):
                pass
            """
        ),
        "tests": d(
            """
            add5 = curry_add(5)
            assert add5(3) == 8
            """
        ),
    },
    {
        "day_index": 7,
        "order": 8,
        "title": "Сериализация",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Serializer` с методами `to_json(obj)` и `from_json(s)`
            с использованием модуля json.
            """
        ),
        "starter_code": d(
            """
            class Serializer:
                def to_json(self, obj):
                    pass

                def from_json(self, s):
                    pass
            """
        ),
        "tests": d(
            """
            s = Serializer()
            data = {"a": 1, "b": [1, 2]}
            json_str = s.to_json(data)
            assert s.from_json(json_str) == data
            """
        ),
    },
    {
        "day_index": 7,
        "order": 9,
        "title": "Наследование фигур",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте базовый класс `Shape` с методом `area()` (выбрасывает
            NotImplementedError) и класс `Square(side)` с переопределением area().
            """
        ),
        "starter_code": d(
            """
            class Shape:
                def area(self):
                    raise NotImplementedError

            class Square(Shape):
                def __init__(self, side):
                    self.side = side

                def area(self):
                    pass
            """
        ),
        "tests": d(
            """
            sq = Square(4)
            assert sq.area() == 16
            """
        ),
    },
    {
        "day_index": 7,
        "order": 10,
        "title": "Таблица лидеров",
        "style": Task.STYLE_OOP,
        "description": d(
            """
            Создайте класс `Leaderboard` с методами `add(score)` и `top(n)`,
            который возвращает n лучших результатов по убыванию.
            """
        ),
        "starter_code": d(
            """
            class Leaderboard:
                def __init__(self):
                    self._scores = []

                def add(self, score):
                    pass

                def top(self, n):
                    pass
            """
        ),
        "tests": d(
            """
            lb = Leaderboard()
            lb.add(10)
            lb.add(30)
            lb.add(20)
            assert lb.top(2) == [30, 20]
            assert lb.top(10) == [30, 20, 10]
            """
        ),
    },
]


class Command(BaseCommand):
    help = "Seed weekly tasks into the database."

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true", help="Delete existing tasks before seeding")

    def handle(self, *args, **options):
        if options["reset"]:
            Task.objects.all().delete()

        created = 0
        updated = 0
        for task_data in TASKS:
            defaults = {
                "title": task_data["title"],
                "style": task_data["style"],
                "description": task_data["description"],
                "starter_code": task_data["starter_code"],
                "tests": task_data["tests"],
            }
            task, was_created = Task.objects.update_or_create(
                day_index=task_data["day_index"],
                order=task_data["order"],
                defaults=defaults,
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(f"Tasks seeded. Created: {created}, Updated: {updated}"))
