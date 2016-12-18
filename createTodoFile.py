"""createTodoFile.py: Creates an todo file with title name as current date"""

import os.path
import time


def createfile():
    # My-File--2009-12-31--23-59-59.txt
    date = time.strftime("%d-%m-%Y")
    filename = "GOALS--" + date + ".todo"
    if not os.path.exists(filename):
        with open(filename, "a") as myfile:
            myfile.write("[RESULTS - {}]".format(date))
        print("INFO: " + filename + " created!")
        addfileToSublime(filename)
    else:
        print("ERROR: " + filename + " already exist! Exiting..")


def addfileToSublime(file):
    os.system("subl --add " + file)


def main():
    createfile()


if __name__ == '__main__':
    main()
