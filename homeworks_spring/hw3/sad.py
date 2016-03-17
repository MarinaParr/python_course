#!/usr/bin/python3.4
import argparse
import os.path
import subprocess
import shutil

parser = argparse.ArgumentParser(description="Saves current state of"
                                             "file or directory"
                                             "or runs utility 'diff' on it")
parser.add_argument("command",
                    type=str,
                    help="'store' for saving current state"
                         "of file or directory,"
                         "'diff' for running standard utility analysing"
                         "the difference between current and saver version")
parser.add_argument("path",
                    type=str,
                    help="Path to the file or directory to work with")

args = parser.parse_args()
command = args.command
path = args.path

if command == 'store':
    if os.path.isfile(path):
        shutil.copy(path, "/home/marina/PycharmProjects/untitled/sad")
    else:
        print("Не умею работать с аргументами-папками")
else:
    com = "diff " + path + " ./sad/" + path
    print(subprocess.call(com, shell=True))
