#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# Write functions and modify main() to call them

#Manipulating file paths
def get_special_path(dir):
  filenames=os.listdir(dir)
  special_paths=[]
  for filename in filenames:
      special=re.search(r'__\w+__',filename)
      if special:
          special_paths.append(os.path.abspath(os.path.join(dir,filename)))
          print special_paths[-1]
      else:
          print "error occurs in ", dir, filename
  return special_paths

#File copying
def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for path in paths:
        fname=os.path.basename(path)
        shutil.copy(path, os.path.join(dir, fname))

#Calling an external program
#def zip_to(paths, zippath):
def zip_to(paths, zipfile):
    cmd='zip -j'+zipfile+' '+' '.join(paths)
    print "Command I'm going to do:"+cmd
    (status,output)=commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  
  # Call your functions
  paths=[]
  for dirname in args:
      paths.extend(get_special_path(dirname))

  if todir:
      copy_to(paths,todir)
  if tozip:
      zip_to(paths,tozip)
  else:
      print '\n'.join(paths)


if __name__ == "__main__":
  main()