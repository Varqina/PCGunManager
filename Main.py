#Load Data
#Load Menu

import SetOfStringsClass
from GunManagerClass import GunManagerClass

GunManager = GunManagerClass()
while True:
    print(SetOfStringsClass.main_menu_loop)
    choice = int(input(SetOfStringsClass.choice_request))
    if choice == 1: #add
        GunManager.add_gun()
    if choice == 2: #edit
        GunManager.edit_gun()
    if choice == 3: #remove
        GunManager.remove_gun()
    if choice == 4: #Display
        GunManager.display_all()
    if choice == 5:
        GunManager.add_shooting()
    if choice == 6:
        break

#Save Data
