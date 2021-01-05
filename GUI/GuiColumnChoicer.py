import PySimpleGUI as sg

import SetOfStringsClass


def run_gui(columnChoicerManager):
    sg.theme('DarkAmber')
    layout = [[sg.Checkbox('Factory', default=columnChoicerManager.get_factory_checkbox_status(), key='factory')],
              [sg.Checkbox('Model', default=columnChoicerManager.get_model_checkbox_status(), key='model')],
              [sg.Checkbox('Serial number', default=columnChoicerManager.get_gun_serial_number_checkbox_status(),
                           key='gun_serial_number')],
              [sg.Checkbox('Used bullets', default=columnChoicerManager.get_bullets_used_total_checkbox_status(),
                           key='bullets_used_total')],
              [sg.Checkbox('Buy date', default=columnChoicerManager.get_buy_date_checkbox_status(), key='buy_date')],
              [sg.Checkbox('Buy price', default=columnChoicerManager.get_buy_price_checkbox_status(), key='buy_price')],
              [sg.Checkbox('First owner', default=columnChoicerManager.get_brand_new_checkbox_status(),
                           key='brand_new')],
              [sg.Checkbox('Date of last cleaning', default=columnChoicerManager.get_last_cleaning_checkbox_status(),
                           key='last_cleaning')],
              [sg.Button("OK")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, disable_minimize=True)
    while True:
        event, values = window.read()
        # {'factory': True, 'model': False, 'gun_serial_number': False}
        if event == "OK":
            columnChoicerManager.set_properties_data(values)
            break
        if event == sg.WIN_CLOSED or 'Exit':
            #it needs to return object with default values
            values = columnChoicerManager.get_values_as_dictionary()
            break
    window.close()
    return values
