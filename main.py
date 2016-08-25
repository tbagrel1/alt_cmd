# -*- coding:utf-8 -*

from os import getcwd, chdir, system

a = ""

print("-------------------------------- ### AltCMD ### ------------------------\
-------\n  AltCMD - Alternative Command Line Interpreter - V0.1.1 - tomsb07@gma\
il.com  ")
print("------------------------------------------------------------------------\
-------\n")
print("You are currently in the following directory :\n"+getcwd()+"\n")
r = raw_input("Do you want to go to the root directory ? [Y/n]\n")
if (r.lower()).strip() != "n":
	try :
		chdir("C:\\")
	except :
		print("\"C:\\\" : Invalid path or directory !")
print("\n")
while a != "exit" :
	a = raw_input(getcwd() + " > ")
	if (a[0:3]).lower() == "cd ":
		try :
			chdir(a[3:])
		except :
			print("\""+a[3:]+"\" : Invalid path or directory !")
	else :
		system(a)
