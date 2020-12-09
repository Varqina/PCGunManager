import PySimpleGUI as sg

import SetOfStringsClass


def run_gui(message_text):
    sg.theme('DarkAmber')
    layout = [[sg.Text(message_text)],
              [sg.Button("OK")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, disable_minimize=True, disable_close=True)
    while True:
        event, values = window.read()
        if event == "Add":
            break
        if event == sg.WIN_CLOSED or 'Exit':
            break
    window.close()
