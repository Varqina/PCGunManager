# todo color selection

def run_search(text, gun_list):
    # datbase lista slownikow
    # robimy AND, OR, !=, = empty, >, <, >=, <=, *, !
    text = text.lower()
    a = ''
    if 'and' in text or 'or' in text:
        text.count('and')

    if '=' in text:
        result_gun_list = find_value_with_equal_property(text, gun_list)
    else:
        result_gun_list = find_gun_buy_value(text, gun_list)
    return result_gun_list


def find_gun_buy_value(text, gun_list):
    """ it search for text in gun properties"""
    result_list = []
    for gun in gun_list:
        gun_as_dict = gun.__dict__
        for key in gun_as_dict:
            if str(gun_as_dict[key]).lower() == text:
                result_list.append(gun)
    return result_list


def find_gun_buy_not_full_value(text, gun_list):
    """ it search for not completed text in gun properties"""
    result_list = []
    for gun in gun_list:
        gun_as_dict = gun.__dict__
        for key in gun_as_dict:
            if str(gun_as_dict[key]).lower() in text:
                result_list.append(gun)
    return result_list


def find_value_with_equal_property(text, gun_list):
    result_list = []
    text_list = text.split()
    character_place = text_list.index('=')
    value = ''
    if character_place == 1:
        property_name = text_list[0]
    else:
        property_name = text_list[0] + "_" + text_list[1]
    if len(text_list) == character_place + 1:
        value = text_list[2]
    else:
        for word in text_list[character_place + 1: len(text_list)]:
            value += word
    exists = False
    for key in gun_list[0].__dict__:
        if str(key) == property_name:
            exists = True
    if exists:
        for gun in gun_list:
            gun_as_dict = gun.__dict__
            if gun_as_dict[property_name].lower() == value:
                result_list.append(gun)

    return result_list
