class GunClass:
    factory = None
    model = None
    bullets_used = 0
    buy_date = None
    buy_price = 0
    brand_new = None
    last_cleaning = None
    gun_serial_number = None

    shooting = {}  # key - int, value = [date of training/shooting, place, ammo used]

    def __init__(self, factory, model, gun_serial_number):
        super().__init__()
        self.factory = factory
        self.model = model
        self.gun_serial_number = gun_serial_number

    def __eq__(self, other):
        return self.factory == other.factory and self.model == other.model and \
               self.gun_serial_number == other.gun_serial_number

    def __str__(self):
        return "Gun: %s, %s, %s " % (self.factory, self.model, self.gun_serial_number)

    def asdict(self):
        return {'factory': self.factory, 'model': self.model, 'used_bullets': self.bullets_used,
                'buy_date': self.buy_date, 'buy_price': self.buy_price, 'brand_new': self.brand_new,
                'last_cleaning': self.last_cleaning, 'gun_serial_number': self.gun_serial_number}

    def add_shooting(self, shooting_date, shooting_place, bullets_amount):
        self.shooting[self.get_latest_used_key() + 1] = (shooting_date, shooting_place, bullets_amount)
        self.bullets_used += bullets_amount

    def remove_shooting(self, shooting_index):
        self.bullets_used -= self.shooting.get(shooting_index).__getitem__(1)
        del self.shooting[shooting_index]

    def print_shooting_date(self):
        for k, v in self.shooting:
            print(k)

    def get_printed_gun_property_list(self):
        print("Factory: " + self.get_factory())
        print("Model: " + self.get_model())
        print("Bullets used: " + str(self.get_bullets_used()))
        print("Buy Date: " + str(self.get_buy_date()))
        print("Buy price: " + str(self.get_buy_price()))
        print("Brand new: " + str(self.get_brand_new()))
        print("Date last cleaning: " + str(self.get_last_cleaning()))
        print("Gun's number: " + self.get_gun_serial_number())

    def get_latest_used_key(self):
        latest_key = 0
        if len(self.shooting) == 0:
            return latest_key
        for k, v in self.shooting:
            if k > latest_key:
                latest_key = k
        return latest_key

    def update_properties(self, property_dictionary):
        property_changed = 0
        if property_dictionary['factory'] != self.get_factory():
            self.set_factory(property_dictionary['factory'])
            property_changed = 1
        if property_dictionary['model'] != self.get_model():
            self.set_model(property_dictionary['model'])
            property_changed = 1
        if property_dictionary['bullets_used'] != self.get_bullets_used():
            self.set_bullets_used_total(property_dictionary['bullets_used'])
            property_changed = 1
        if property_dictionary['buy_date'] != self.get_buy_date():
            self.set_buy_date(property_dictionary['buy_date'])
            property_changed = 1
        if property_dictionary['buy_price'] != self.get_buy_price():
            self.set_buy_price(property_dictionary['buy_price'])
            property_changed = 1
        if property_dictionary['brand_new'] != self.get_brand_new():
            self.set_brand_new(property_dictionary['brand_new'])
            property_changed = 1
        if property_dictionary['cleaning_date'] != self.get_last_cleaning():
            self.set_last_cleaning(property_dictionary['cleaning_date'])
            property_changed = 1
        if property_dictionary['serial_number'] != self.get_gun_serial_number():
            self.set_gun_serial_number(property_dictionary['serial_number'])
            property_changed = 1
        return True if property_changed == 1 else False

    def get_shooting(self):
        return self.shooting

    def get_factory(self):
        return self.factory

    def get_model(self):
        return self.model

    def get_bullets_used(self):
        return self.bullets_used

    def get_buy_date(self):
        return self.buy_date

    def get_buy_price(self):
        return self.buy_price

    def get_brand_new(self):
        return self.brand_new

    def get_last_cleaning(self):
        return self.last_cleaning

    def get_gun_serial_number(self):
        return self.gun_serial_number

    def set_factory(self, factory):
        self.factory = factory

    def set_model(self, model):
        self.factory = model

    def set_bullets_used_total(self, bullets_used_total):
        self.bullets_used = bullets_used_total

    def set_buy_date(self, buy_date):
        self.buy_date = buy_date

    def set_buy_price(self, buy_price):
        self.buy_price = buy_price

    def set_brand_new(self, brand_new):
        self.brand_new = brand_new

    def set_last_cleaning(self, last_cleaning):
        self.last_cleaning = last_cleaning

    def set_gun_serial_number(self, gun_number):
        self.gun_serial_number = gun_number
