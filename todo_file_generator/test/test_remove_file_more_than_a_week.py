"""test_remove_file_more_than_a_week.py: Moves files to archive than a more than a week"""
import os
import time


def get_files():
    files_array = []
    files_directory = 'files/'
    extension = 'todo'
    for file in os.listdir(files_directory):
        if file.endswith(extension):
            files_array.append(file)

    return files_array


def move_file(source, target):
    os.rename(source, target)


def test_should_return_file_duration():
    files_directory = 'files/'
    archive_directory = 'archive/'
    date_format = '%Y-%m-%d %H:%M:%S'
    one_week = time.time() - 604800
    file_list = get_files()
    for file in file_list:
        file_path = files_directory + file
        file_stat = os.stat(file_path)
        mtime = file_stat.st_mtime
        file_creation_time = time.strftime(date_format, time.localtime(mtime))
        if mtime < one_week:
            print('Moving {} | Creation date: [{}]'.format(file, file_creation_time))
            target_path = files_directory + archive_directory + file
            move_file(file_path, target_path)


def main():
    test_should_return_file_duration()


if __name__ == '__main__':
    main()
