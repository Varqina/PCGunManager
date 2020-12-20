import unittest

from SaveAndLoad import get_latest_backup, get_oldest_backup


class TestGetLatestBackup(unittest.TestCase):
    def test_get_latest_backup_by_year(self):
        directory_list = ['20201220185318.obj', '20221220185318.obj', '20191220185318.obj']
        self.assertEqual(get_latest_backup(directory_list), r'D:\Python\PCGunManager\backup\20221220185318.obj')

    def test_get_latest_backup_by_month(self):
        directory_list = ['20201120185318.obj', '20201020185318.obj', '20200920185318.obj']
        self.assertEqual(get_latest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120185318.obj')

    def test_get_latest_backup_by_day(self):
        directory_list = ['20201120185318.obj', '20201118185318.obj', '20201117185318.obj']
        self.assertEqual(get_latest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120185318.obj')

    def test_get_latest_backup_by_hour(self):
        directory_list = ['20201120155318.obj','20201120185318.obj','20201120125318.obj']
        self.assertEqual(get_latest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120185318.obj')

    def test_get_latest_backup_by_minutes(self):
        directory_list = ['20201120154418.obj', '20201120154418.obj', '20201120155318.obj']
        self.assertEqual(get_latest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120155318.obj')

    def test_get_latest_backup_by_sec(self):
        directory_list = ['20201120154418.obj', '20201120154456.obj','20201120154419.obj']
        self.assertEqual(get_latest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120154456.obj')

    def test_get_oldest_backup_by_year(self):
        directory_list = ['20201220185318.obj', '20221220185318.obj', '20191220185318.obj']
        self.assertEqual(get_oldest_backup(directory_list), r'D:\Python\PCGunManager\backup\20191220185318.obj')

    def test_get_oldest_backup_by_month(self):
        directory_list = ['20201120185318.obj', '20201020185318.obj', '20200920185318.obj']
        self.assertEqual(get_oldest_backup(directory_list), r'D:\Python\PCGunManager\backup\20200920185318.obj')

    def test_get_oldest_backup_by_day(self):
        directory_list = ['20201120185318.obj', '20201118185318.obj', '20201117185318.obj']
        self.assertEqual(get_oldest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201117185318.obj')

    def test_get_oldest_backup_by_hour(self):
        directory_list = ['20201120155318.obj', '20201120185318.obj', '20201120125318.obj']
        self.assertEqual(get_oldest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120125318.obj')

    def test_get_oldest_backup_by_minutes(self):
        directory_list = ['20201120154418.obj', '20201120154418.obj', '20201120155318.obj']
        self.assertEqual(get_oldest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120154418.obj')

    def test_get_oldest_backup_by_sec(self):
        directory_list = ['20201120154418.obj', '20201120154456.obj', '20201120154419.obj']
        self.assertEqual(get_oldest_backup(directory_list), r'D:\Python\PCGunManager\backup\20201120154418.obj')
