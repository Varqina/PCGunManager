import os
import pickle
from datetime import datetime
from shutil import copyfile

current_path = os.path.dirname(os.path.realpath(__file__))
database_directory = 'database'
database_path = os.path.join(current_path, database_directory)
save_file = 'gun_list.obj'
save_file_path = os.path.join(database_path, save_file)
backup_directory = 'backup'
backup_directory_path = os.path.join(current_path, backup_directory)


def save_application_data(gun_list):
    create_backup_file()
    create_directory(database_path)
    gun_list_file = open(save_file_path, 'wb')
    pickle.dump(gun_list, gun_list_file)


def load_application_data():
    if os.path.exists(save_file_path):
        gun_list_file = open(save_file_path, 'rb')
        gun_list = pickle.load(gun_list_file)
        return gun_list
    else:
        gun_list = []
        return gun_list


def clear_application_data():
    pass


def create_directory(new_directory_path):
    if not os.path.isdir(new_directory_path):
        try:
            os.mkdir(new_directory_path)
        except OSError:
            print("Creation of the directory %s failed " % new_directory_path)
        else:
            print("Successfully created the directory %s " % new_directory_path)


def create_backup_file():
    date = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
    backup_name = date + ".obj"
    create_directory(backup_directory_path)
    backup_file_path = os.path.join(backup_directory_path, backup_name)
    try:
        copyfile(save_file_path, backup_file_path)
    except IOError:
        print("Backup file creation failed")
    else:
        print("Backup file created")
