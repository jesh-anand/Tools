"""test_remove_file_more_than_a_week.py: Moves files to archive than a more than a week"""
import os
import time

from todo_file_generator.test import constants


def get_files():
    files_array = []
    for file in os.listdir(constants.FILES_DIRECTORY):
        if file.endswith(constants.FILE_EXTENSION):
            files_array.append(file)
    return files_array


def remove_file(source, target):
    os.unlink(source, target)


def test_should_return_file_duration():
    one_week = time.time() - (60 * 60 * 24 * 7)
    file_list = get_files()
    for file in file_list:
        file_path = constants.FILES_DIRECTORY + file
        file_stat = os.stat(file_path)
        modified_time = file_stat.st_mtime
        file_creation_time = time.strftime(constants.DATE_FORMAT, time.localtime(modified_time))
        if modified_time < one_week:
            print('Moving {} | Creation date: [{}]'.format(file, file_creation_time))
            target_path = constants.FILES_DIRECTORY + constants.ARCHIVE_DIRECTORY + file
            # remove_file(file_path, target_path)


def main():
    test_should_return_file_duration()


if __name__ == '__main__':
    main()
