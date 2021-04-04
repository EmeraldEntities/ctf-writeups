#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import commands
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class color:
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    BLUE2 = '\033[1;36m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    GREEN = '\033[1;32m'

def Steg_brute():
    dicc = "potential_passwords.txt"
    ifile = "picture2.bmp"
    
    nlines = len(open(dicc).readlines())
    print("brute forcing")
    with open(dicc, 'r') as passFile:
        for line in passFile.readlines():
            password = line.strip('\r\n')
            lpassword = password.lower()
            test("picture1.bmp", password)
            test("picture1.bmp", lpassword)
            test("picture2.bmp", password)
            test("picture2.bmp", lpassword)
            test("picture3.bmp", password)
            test("picture3.bmp", lpassword)
            
def test(ifile, password):
    ofile = ifile.split('.')[0] + "_flag.txt"
    r = commands.getoutput("steghide extract -sf %s -p '%s' -xf %s" % (ifile, password, ofile))
    print(color.INFO + "testing " + ifile)
    print(color.BLUE + password)
    print(color.FAIL + r)
    if not "could not extract" in r:
        print(color.GREEN + "\n\n " + r + color.ENDC)
        print("\n\n [+] " + color.INFO + "Information obtained with password:" + color.GREEN + " %s\n" % password + color.ENDC)

Steg_brute()
