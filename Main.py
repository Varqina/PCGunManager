#Load Data
#Load Menu
import PySimpleGUI as sg

import GlobalVariables
import SetOfStringsClass
from GUI import GuiMain
from GunManagerClass import GunManagerClass

gun_manager = GunManagerClass()

if GlobalVariables.gui:
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

#Save Data
