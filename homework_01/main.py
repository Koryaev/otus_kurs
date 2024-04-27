"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args: int):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return[num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    # if even
    if number % 2 == 0:
        return number == 2

    odd = 3
    while odd ** 2 <= number and number % odd != 0:
        odd += 2

    return odd ** 2 > number


def filter_numbers(numbers: list, filter_type: str, ):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == PRIME:
        return list(filter(is_prime, numbers))
    elif filter_type == ODD:
        return list(filter(lambda num: num % 2 == 1, numbers))
    else:
        return list(filter(lambda num: num % 2 == 0, numbers))
