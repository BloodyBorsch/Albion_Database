from enum import Enum


def int_parser(value):
    try:
        return int(value), True
    except:
        return "Вводить можно только цифры", False


class Data_types(Enum):
    test = 1
    tst2 = 2
    test3 = 3
    test4 = 4
