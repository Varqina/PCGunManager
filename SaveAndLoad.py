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
    directory_list = os.listdir(backup_directory_path)
    latest_file = directory_list[0]
    for file in directory_list:
        if get_year(file) > get_year(latest_file):
            latest_file = file
            continue
        if get_month(file) > get_month(latest_file):
            latest_file = file
            continue
        if get_day(file) > get_day(latest_file):
            latest_file = file
            continue
        if get_hour(file) > get_hour(latest_file):
            latest_file = file
            continue
        if get_min(file) > get_min(latest_file):
            latest_file = file
            continue
        if get_sec(file) > get_sec(latest_file):
            latest_file = file
            continue
    return latest_file


def create_backup_file(gun_list):
    # TODO chech if file has not the same content as prevoius
    # TODO keep only 3 backupfiles
    latest_dump_file_path = os.path.join(backup_directory_path, get_latest_dump_file())
    date = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
    backup_name = date + ".obj"
    backup_file_path = os.path.join(backup_directory_path, backup_name)
    create_directory(backup_directory_path)
    gun_list_from_backup = pickle.load(open(latest_dump_file_path, 'rb'))
    #Compare lists with set, if the same set is empty
    if not (set(gun_list) & set(gun_list_from_backup)) == set():
        copyfile(save_file_path, backup_file_path)
    else:
        os.rename(latest_dump_file_path, backup_file_path)


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
