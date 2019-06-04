#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""

def get_special_path(dir):
    for filename in os.listdir(dir):
        if not filename.endswith('.py'):
            print(os.path.abspath(filename))

def copy_to(dir):
    dest = os.getcwd()+dir
    if not os.path.exists(dest):
        os.mkdir(dest)
    for filename in os.listdir(os.getcwd()):
        if re.match(r'(\w+)__', filename):
            shutil.copy(os.path.abspath(filename), dest)

def to_zip(zipfile):
    listFile = []
    for filename in os.listdir(os.getcwd()):
        if re.match(r'(\w+)__', filename):
            listFile.append(filename)
    cmd = 'zip -j '+str(zipfile)+' '+' '.join(listFile)
    os.popen(cmd)



def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        get_special_path(os.getcwd())
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        copy_to(todir)

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        to_zip(tozip)


    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

        # +++your code here+++
        # Call your functions


if __name__ == "__main__":
    main()
