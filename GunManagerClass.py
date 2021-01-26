import Settings
from ColumnChoicerManagerClass import ColumnChoicerManagerClass
from GUI import GuiAddGun, GuiRemoveGun, GuiMessageTextDialog, GuiEdit, GuiEditProperties
from GunClass import GunClass
import SetOfStringsClass


# TODO ENUM to gun form

class GunManagerClass:
    gun_list = []
    columnChoicerEdit = ColumnChoicerManagerClass()
    columnChoicerRemove = ColumnChoicerManagerClass()

    def __eq__(self, other):
        return self.gun_list == other.gun_list

    def add_gun(self, gun_form=None, first_run=True):
        if Settings.gui:
            if gun_form is not None:
                gun_to_be_added = GunClass(gun_form[0], gun_form[1], gun_form[2])
                self.add_gun_and_refresh_gui(gun_to_be_added)
            else:
                if first_run:
                    gun_form = GuiAddGun.run_gui()
                if gun_form is None:
                    return None
                gun_to_be_added = GunClass(gun_form[0], gun_form[1], gun_form[2])
                self.add_gun_and_refresh_gui(gun_to_be_added)
        else:
            gun_to_be_added = GunClass(input(SetOfStringsClass.provide_factory), input(SetOfStringsClass.provide_model),
                                       input(SetOfStringsClass.provide_gun_number))
            if not self.check_if_gun_exists_in_database(gun_to_be_added):
                self.gun_list.append(gun_to_be_added)

    def add_gun_and_refresh_gui(self, gun_to_be_added):
        if not self.check_if_gun_exists_in_database(gun_to_be_added):
            self.gun_list.append(gun_to_be_added)
            self.add_gun(GuiAddGun.run_gui(added_comment=True), first_run=False)
        else:
            self.add_gun(GuiAddGun.run_gui(already_in_database=True, gun=gun_to_be_added), first_run=False)

    def check_if_gun_exists_in_database(self, gun_to_be_added):
        for gun in self.gun_list:
            if gun.get_gun_serial_number() == gun_to_be_added.get_gun_serial_number():
                return True
        return False

    def remove_gun(self):
        # TODO dziedziczenie po sobie
        if len(self.gun_list) != 0:
            if Settings.gui:
                guns_to_be_removed = GuiRemoveGun.run_gui(self.gun_list, column_choicer_remove=self.columnChoicerRemove)
                while guns_to_be_removed == 'refresh':
                    guns_to_be_removed = GuiRemoveGun.run_gui(self.gun_list,
                                                              column_choicer_remove=self.columnChoicerRemove)
            else:
                guns_to_be_removed = input(SetOfStringsClass.provide_gun_number)
            if guns_to_be_removed is not None:
                for gun in self.gun_list:
                    for gun_number_to_be_removed in guns_to_be_removed:
                        if gun.get_gun_serial_number() == gun_number_to_be_removed:
                            self.gun_list.remove(gun)
                            break
        else:
            GuiMessageTextDialog.run_gui("There is no gun in the stock")

    def run_gui_update_properties(self, gun):
        new_properties = GuiEditProperties.run_gui(gun=gun)
        if new_properties is not None:
            if gun.update_properties(new_properties):
                GuiMessageTextDialog.run_gui(SetOfStringsClass.value_updated)
            else:
                GuiMessageTextDialog.run_gui("No changes detected")
            self.run_gui_update_properties(gun)

    def run_update_properties(self):
        pass

    def edit_gun(self):
        # TODO export to Json
        if Settings.gui:
            gui_respond = GuiEdit.run_gui(self.gun_list, column_choicer_edit=self.columnChoicerEdit)
            # be ready to for each colum choiser invoke
            while gui_respond[0]:
                if gui_respond[1] != 'gun_list':
                    gun_list = gui_respond[1]
                else:
                    gun_list = self.gun_list
                gui_respond = GuiEdit.run_gui(gun_list, column_choicer_edit=self.columnChoicerEdit)
            # to avoid inedx our of range
            if len(gui_respond) > 2:
                gun = self.get_gun_by_serial_number(gui_respond[2])
            else:
                gun = None
            if gun is not None:
                self.run_gui_update_properties(gun)
                self.edit_gun()
        else:
            picked_gun = self.user_pick_gun_from_list()
            picked_gun.get_printed_gun_property_list()
            property_name = input(SetOfStringsClass.select_gun_property).lower()
            new_property_value = input(SetOfStringsClass.provide_new_value)
            if property_name == "factory": picked_gun.set_factory(new_property_value)
            if property_name == "model": picked_gun.set_model(new_property_value)
            if property_name == "bullets used": picked_gun.set_bullets_used_total(new_property_value)
            if property_name == "buy date": picked_gun.set_buy_date(new_property_value)
            if property_name == "buy price": picked_gun.set_buy_price(new_property_value)
            if property_name == "brand new": picked_gun.set_brand_new(new_property_value)
            if property_name == "date last cleaning": picked_gun.set_last_cleaning(new_property_value)
            if property_name == "Gun's number": picked_gun.set_gun_serial_number(new_property_value)
            print(SetOfStringsClass.value_updated)
            picked_gun.get_printed_gun_property_list()

    def get_gun_by_serial_number(self, picked_gun_serial_number):
        for gun in self.gun_list:
            if gun.get_gun_serial_number() == picked_gun_serial_number:
                return gun
        else:
            return None

    def display_all_with_details(self):
        index = 1
        for gun in self.gun_list:
            print(str(index) + ": " + str(gun))
            gun.get_printed_gun_property_list()
            index += 1

    def display_all(self):
        if Settings.gui:
            GuiEdit.run_gui(self.gun_list)
        else:
            index = 1
            for gun in self.gun_list:
                print(str(index) + ": " + str(gun))
                index += 1

    def add_shooting(self):
        index = 1
        for gun in self.gun_list:
            print(str(index) + ": " + str(gun))
            index += 1
        gun_index = int(input(SetOfStringsClass.used_gun)) - 1
        shooting_date = input(SetOfStringsClass.add_date)
        shooting_place = input(SetOfStringsClass.add_shooting_place)
        bullets_used = input(SetOfStringsClass.add_used_bullets)
        self.gun_list[gun_index].add_shooting(shooting_date, shooting_place, bullets_used)

    def edit_shooting(self):
        picked_gun = self.user_pick_gun_from_list()
        shooting_amount = len(picked_gun.get_shooting())
        if shooting_amount == 0: return SetOfStringsClass.no_shooting_available
        shooting_to_edit = 1
        if len(picked_gun.get_shooting()) > 1:
            picked_gun.print_shooting_date()
            shooting_to_edit = input(SetOfStringsClass.choice_shooting)
        shooting_properties = picked_gun.get_shooting[shooting_to_edit]
        # TODO: GET enum to access tab elements by name not index number

    def remove_shooting(self):
        picked_gun = self.user_pick_gun_from_list()

        pass

    def user_pick_gun_from_list(self):
        self.display_all()
        gun_index = int(input(SetOfStringsClass.choice_gun + " to edit")) - 1
        return self.gun_list[gun_index]

    def get_gun_list(self):
        return self.gun_list

    def set_gun_list(self, gun_list):
        self.gun_list = gun_list
