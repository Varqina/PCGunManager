import unittest

from GunClass import GunClass
from GunManagerClass import GunManagerClass


class TestGetLatestBackup(unittest.TestCase):
    def test_check_if_gun_exists_in_database(self):
        gun_list = GunManagerClass()
        gun = GunClass("CZ", "Shadow", "123456789")
        gun_list.gun_list.append(gun)
        self.assertTrue(gun_list.check_if_gun_exists_in_database(gun))

    def test_check_if_gun_not_exists_in_database_serial_number(self):
        gun_list = GunManagerClass()
        gun = GunClass("CZ", "Shadow", "123456789")
        gun2 = GunClass("CZ", "Shadow", "987654321")
        gun_list.gun_list.append(gun)
        self.assertFalse(gun_list.check_if_gun_exists_in_database(gun2))

    def test_check_if_gun_not_exists_in_database_model(self):
        gun_list = GunManagerClass()
        gun = GunClass("CZ", "Shadow", "123456789")
        gun2 = GunClass("CZ", "Shadow2", "987654321")
        gun_list.gun_list.append(gun)
        self.assertFalse(gun_list.check_if_gun_exists_in_database(gun2))

    def test_check_if_gun_not_exists_in_database_factory(self):
        gun_list = GunManagerClass()
        gun = GunClass("CZ", "Shadow", "123456789")
        gun2 = GunClass("1", "Shadow2", "987654321")
        gun_list.gun_list.append(gun)
        self.assertFalse(gun_list.check_if_gun_exists_in_database(gun2))


