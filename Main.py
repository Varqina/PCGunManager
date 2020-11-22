#Load Data
#Load Menu

import MenuClass
from GunClass import GunClass
from GunManagerClass import GunManagerClass

GunManager = GunManagerClass()
while True:
    print(MenuClass.main_menu_loop)
    choice = int(input(MenuClass.choice_request))

    if (choice == 1):

        pass #display all
    if (choice == 2):
        gun_factory = input(MenuClass.provide_factory)
        gun_model = input(MenuClass.provide_model)
        GunManager.add_gun(GunClass(gun_factory, gun_model))


    if (choice == 3):
        pass #edit gun
    if (choice == 4):
        pass #remove gun
    if (choice == 5):
        GunManager.display_all()
        pass #display all
    if (choice == 6):
        break

#Save Data
