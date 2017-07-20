#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Simple and lightweight script to reproduce Windows cmd on system where cmd
is blocked"""

import os

HOME = """### AltCMD ###
"""
PS1 = "$ "
ROOT_DIRECTORY = "C:\\"

def do_cd(path):
    """Execute change directory action with try/exec handling"""
    try:
        os.chdir(path)
    except:
        print("<{}>: Invalid path or directory!\n".format(path))

def main():
    """Main function"""
    print(HOME)
    cmd = ""
    while cmd.lower() != "exit()":
        cmd = input(PS1).strip()
        if cmd.lower() == "exit()":
            pass
        elif cmd.lower() == "cd":
            do_cd(ROOT_DIRECTORY)
        elif len(cmd) > 3 and cmd[:3].lower() == "cd ":
            do_cd(cmd[3:])
        else:
            os.system(cmd)

if __name__ == "__main__":
    main()
