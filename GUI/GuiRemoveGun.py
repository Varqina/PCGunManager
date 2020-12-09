import PySimpleGUI as sg

import SetOfStringsClass
from GUI import GuiMessageTextDialog

#TODO online update
#TODO search
#TODO buttons to right

def run_gui(gun_list):
    sg.theme('DarkAmber')
    heading = ['index', 'number', 'factory', 'model']
    table_data = create_table_data(gun_list)
    layout = [[sg.Table(values=table_data, auto_size_columns=True, headings=heading), sg.Button('Delete')],
              [sg.Text(SetOfStringsClass.choice_gun), sg.Input('0', size=(3,1)), sg.Button("Remove")],
              [sg.Button("Back")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0))
    while True:
        event, values = window.read()
        if event == "Remove":
            if is_user_value_correct(values[1]) and int(values[1]) < len(table_data):
                picked_index = int(values[1])
                picked_gun = table_data[picked_index]
                picked_gun_number = picked_gun[1]
                break
            else:
                GuiMessageTextDialog.run_gui("Provided value: " + values[1] + " is incorrect")
        if event == "Delete":
            if len(values[0]) > 0:
                picked_index = int(values[0][0])
                picked_gun = table_data[picked_index]
                picked_gun_number = picked_gun[1]
                break
            else:
                GuiMessageTextDialog.run_gui("You need to pick expected row")
        if event == sg.WIN_CLOSED or event == "Back":
            picked_gun_number = None
            break
    window.close()
    return picked_gun_number


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
