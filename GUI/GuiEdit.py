import PySimpleGUI as sg
import SetOfStringsClass
from GUI import GuiMessageTextDialog, GuiColumnChoicer

# TODO search
# TODO Resize and aligment
# TODO columChosser
# TODO edit on empty makes error
from GunClass import GunClass
from Search import run_search


def change_dictionary_list_into_gun_list(gun_list_as_dictionary_list):
    # Todo przeniesc do glownego programu nie w gui
    gun_list = []
    print(gun_list_as_dictionary_list[0])
    for element in gun_list_as_dictionary_list:
        # tutaj przychodzi caly czas pierdolony slownik
        #print(element.get_bullets_used()) AttributeError: 'dict' object has no attribute 'get_bullets_used'
        gun = GunClass(element['factory'], element['model'], element['gun_serial_number'])
        gun.update_properties(element)
        gun_list.append(gun)
    return gun_list


def run_gui(gun_list, column_choicer_edit):
    sg.theme('DarkAmber')
    table_heading = column_choicer_edit.get_table_heading()
    table_data = create_table_data(gun_list, column_choicer_edit)
    window = create_window(table_data, heading=table_heading)
    # list guid respond has two values [0] - Refresh, [1] - data to be displayed
    # But it can have gun which has been chosen
    # as [0] parameter there is None to close window
    # as [2] parameter there is a gun to be edited
    gui_respond = [False, 'gun_list']

    while True:
        print(table_heading)
        event, values = window.read()

        if event == "Search":
            search_value = values[0]
            search_gun_list = run_search(search_value, gun_list)
            #search_gun_list = change_dictionary_list_into_gun_list(gun_list_as_dictionary_list)
            gui_respond[0] = True
            gui_respond[1] = search_gun_list
            break
        if event == "Edit":
            table_of_lists = values[1]
            if len(table_of_lists) > 0:
                index_of_selected_list = table_of_lists[0]
                picked_index_as_int = int(index_of_selected_list)
                picked_gun = table_data[picked_index_as_int]
                gui_respond.append(picked_gun[3])
                break
            else:
                GuiMessageTextDialog.run_gui("You need to pick expected gun")
        if event == "Column Choicer":
            column_property_choicer_as_dictionary = GuiColumnChoicer.run_gui(column_choicer_edit)
            column_choicer_edit.set_properties_data(column_property_choicer_as_dictionary)
            # it will use refresh to refresh window and get updated table
            gui_respond[0] = 'refresh'
            break
        if event == sg.WIN_CLOSED or event == "Back":
            gui_respond[0] = None
            break
        if len(table_data) == 0:
            GuiMessageTextDialog.run_gui("There are no guns")
            break

    window.close()
    return gui_respond


def refresh_table_data(table_data):
    index = 1
    for row in table_data:
        row[0] = index
        index += 1
    return table_data


def create_table_data(gun_list, column_choicer):
    table_data = []
    index = 1
    for gun in gun_list:
        if column_choicer is None:
            temporary_tab = [index, gun.get_factory(), gun.get_model(), gun.get_gun_serial_number()]
        else:
            temporary_tab = column_choicer.get_row_with_selected_properties(index, gun)
        table_data.append(temporary_tab)
        index += 1
    return table_data


def is_user_value_correct(user_value):
    try:
        int(user_value)
    except (TypeError, ValueError):
        return False
    return True


def create_window(table_data, heading, first_invoke=True):
    return refresh_window(table_data, heading, first_invoke=first_invoke)


def refresh_window(table_data, heading, window=None, first_invoke=False):
    if not first_invoke:
        window.close()
    layout = [[sg.Input("Write gun here"), sg.Button("Search")],
              [sg.Button("Column Choicer")],
              [sg.Table(values=table_data, auto_size_columns=True, headings=heading), sg.Button('Edit')],
              [sg.Button("Back")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), element_justification='right')
    return window
