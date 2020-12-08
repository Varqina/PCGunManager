import PySimpleGUI as sg

import SetOfStringsClass


def run_gui(gun_list):
    sg.theme('DarkAmber')
    heading = ['index', 'number', 'factory', 'model']
    table_data = create_table_data(gun_list)
    layout = [[sg.Table(values=table_data, auto_size_columns=True, headings=heading)],
              [sg.Text(SetOfStringsClass.choice_gun), sg.Input('Index Number')],
              [sg.Button("Remove")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400))
    while True:
        event, values = window.read()
        if event == "Remove":
            break
        if event == sg.WIN_CLOSED or 'Exit':
            break
    window.close()
    picked_gun = table_data[int(values[1])]
    return picked_gun[1]


def create_table_data(gun_list):
    table_data = []
    index = 0
    for gun in gun_list:
        temporary_tab = [index, gun.get_number(), gun.get_factory(), gun.get_model()]
        table_data.append(temporary_tab)
        index += 1
    return table_data
