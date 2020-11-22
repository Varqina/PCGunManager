from GunClass import GunClass
import SetOfStringsClass


class GunManagerClass:
    gun_list = []

    def add_gun(self,):
        gun_to_be_added = GunClass(input(SetOfStringsClass.provide_factory), input(SetOfStringsClass.provide_model),
                                   input(SetOfStringsClass.provide_gun_number))
        self.gun_list.append(gun_to_be_added)

    def remove_gun(self):
        gun_to_be_removed = input(SetOfStringsClass.provide_gun_number)
        for gun in self.gun_list:
            if gun.get_gun_number() == gun_to_be_removed:
                self.gun_list.remove(gun)
                break

    def edit_gun(self):
        self.display_all()
        gun_index = int(input(SetOfStringsClass.choice_gun + " to edit")) -1
        edited_gun = self.gun_list[gun_index]
        edited_gun.get_printed_gun_property_list()
        property_name = input(SetOfStringsClass.select_gun_property).lower()
        new_property_value = input(SetOfStringsClass.provide_new_value)
        if property_name == "factory": edited_gun.set_factory(new_property_value)
        if property_name == "model": edited_gun.set_model(new_property_value)
        if property_name == "bullets used": edited_gun.set_bullets_used_total(new_property_value)
        if property_name == "buy date": edited_gun.set_buy_date(new_property_value)
        if property_name == "buy price": edited_gun.set_buy_price(new_property_value)
        if property_name == "brand new": edited_gun.set_brand_new(new_property_value)
        if property_name == "date last cleaning": edited_gun.set_last_cleaning(new_property_value)
        if property_name == "Gun's number": edited_gun.set_gun_number(new_property_value)
        print(SetOfStringsClass.value_updated)
        edited_gun.get_printed_gun_property_list()

    def display_all(self):
        detailed_view = input(SetOfStringsClass.detailed_view)
        index = 1
        for gun in self.gun_list:
            print(str(index) + ": " + str(gun))
            if detailed_view == "yes" or detailed_view == "y":
                gun.get_printed_gun_property_list()
            index += 1

    def add_shooting(self):
        #2add remove shooting
        index = 1
        for gun in self.gun_list:
            print(str(index) + ": " + str(gun))
            index += 1
        gun_index = int(input(SetOfStringsClass.used_gun)) - 1
        shooting_date = input(SetOfStringsClass.add_date)
        shooting_place = input(SetOfStringsClass.add_shooting_place)
        bullets_used = input(SetOfStringsClass.add_used_bullets)
        self.gun_list[gun_index].add_shooting(shooting_date, shooting_place, bullets_used)