import os


def filesCount(path, ext):
    if len(path) == 0:
        return False
    else:
        x = 0
        for files in os.listdir(path):
            if files.lower().endswith(ext.lower()):
                x += 1
        return x