#!/usr/bin/python3.4
import argparse
import os.path
import subprocess
import re

parser = argparse.ArgumentParser(description="To make picture smaller")
parser.add_argument("percentage",
                    type=str,
                    help="how small a picture should be")
parser.add_argument("path",
                    type=str,
                    help="Path to the file or directory to work with")
parser.add_argument("--new_path",
                    type=str,
                    help="new path")
args = parser.parse_args()
percentage = args.percentage
path = args.path
new_path = args.new_path

if not os.path.exists(path):
    print("Dir or file doesn't exist")
else:
    if os.path.isfile(path):
        if new_path is None:
            new_path = path
        com = "convert "+path+" -resize "+percentage+"% "+new_path
        subprocess.call(com, shell=True)
    else:
        for d, dirs, files in os.walk(path):
            for f in files:
                path = os.path.join(d, f)
                a = re.findall("\.png", path)
                b = re.findall("\.jpg", path)
                if a != [] or b != []:
                    com = "convert "+path+" -resize "+percentage+"% "+path
                    subprocess.call(com, shell=True)
