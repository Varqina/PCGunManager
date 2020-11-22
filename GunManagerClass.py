class GunManagerClass:
    gun_list = []

    def add_gun(self, gun):
        self.gun_list.append(gun)
        pass
    def remove_gun(self):
        pass
    def edit_gun(self):
        pass
    def display_all(self):
        index = 1
        for gun in self.gun_list:
            print(str(index) + ": " + str(gun))
            index += 1
