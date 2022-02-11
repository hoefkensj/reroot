

# DEFINITIONS
# Supersu run chk_mnt is_mount umount mount

import shlex, os, sys, time,subprocess
from multiprocessing import Process
from functools import partial

#create a process to be executed with processname = proc
subproc= partial(subprocess.Popen, stdin=subprocess.PIPE,stdout=subprocess.PIPE, universal_newlines=True)
proc= Process

#run the program as root :
def root(helper='sudo', trys=0):
	euid = os.geteuid
	if euid() != 0:
		print("Script not started as root. Running sudo..")
		args = [helper, sys.executable] + sys.argv + [os.environ]
		# the next line replaces the currently-running process with the sudo
		os.execlpe(helper, *args)
	else:
		return euid
	root(trys=(trys-1)) if trys else sys.exit("couldn't get root")


#implement the Su not as root but as switch User!!!
def su(user):
	shell = subproc
	user=shell(('su', user))
	return user
	
def run(a):
	shell = subproc
	tpl_a=shlex.split(a)
	out=shell(tpl_a)
	return out.stdout.readlines()

def cmd(*a):
	os.system(*a)
	return

def fork(*a):
	shell= Process(target=cmd ,args=a)
	shell.start()
	return shell

def umount(path):
	STAT= run(f'umount-l {path.lower()}')
	return STAT

def mount(**k):
	STAT = run(f"mount {k['args']}\n")
	return STAT

def wxl(line):
	sys.stdout.write(f'\t{line}')

def wrl(line):
	sys.stdout.write(f'\r{line}')

def wnl(line):
	sys.stdout.write(f'\n{line}')

if __name__ == '__main__':
	
	stat = fork('konsole &')
	
	print(stat)