from math import sqrt


def add_numbers(one: int, two: int) -> int:
    return one + two


def CalculateSquareRoot(Number: float) -> float:
    return sqrt(Number)


def calc(your_number: float) -> str:
    if your_number <= 0:
        return f'{your_number} = 0'
    else:
        return (f'Мы вычислили квадратный корень из введённого вами числа. '
                f'Это будет: {CalculateSquareRoot(your_number)}')


one = 10
two = 5

print('Сумма чисел: ', add_numbers(one, two))

print(calc(25.5))
