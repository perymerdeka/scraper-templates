import os
from os.path import abspath, curdir, join


def default_driver_path():
    # default path for browser driver

    drive_dir = 'scraper'
    default_path = abspath(join(curdir, drive_dir))

    return default_path
