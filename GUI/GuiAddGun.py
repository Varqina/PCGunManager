import PySimpleGUI as sg

import SetOfStringsClass


# TODO Add Photo
# TODO Validate values
# TODO nie dziala gdy 2 sa uniq i jedno w bazie juz jest
# TODO pusty string dziala
# TODO moge dodac bron z tym samym numerem
def run_gui(added_comment=False, already_in_database=False, gun=None):
    sg.theme('DarkAmber')
    '''Variable initialization'''
    add_gun_output = ' '
    color = 'green'
    gun_factor = 'Gun Factory'
    gun_model = 'Gun Model'
    gun_serial_number = 'Gun Serial Number'

    '''Update variable according to parameters'''
    if added_comment:
        add_gun_output = "The gun has been added!"
    if already_in_database:
        add_gun_output = "This gun is already in database"
        color = 'red'
        gun_factor = gun.get_factory()
        gun_model = gun.get_model()
        gun_serial_number = gun.get_gun_serial_number()
    layout = [[sg.Text(SetOfStringsClass.provide_factory), sg.Input(gun_factor)],
              [sg.Text(SetOfStringsClass.provide_model), sg.Input(gun_model)],
              [sg.Text(SetOfStringsClass.provide_gun_number), sg.Input(gun_serial_number)],
              [sg.Button("Add"), sg.Button("Exit")],
              [sg.Text(add_gun_output, text_color=color)]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400))
    while True:
        event, values = window.read()
        if event == "Add":
            break
        if event == sg.WIN_CLOSED or 'Exit':
            values = None
            break
    window.close()
    return values