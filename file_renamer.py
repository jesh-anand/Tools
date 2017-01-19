import os

from logger import DEBUG

""" file_renamer. py: This script renames plain numbered files with meaningful prefixes"""


def main():
    path = 'INSERT_PATH'
    prefix = "INSERT_PREFIX"
    directory = r"{}".format(path)

    os.chdir(directory)

    for srcTitle in os.listdir(directory):
        formattedTitle = prefix + "_" + srcTitle
        if srcTitle.startswith(formattedTitle):
            continue
        DEBUG("Renaming '{}' to '{}'".format(srcTitle, formattedTitle))
        os.rename(srcTitle, formattedTitle)


if __name__ == '__main__':
    main()
