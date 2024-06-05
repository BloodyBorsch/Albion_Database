def int_parser(value):
    try:
        return int(value), True
    except:
        return "Вводить можно только цифры", False
    
def list_parser(dirty_list, id=None):
    temp_list = list()

    for x in dirty_list:
        if x == dirty_list[0]:
            temp_list.append(x.value.title().rstrip())
            continue
        temp_list.append(x.value)

    if id != None:
        temp_list.append(id)

    return temp_list