#!/usr/bin/env python3

import sys, os
from tv.main import TV

current_script_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_script_path)

def log(s):
    sys.stderr.write("start to run: ")
    sys.stderr.write(s)
    sys.stderr.write("\n")
    sys.stderr.flush()

def get_files(directory) -> list:
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
if __name__ == "__main__":
    all_files = get_files(current_directory)
    tv = TV(file_list=all_files)
    tv.execute_batch()