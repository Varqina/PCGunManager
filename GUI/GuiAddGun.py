import PySimpleGUI as sg

import SetOfStringsClass



# TODO Add Photo
# TODO Validate values
# TODO nie dziala gdy 2 sa uniq i jedno w bazie juz jest
# TODO pusty string dziala
# TODO moge dodac bron z tym samym numerem
def run_gui(added_comment=False, already_in_database_comment=False, gun=None):
    sg.theme('DarkAmber')
    gun_factor = 'Gun Factory'
    gun_model = 'Gun Model'
    gun_serial_number = 'Gun Serial Number'
    layout = [[sg.Text(SetOfStringsClass.provide_factory), sg.Input(gun_factor)],
              [sg.Text(SetOfStringsClass.provide_model), sg.Input(gun_model)],
              [sg.Text(SetOfStringsClass.provide_gun_number), sg.Input(gun_serial_number)],
              [sg.Button("Add")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400))
    if added_comment:
        window.add_row(sg.Text("The gun has been added!", text_color='green'))
    if already_in_database_comment:
        window.add_row(sg.Text("This gun is already in database", text_color='red'))
    while True:
        event, values = window.read()
        if event == "Add":
            break
        if event == sg.WIN_CLOSED or 'Exit':
            values = None
            break
    window.close()
    return values
