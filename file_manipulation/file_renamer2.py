import os

""" file_renamer2. py: Shortens file title

ie. 
Old Title:
13 - Anthony Robbins - Personal power II - How to condition yourself to wealth.mp3 

New Title:
13 - How to condition yourself to wealth.mp3

"""


def main():
    path = 'INSERT PATH HERE'
    renameFiles(path)


def renameFiles(path):
    directory = r"{}".format(path)
    os.chdir(directory)

    for file in os.listdir(directory):
        list = file.split(' - ')
        trackNo = list[0]
        title = list[3]
        newTitle = '{} - {}'.format(trackNo, title)
        print(file + ' => ' + newTitle)
        os.rename(file, newTitle)


if __name__ == '__main__':
    main()