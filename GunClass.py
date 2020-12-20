class GunClass:
    factory = None
    model = None
    bullets_used_total = 0
    buy_date = None
    buy_price = 0
    brand_new = None
    last_cleaning = None
    gun_serial_number = None

    shooting = {}  # key - int, value = [date of training/shooting, place, ammo used]

    def __init__(self, factory, model, gun_number):
        self.factory = factory
        self.model = model
        self.gun_serial_number = gun_number

    def __eq__(self, other):
        return self.factory == other.factory and self.model == other.model and \
               self.gun_serial_number == other.gun_serial_number

    def add_shooting(self, shooting_date, shooting_place, bullets_amount):
        self.shooting[self.get_latest_used_key() + 1] = (shooting_date, shooting_place, bullets_amount)
        self.bullets_used_total += bullets_amount

    def remove_shooting(self, shooting_index):
        self.bullets_used_total -= self.shooting.get(shooting_index).__getitem__(1)
        del self.shooting[shooting_index]

    def print_shooting_date(self):
        for k, v in self.shooting:
            print(k)

    def get_printed_gun_property_list(self):
        print("Factory: " + self.get_factory())
        print("Model: " + self.get_model())
        print("Bullets used: " + str(self.get_bullets_used_total()))
        print("Buy Date: " + str(self.get_buy_date()))
        print("Buy price: " + str(self.get_buy_price()))
        print("Brand new: " + str(self.get_brand_new()))
        print("Date last cleaning: " + str(self.get_last_cleaning()))
        print("Gun's number: " + self.get_number())

    def get_latest_used_key(self):
        latest_key = 0
        if len(self.shooting) == 0:
            return latest_key
        for k, v in self.shooting:
            if k > latest_key:
                latest_key = k
        return latest_key

    def __str__(self):
        return "Gun: %s, %s, %s " % (self.factory, self.model, self.gun_serial_number)

    def get_shooting(self):
        return self.shooting

    def get_factory(self):
        return self.factory

    def get_model(self):
        return self.model

    def get_bullets_used_total(self):
        return self.bullets_used_total

    def get_buy_date(self):
        return self.buy_date

    def get_buy_price(self):
        return self.buy_price

    def get_brand_new(self):
        return self.brand_new

    def get_last_cleaning(self):
        return self.last_cleaning

    def get_number(self):
        return self.gun_serial_number

    def set_factory(self, factory):
        self.factory = factory

    def set_model(self, model):
        self.factory = model

    def set_bullets_used_total(self, bullets_used_total):
        self.bullets_used_total = bullets_used_total

    def set_buy_date(self, buy_date):
        self.buy_date = buy_date

    def set_buy_price(self, buy_price):
        self.buy_price = buy_price

    def set_brand_new(self, brand_new):
        self.brand_new = brand_new

    def set_last_cleaning(self, last_cleaning):
        self.last_cleaning = last_cleaning

    def set_gun_number(self, gun_number):
        self.gun_serial_number = gun_number
