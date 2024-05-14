def int_parser(value):
    try:
        return int(value), True
    except:
        return "Вводить можно только цифры", False