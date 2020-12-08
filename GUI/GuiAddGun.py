import PySimpleGUI as sg

import SetOfStringsClass


def run_gui():
    sg.theme('DarkAmber')
    layout = [[sg.Text(SetOfStringsClass.provide_factory), sg.Input('Gun Factory')],
              [sg.Text(SetOfStringsClass.provide_model), sg.Input('Gun Model')],
              [sg.Text(SetOfStringsClass.provide_gun_number), sg.Input('Gun Number')],
              [sg.Button("Add")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400))
    while True:
        event, values = window.read()
        if event == "Add":
            break
        if event == sg.WIN_CLOSED or 'Exit':
            break
    window.close()
    if values[0] is not None or values[1] is not None or values[2] is not None:
        return values

