import PySimpleGUI as sg

import SetOfStringsClass


def run_gui(gun_list):
    sg.theme('DarkAmber')
    heading = ['index', 'number', 'factory', 'model']
    layout = [[sg.Table(values=create_table_data(gun_list), auto_size_columns=True, headings=heading)],
              [sg.Text(SetOfStringsClass.choice_gun), sg.Input('Index Number')],
              [sg.Button("Remove")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400))
    while True:
        event, values = window.read()
        if event == "Remove":
            return values[0]
        if event == sg.WIN_CLOSED or 'Exit':
            break
    window.close()


def create_table_data(gun_list):
    table_data = []
    index = 0
    for gun in gun_list:
        temporary_tab = [index, gun.get_number(), gun.get_factory(), gun.get_model()]
        table_data.append(temporary_tab)
        index += 1
    return table_data
