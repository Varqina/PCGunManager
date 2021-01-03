import PySimpleGUI as sg

import SetOfStringsClass
from GUI import GuiMessageTextDialog


# TODO search
# TODO Resize and aligment
# TODO columChosser

def run_gui(gun_list):
    sg.theme('DarkAmber')
    table_heading = ['index', 'factory', 'model', 'serial number']
    table_data = create_table_data(gun_list)
    window = create_window(table_data, heading=table_heading)
    picked_gun_serial_number = ""

    while True:
        event, values = window.read()
        if event == "Search":
            search_value = values[0]
            run_search(search_value)
        if event == "Edit":
            table_of_lists = values[1]
            if len(table_of_lists) > 0:
                index_of_selected_list = table_of_lists[0]
                picked_index_as_int = int(index_of_selected_list)
                picked_gun = table_data[picked_index_as_int]
                picked_gun_serial_number = picked_gun[3]
                break
            else:
                GuiMessageTextDialog.run_gui("You need to pick expected gun")
        if event == sg.WIN_CLOSED or event == "Back":
            picked_gun_serial_number = None
            break
        if len(table_data) == 0:
            GuiMessageTextDialog.run_gui("There are no guns")
            break

    window.close()
    return picked_gun_serial_number


def refresh_table_data(table_data):
    index = 1
    for row in table_data:
        row[0] = index
        index += 1
    return table_data


def create_table_data(gun_list):
    table_data = []
    index = 1
    for gun in gun_list:
        temporary_tab = [index, gun.get_factory(), gun.get_model(), gun.get_gun_serial_number()]
        table_data.append(temporary_tab)
        index += 1
    return table_data


def is_user_value_correct(user_value):
    try:
        int(user_value)
    except (TypeError, ValueError):
        return False
    return True


def create_window(table_data, heading, first_invoke=True):
    return refresh_window(table_data, heading, first_invoke=first_invoke)


def refresh_window(table_data, heading, window=None, first_invoke=False):
    if not first_invoke:
        window.close()
    layout = [[sg.Input("Write gun here"), sg.Button("Search")],
              [sg.Table(values=table_data, auto_size_columns=True, headings=heading), sg.Button('Edit')],
              [sg.Button("Back")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), element_justification='right')
    return window


def run_search(text):
    pass
