from os import path

def get_full_path(filename):
    return path.join(path.dirname(__file__), filename)
