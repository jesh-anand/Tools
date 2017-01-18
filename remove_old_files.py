import os
import time


def main():
    file_age_in_days = 7
    remove_file_flag = False
    removeOldFiles(file_age_in_days, remove_file_flag)


def removeOldFiles(duration_in_days, flag):
    files = os.listdir()
    for file in files:
        if (isOldFile(file, duration_in_days)):
            if (flag):
                os.unlink(file)


def isOldFile(file, day):
    timeline = time.time() - (60 * 60 * 24 * day)
    date_format = '%Y-%m-%d %H:%M:%S'
    file_stat = os.stat(file)
    modified_time = file_stat.st_mtime
    last_modified_time = time.strftime(date_format, time.localtime(modified_time))
    if modified_time < timeline:
        print('Removing {} | Creation date: [{}]'.format(file, last_modified_time))
        return True
    return False


if __name__ == '__main__':
    main()
