"""moveFiles.py: Move files to specific directory defined by file extension"""

import os
import shutil

#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                ('-.  _   .-')                      (`-.      ('-.  _  .-')     #
#                              _(  OO)( '.( OO )_                  _(OO  )_  _(  OO)( \( -O )    #
#    ,------.,-.-')  ,--.     (,------.,--.   ,--.).-'),-----. ,--(_/   ,. \(,------.,------.    #
# ('-| _.---'|  |OO) |  |.-')  |  .---'|   `.'   |( OO'  .-.  '\   \   /(__/ |  .---'|   /`. '   #
# (OO|(_\    |  |  \ |  | OO ) |  |    |         |/   |  | |  | \   \ /   /  |  |    |  /  | |   #
# /  |  '--. |  |(_/ |  |`-' |(|  '--. |  |'.'|  |\_) |  |\|  |  \   '   /, (|  '--. |  |_.' |   #
# \_)|  .--',|  |_.'(|  '---.' |  .--' |  |   |  |  \ |  | |  |   \     /__) |  .--' |  .  '.'   #
#   \|  |_)(_|  |    |      |  |  `---.|  |   |  |   `'  '-'  '    \   /     |  `---.|  |\  \    #
#    `--'    `--'    `------'  `------'`--'   `--'     `-----'      `-'      `------'`--' '--'   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #

class FileManager(object):
    VIDEO_EXTENSIONS = ('.mp4', '.mkv', '.avi')

    def __init__(self, target, destination):
        self.target = 'Downloads' if target is None else target
        self.destination = 'Downloads' if destination is None else destination

    def manage(self):
        files = os.listdir(self.target)
        try:
            for file in files:
                for extension in FileManager.VIDEO_EXTENSIONS:
                    if file.endswith(extension):
                        shutil.move(self.target + "/" + file, self.destination)
        except IOError as e:
            print("ERROR | Directory not found: {}".format(self.target), e)


if __name__ == '__main__':
    util = FileManager(target='../Downloads/Completed', destination='../Movies')
    util.manage()
