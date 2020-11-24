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
        if property_name == "Gun's number": picked_gun.set_gun_number(new_property_value)
        print(SetOfStringsClass.value_updated)
        picked_gun.get_printed_gun_property_list()

    def display_all_with_details(self):
        index = 1
        for gun in self.gun_list:
            print(str(index) + ": " + str(gun))
            gun.get_printed_gun_property_list()
            index += 1

    def display_all(self):
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
        shooting_length = len(picked_gun.get_shooting())
        if shooting_length == 0: return SetOfStringsClass.no_shooting_available
        shooting_to_edit = 1
        if len(picked_gun.get_shooting()) > 1:
            picked_gun.print_shooting_date()
            shooting_to_edit = input(SetOfStringsClass.choice_shooting)
        shooting_properties = picked_gun.get_shooting[shooting_to_edit]
        #TODO: GET enum to access tab elements by name not index number



    def remove_shooting(self):
        pass

    def user_pick_gun_from_list(self):
        self.display_all()
        gun_index = int(input(SetOfStringsClass.choice_gun + " to edit")) - 1
        return self.gun_list[gun_index]