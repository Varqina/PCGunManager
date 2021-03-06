import Settings
import SetOfStringsClass
from GUI import GuiMain
from GunManagerClass import GunManagerClass
from SaveAndLoad import save_application_data, load_application_data
gun_manager = GunManagerClass()

# TODO object to handle it
gun_manager.set_gun_list(load_application_data(SetOfStringsClass.database_gun_list_file))
gun_manager.columnChoicerRemove.set_properties_data(load_application_data(SetOfStringsClass.database_choicer_remove_file))
gun_manager.columnChoicerEdit.set_properties_data(load_application_data(SetOfStringsClass.database_choicer_edit_file))

if Settings.gui:
    GuiMain.run_gui(gun_manager)
else:
    while True:
        print(SetOfStringsClass.main_menu_loop)
        choice = int(input(SetOfStringsClass.choice_request))
        if choice == 1:
            gun_manager.add_gun()
        if choice == 2:
            gun_manager.edit_gun()
        if choice == 3:
            gun_manager.remove_gun()
        if choice == 4:
            gun_manager.display_all()
        if choice == 5:
            print(SetOfStringsClass.shooting_menu)
            choice = int(input(SetOfStringsClass.choice_request))
            if choice == 1:
                gun_manager.add_shooting()
            if choice == 2:
                gun_manager.edit_shooting()
            if choice == 3:
                gun_manager.remove_shooting()
            else:
                pass
        if choice == 6:
            break

# TODO object to handle it
save_application_data(gun_manager.get_gun_list(), SetOfStringsClass.database_gun_list_file, backup=True)
save_application_data(gun_manager.columnChoicerRemove.get_values_as_dictionary(), SetOfStringsClass.database_choicer_remove_file)
save_application_data(gun_manager.columnChoicerEdit.get_values_as_dictionary(), SetOfStringsClass.database_choicer_edit_file)
#Save Data