import PySimpleGUI as sg

import SetOfStringsClass
from GUI import GuiMessageTextDialog


# TODO search
# TODO Resize and aligment




def run_gui(gun_list):
    sg.theme('DarkAmber')
    heading = ['index', 'number', 'factory', 'model']
    table_data = create_table_data(gun_list)
    window = get_window(table_data, heading, first_invoke=True)
    numbers_of_picked_guns = []

    while True:
        event, values = window.read()
        if event == "Search":
            run_search(values[0])
        if event == "Remove":
            #1->2
            if is_user_value_correct(values[1]) and int(values[1]) < len(table_data):
                picked_index = int(values[1])
                picked_gun = table_data[picked_index]
                numbers_of_picked_guns.append(picked_gun[1])
                table_data.remove(picked_gun)
                window = get_window(table_data, heading, window)
            else:
                GuiMessageTextDialog.run_gui("Provided value: " + values[1] + " is incorrect")
        if event == "Delete":
            #[0] -> [1]
            #[0][0] -> [1][0]
            #[1] -> [2]
            if len(values[0]) > 0:
                picked_index = int(values[0][0])
                picked_gun = table_data[picked_index]
                numbers_of_picked_guns.append(picked_gun[1])
                table_data.remove(picked_gun)
                window = get_window(table_data, heading, window)
            else:
                GuiMessageTextDialog.run_gui("You need to pick expected row")
        if event == sg.WIN_CLOSED or event == "Back":
            break
        if len(table_data) == 0:
            GuiMessageTextDialog.run_gui("There are no more guns")
            break
    window.close()
    return numbers_of_picked_guns


def create_table_data(gun_list):
    table_data = []
    index = 0
    for gun in gun_list:
        temporary_tab = [index, gun.get_number(), gun.get_factory(), gun.get_model()]
        table_data.append(temporary_tab)
        index += 1
    return table_data


def is_user_value_correct(user_value):
    try:
        int(user_value)
    except (TypeError, ValueError):
        return False
    return True


def get_window(table_data, heading, window=None, first_invoke=False):
    if not first_invoke:
        window.close()
    layout = [[sg.Input("Write gun here"), sg.Button("Search")],
              [sg.Table(values=table_data, auto_size_columns=True, headings=heading), sg.Button('Delete')],
              [sg.Text(SetOfStringsClass.choice_gun), sg.Input('0', size=(3, 1))],
              [sg.Button("Remove"), sg.Button("Back")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), element_justification='right')
    return window


def run_search():
    pass