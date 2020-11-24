#Load Data
#Load Menu

import SetOfStringsClass
from GunManagerClass import GunManagerClass

GunManager = GunManagerClass()
while True:
    print(SetOfStringsClass.main_menu_loop)
    choice = int(input(SetOfStringsClass.choice_request))
    if choice == 1:
        GunManager.add_gun()
    if choice == 2:
        GunManager.edit_gun()
    if choice == 3:
        GunManager.remove_gun()
    if choice == 4:
        GunManager.display_all()
    if choice == 5:
        print(SetOfStringsClass.shooting_menu)
        choice = int(input(SetOfStringsClass.choice_request))
        if choice == 1:
            GunManager.add_shooting()
        if choice == 2:
            GunManager.edit_shooting()
        if choice == 3:
            GunManager.remove_shooting()
        else:
            pass
    if choice == 6:
        break

#Save Data
