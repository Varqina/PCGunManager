def run_search(text, gun_list):
    # datbase lista slownikow
    # robimy AND, OR, !=, = empty
    text = text.lower()
    return find_value(text, gun_list)


def find_value(text, gun_list):
    result_list = []
    for gun in gun_list:
        gun_as_dict = gun.__dict__
        for key in gun_as_dict:
            if str(gun_as_dict[key]).lower() == text:
                result_list.append(gun)
    return result_list
