import PySimpleGUI as sg

import SetOfStringsClass
from GUI import GuiMessageTextDialog

'''Variable initialization'''
add_gun_output = ' '
color = 'green'
gun_factor = 'Gun Factory'
gun_model = 'Gun Model'
gun_serial_number = 'Gun Serial Number'


# TODO Extend Properties button

def run_gui(added_comment=False, already_in_database=False, gun=None):
    global gun_factor, gun_model, gun_serial_number, color, add_gun_output

    sg.theme('DarkAmber')

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
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400),
                       element_justification='right')
    while True:
        event, values = window.read()
        if event == "Add":
            if verify_value(values):
                break
        if event == sg.WIN_CLOSED or event == 'Exit':
            values = None
            break
    window.close()
    # [0] - Gun Factory, [1] - Gun Model, [2] - Gun Serial Number
    return values


def value_is_incorrect(input_value):
    error_value = ErrorValue()
    forbidden_characters_tuple = " "
    if len(input_value) == 0:
        error_value.set_error_list("empty value")
        return error_value
    for character in forbidden_characters_tuple:
        if character in input_value:
            if character == " ":
                character = "space"
            error_value.set_error_list(character)
    return error_value


def verify_value(values):
    issue_exists = 0
    tested_value = value_is_incorrect(values[0])
    if tested_value.get_error_status():
        GuiMessageTextDialog.run_gui("Value '%s' is incorrect. Please don't use %s in %s"
                                     % (values[0], tested_value.get_error_list_as_string(), gun_factor))
        issue_exists = 1
    tested_value = value_is_incorrect(values[1])
    if tested_value.get_error_status():
        GuiMessageTextDialog.run_gui("Value '%s' is incorrect. Please don't use %s in %s"
                                     % (values[1], tested_value.get_error_list_as_string(), gun_model))
        issue_exists = 1
    tested_value = value_is_incorrect(values[2])
    if tested_value.get_error_status():
        GuiMessageTextDialog.run_gui("Value '%s' is incorrect. Please don't use %s in %s"
                                     % (values[2], tested_value.get_error_list_as_string(), gun_serial_number))
        issue_exists = 1
    return True if issue_exists == 0 else False


class ErrorValue:
    def __init__(self):
        self.error_list = []
        self.error_status = False

    def get_error_list(self):
        return self.error_list

    def get_error_status(self):
        if len(self.error_list) != 0:
            self.error_status = True
        return self.error_status

    def set_error_list(self, error_character):
        self.error_list.append(error_character)

    def get_error_list_as_string(self):
        output_string = ""
        for element in self.get_error_list():
            output_string += element
            output_string += ', '
        return output_string[0:len(output_string) - 2]
