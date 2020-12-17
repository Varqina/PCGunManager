import os
import pickle

current_path = os.path.dirname(os.path.realpath(__file__))
database_directory = 'database'
database_directory_path = os.path.join(current_path, database_directory)
save_file = 'gun_list.obj'
save_file_path = os.path.join(database_directory_path, save_file)


def save_application_data(gun_list):
    create_database_directory()
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


def create_database_directory():
    if not os.path.isdir(database_directory_path):
        try:
            os.mkdir(database_directory_path)
        except OSError:
            print("Creation of the directory %s failed " % database_directory_path)
        else:
            print("Successfully created the directory %s " % database_directory_path)
