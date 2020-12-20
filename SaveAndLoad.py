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
    create_directory(database_path)
    gun_list_file = open(save_file_path, 'wb')
    pickle.dump(gun_list, gun_list_file)
    gun_list_file.close()
    create_backup_file(gun_list)


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
        latest_file = directory_list[0]
        latest_file = int(latest_file.replace(".obj", ""))
        for file in directory_list:
            file = int(file.replace(".obj", ""))
            if file > latest_file:
                latest_file = file
        return str(latest_file) + '.obj'
    return None


def get_oldest_dump_file():
    directory_list = get_backup_directory_list()
    if len(directory_list) > 0:
        oldest_file = directory_list[0]
        oldest_file = int(oldest_file.replace(".obj", ""))
        for file in directory_list:
            file = int(file.replace(".obj", ""))
            if file < oldest_file:
                oldest_file = file
        return str(oldest_file) + '.obj'
    return None


def clear_backup_directory():
    while len(get_backup_directory_list()) > 3:
        print(get_backup_directory_list())
        os.remove(os.path.join(backup_directory_path, get_oldest_dump_file()))


def create_backup_file(gun_list):
    # TODO keep only 3 backupfiles
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_name = date + ".obj"
    backup_file_path = os.path.join(backup_directory_path, backup_name)
    create_directory(backup_directory_path)
    if len(os.listdir(backup_directory_path)) != 0:
        #If it is not empty
        latest_dump_file_path = os.path.join(backup_directory_path, get_latest_dump_file())
        print(latest_dump_file_path)
        gun_list_from_dump_file = pickle.load(open(latest_dump_file_path, 'rb'))
        # Compare lists with set, if the same set is empty
        print(gun_list)
        print(gun_list_from_dump_file)
        if not gun_list == gun_list_from_dump_file:
            copyfile(save_file_path, backup_file_path)
        else:
            os.rename(latest_dump_file_path, backup_file_path)
    else:
        copyfile(save_file_path, backup_file_path)
    clear_backup_directory()


def get_backup_directory_list():
    return os.listdir(backup_directory_path)
