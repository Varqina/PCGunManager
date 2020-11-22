class GunClass:
    def __init__(self, factory, model):
        self.factory = factory
        self.model = model

    factory = None
    model = None
    bullets_used_total = 0
    buy_date = None
    buy_price = None
    brand_new = None
    last_cleaning = None

    shooting = {}  # key - date of training/shooting, value = place, ammo used

    def add_shooting(self, shooting_date, shooting_place, bullets_amount):
        self.shooting[shooting_date] = (shooting_place, bullets_amount)
        self.bullets_used_total += bullets_amount

    def remove_shooting(self, shooting_date):
        self.bullets_used_total -= self.shooting.get(shooting_date).__getitem__(1)
        del self.shooting[shooting_date]

    def __str__(self):
        return "Gun's factory: %s, model: %s " % (self.factory, self.model)

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
