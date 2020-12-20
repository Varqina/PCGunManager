import os
import pickle
from datetime import datetime
from shutil import copyfile


current_path = os.path.dirname(os.path.realpath(__file__))
database_directory_name = 'database'
database_directory = os.path.join(current_path, database_directory_name)
save_file = 'gun_list.obj'
database_file = os.path.join(database_directory, save_file)
backup_directory_name = 'backup'
backup_directory = os.path.join(current_path, backup_directory_name)

#TODO logger
#TODO pywinauto tests


def save_application_data(gun_list):
    create_directory(database_directory)
    gun_list_file = open(database_file, 'wb')
    pickle.dump(gun_list, gun_list_file)
    gun_list_file.close()
    create_backup_file(gun_list)


def load_application_data():
    if os.path.exists(database_file):
        gun_list_file = open(database_file, 'rb')
        gun_list = pickle.load(gun_list_file)
        return gun_list
    else:
        return []


def clear_application_data():
    pass


def create_directory(new_directory):
    if not os.path.isdir(new_directory):
        try:
            os.mkdir(new_directory)
        except OSError:
            print("Creation of the directory %s failed " % new_directory)
        else:
            print("Successfully created the directory %s " % new_directory)


def get_backup_directory_content():
    return os.listdir(backup_directory)


def get_latest_backup(directory_list=None):
    if directory_list is None:
        directory_list = get_backup_directory_content()
    if len(directory_list) > 0:
        latest_created_file = directory_list[0]
        latest_created_file = int(latest_created_file.replace(".obj", ""))
        for file in directory_list:
            file = int(file.replace(".obj", ""))
            if file > latest_created_file:
                latest_created_file = file
        return os.path.join(backup_directory, (str(latest_created_file) + '.obj'))
    return None


def get_oldest_backup(directory_list=None):
    if directory_list is None:
        directory_list = get_backup_directory_content()
    if len(directory_list) > 0:
        oldest_created_file = directory_list[0]
        oldest_created_file = int(oldest_created_file.replace(".obj", ""))
        for file in directory_list:
            file = int(file.replace(".obj", ""))
            if file < oldest_created_file:
                oldest_created_file = file
        return os.path.join(backup_directory, (str(oldest_created_file) + '.obj'))
    return None


def clear_backup_directory():
    while len(get_backup_directory_content()) > 3:
        os.remove(get_oldest_backup())


def create_backup_file(gun_list):
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file_name = current_date + ".obj"
    backup_file = os.path.join(backup_directory, backup_file_name)
    create_directory(backup_directory)
    if len(os.listdir(backup_directory)) != 0:
        #If it is not empty
        latest_created_backup_file_path = get_latest_backup()
        gun_list_from_backup_file = pickle.load(open(latest_created_backup_file_path, 'rb'))
        # Compare lists with set, if the same set is empty
        if not gun_list == gun_list_from_backup_file:
            copyfile(database_file, backup_file)
        else:
            os.rename(latest_created_backup_file_path, backup_file)
    else:
        copyfile(database_file, backup_file)
    clear_backup_directory()



