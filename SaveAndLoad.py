import filecmp
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
    create_backup_file(gun_list)
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


def get_latest_dump_file():
    directory_list = get_backup_directory_list()
    if len(directory_list) > 0:
        latest_file = int(directory_list[0])
        for file in directory_list:
            file = file.replace(".obj", "")
            if int(file) > latest_file:
                latest_file = int(file)
        return str(latest_file)
    return None


def create_backup_file(gun_list):
    # TODO keep only 3 backupfiles
    latest_dump_file_path = os.path.join(backup_directory_path, get_latest_dump_file())
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_name = date + ".obj"
    backup_file_path = os.path.join(backup_directory_path, backup_name)
    create_directory(backup_directory_path)
    gun_list_from_backup = pickle.load(open(latest_dump_file_path, 'rb'))
    # Compare lists with set, if the same set is empty
    if not (set(gun_list) & set(gun_list_from_backup)) == set():
        copyfile(save_file_path, backup_file_path)
    else:
        os.rename(latest_dump_file_path, backup_file_path)
    clear_backup_directory()


def clear_backup_directory():
    directory_list = get_backup_directory_list()
    oldest_file = int(directory_list[0])
    while len(directory_list) > 3:
        for file in directory_list:
            file = file.replace(".obj", "")
            if int(file) < oldest_file:
                oldest_file = int(file)
        os.remove(os.path.join(backup_directory_path, str(oldest_file) + '.obj'))

def get_year(file):
    return int(file[6:10])


def get_day(file):
    return int(file[0:2])


def get_month(file):
    return int(file[3:5])


def get_hour(file):
    return int(file[11:13])


def get_min(file):
    return int(file[14:16])


def get_sec(file):
    return int(file[17:19])


def get_backup_directory_list():
    return os.listdir(backup_directory_path)
