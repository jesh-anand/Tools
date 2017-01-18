"""test_remove_file_more_than_a_week.py: Creates an todo file with title name as current date"""
import os
import time


def get_files():
    files_array = []
    for file in os.listdir("files/"):
        if file.endswith(".todo"):
            files_array.append(file)

    return files_array


# todo: fix file duration
def test_should_return_file_duration():
    files_directory = 'files/'
    file_list = get_files()
    one_week = time.time() - 604800
    for file in file_list:
        file_path = files_directory + file
        file_stat = os.stat(file_path)
        mtime = file_stat.st_mtime
        if mtime > one_week:
            print('Remove ' + file + ' at the age of ' + mtime)


def main():
    test_should_return_file_duration()


if __name__ == '__main__':
    main()
