import PySimpleGUI as sg

import SetOfStringsClass

# todo serializacja
# todo load application

def run_gui(gun_manager):
    sg.theme('DarkAmber')
    layout = [[sg.Text(SetOfStringsClass.add_gun_to_the_stock), sg.Button('Add')],
              [sg.Text(SetOfStringsClass.edit_gun), sg.Button('Edit')],
              [sg.Text(SetOfStringsClass.remove_gun), sg.Button('Remove')],
              [sg.Text(SetOfStringsClass.display_stock), sg.Button('Display')],
              [sg.Text(SetOfStringsClass.edit_shooting_activity), sg.Button('Edit')],
              [sg.Text(SetOfStringsClass.exit_application), sg.Button('Exit')]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400))
    while True:
        event, values = window.read()
        if event == 'Add':
            gun_manager.add_gun()
        if event == 'Edit':
            gun_manager.edit_gun()
        if event == 'Remove':
            gun_manager.remove_gun()
        if event == 'Display':
            gun_manager.display_all()
        if event == 'Edit0':
            gun_manager.edit_shooting()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()



