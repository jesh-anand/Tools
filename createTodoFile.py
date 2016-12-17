"""createTodoFile.py: Creates an todo file with title name as current date"""

import time
import os.path


def createfile():
    # My-File--2009-12-31--23-59-59.txt
    date = time.strftime("%d-%m-%Y")
    filename = "GOALS--" + date + ".todo"
    if not os.path.exists(filename):
        with open(filename, "a") as myfile:
            myfile.write("[RESULTS - {}]".format(date))
        print("INFO: " + filename + " created!")
    else:
        print("ERROR: " + filename + " already exist! Exiting..")

# TODO: To move files into archive if more than a week
def archiveFiles():
    pass


def main():
    createfile()


if __name__ == '__main__':
    main()
