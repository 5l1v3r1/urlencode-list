#!/usr/bin/env python
import sys
import os.path
import urllib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help='Input file', type=str, required=True)
parser.add_argument('--output', '-o', help='Output file', type=str)
parser.add_argument('--decode', '-d', help='Decode file', action='store_true')

args = parser.parse_args()

if not os.path.exists(args.file): 
    print("{} not found".format(args.file))
    sys.exit(0)

f = open(args.file)
names = f.read().splitlines()
f.close()

if args.decode is False:
    #This will encode the file
    if args.output is not None:
        #Check to see if we are outputting a file
        path = os.path.join(os.getcwd(), args.output)

        f = open(path, 'w+')
        for name in names:
            f.write(urllib.quote(name) + '\n')
        f.close()
    else:
        for name in names:
            print(urllib.quote(name))
else:
    #Here we will decode if the user has supplied the decode argument
    if args.output is not None:
        #Check to see if we are outputting a file
        path = os.path.join(os.getcwd(), args.output)

        f = open(path, 'w+')
        for name in names:
            f.write(urllib.unquote(name) + '\n')
        f.close()
    else:
        for name in names:
            print(urllib.unquote(name))
