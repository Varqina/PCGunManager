from GUI import GuiColumnChoicer


class ColumnChoicerManagerClass:
    factory = True
    model = True
    bullets_used_total = False
    buy_date = False
    buy_price = False
    brand_new = False
    last_cleaning = False
    gun_serial_number = True

    def get_table_heading(self):
        # ['index', 'factory', 'model', 'serial number']
        heading = ['index']
        if self.factory: heading.append('Factory')
        if self.model: heading.append('Model')
        if self.gun_serial_number: heading.append('Serial Number')
        if self.bullets_used_total: heading.append('Used Bullets')
        if self.buy_date: heading.append('Buy Date')
        if self.buy_price: heading.append('Buy Price')
        if self.brand_new: heading.append('First Owner')
        if self.last_cleaning: heading.append('Cleaning Date')
        return heading

    def get_row_with_selected_properties(self, index, gun):
        # [index, gun.get_factory(), gun.get_model(), gun.get_gun_serial_number()]
        row_tab = [index]
        if self.factory: row_tab.append(gun.get_factory())
        if self.model: row_tab.append(gun.get_model())
        if self.gun_serial_number: row_tab.append(gun.get_gun_serial_number())
        if self.bullets_used_total: row_tab.append(gun.get_bullets_used())
        if self.buy_date: row_tab.append(gun.get_buy_date())
        if self.buy_price: row_tab.append(gun.get_buy_price())
        if self.brand_new: row_tab.append(gun.get_brand_new())
        if self.last_cleaning: row_tab.append(gun.get_last_cleaning())
        return row_tab

    def get_gun_serial_number_checkbox_status(self):
        return self.gun_serial_number

    def get_model_checkbox_status(self):
        return self.model

    def get_brand_new_checkbox_status(self):
        return self.brand_new

    def get_last_cleaning_checkbox_status(self):
        return self.last_cleaning

    def get_bullets_used_total_checkbox_status(self):
        return self.bullets_used_total

    def get_buy_date_checkbox_status(self):
        return self.buy_date

    def get_buy_price_checkbox_status(self):
        return self.buy_price

    def set_model_checkbox_status(self, model):
        self.model = model

    def get_factory_checkbox_status(self):
        return self.factory

    def set_brand_new_checkbox_status(self, brand_new):
        self.brand_new = brand_new

    def set_gun_serial_number_checkbox_status(self, gun_serial_number):
        self.gun_serial_number = gun_serial_number

    def set_last_cleaning_checkbox_status(self, last_cleaning):
        self.last_cleaning = last_cleaning

    def set_bullets_used_total_checkbox_status(self, bullets_used_total):
        self.bullets_used_total = bullets_used_total

    def set_buy_date_checkbox_status(self, buy_date):
        self.buy_date = buy_date

    def set_buy_price_checkbox_status(self, buy_price):
        self.buy_price = buy_price

    def set_factory_checkbox_status(self, factory):
        self.factory = factory

    def set_properties_data(self, value_dictionary):
        if len(value_dictionary) != 0:
            self.factory = value_dictionary['factory']
            self.model = value_dictionary['model']
            self.gun_serial_number = value_dictionary['gun_serial_number']
            self.bullets_used_total = value_dictionary['bullets_used_total']
            self.buy_date = value_dictionary['buy_date']
            self.buy_price = value_dictionary['buy_price']
            self.brand_new = value_dictionary['brand_new']
            self.last_cleaning = value_dictionary['last_cleaning']
        # save to file

    def get_values_as_dictionary(self):
        dictionary = {'factory': self.get_factory_checkbox_status(),
                      'model': self.get_model_checkbox_status(),
                      'gun_serial_number': self.get_gun_serial_number_checkbox_status(),
                      'bullets_used_total': self.get_bullets_used_total_checkbox_status(),
                      'buy_date': self.get_buy_date_checkbox_status(),
                      'buy_price': self.get_buy_price_checkbox_status(),
                      'brand_new': self.get_brand_new_checkbox_status(),
                      'last_cleaning': self.get_last_cleaning_checkbox_status()}
        return dictionary
