#!/usr/bin/python3
import sys,argparse,os
import clit,cfg,file
from bash import *

from configparser import ConfigParser, ExtendedInterpolation


# def run(a,**k):
# 	binbash=f'/usr/bin/bash'
# 	thisproc=subprocess.Popen(a , stdout=subprocess.PIPE, universal_newlines=True)
# 	return thisproc

def root(helper='sudo',trys=0):
	euid = os.geteuid
	if euid() != 0:
		print("Script not started as root. Running sudo..")
		args = [helper, sys.executable] + sys.argv + [os.environ]
		# the next line replaces the currently-running process with the sudo
		os.execlpe(helper, *args)
	else: return euid
	root(trys=(trys-1)) if trys else sys.exit("couldn't get root")


def start(seqs,env):
	for seq in seqs:
		wnl(f'mount {seqs[seq]}')
		mount(args=seqs[seq])
	wnl('copieng resolf.conf...')
	run( f'cp -vf --dereference /etc/resolv.conf /os/{env}/etc')


	return 0


def startx(seqs, env,username='hoefkens'):
	wnl("test")
	start(seqs=seqs, env=env)
	wnl('configuring Xephyr')
	wnl(f'cp /home/{username}/.Xauthority /os/{env}/home/{username}')
	run(f'cp /home/{username}/.Xauthority /os/{env}/home/{username}')
	run(f'cp /root/.Xauthority /os/{env}/root/')
	cmd(f'Xephyr -ac -screen 1920x1080 -br -reset -terminate -name "Xephyr" 2> /dev/null :4 & export DISPLAY=:4.0')
	#run( f'konsole -e chroot /os/{env} /bin/bash')
	run(f'chroot /os/{env} /bin/bash ')
	os.chroot(f'/os/{env}')
	run(f'source /etc/profile')
	#run(f'su {username}')
	run(f'cd ~/')
	run(f'xhost +')
	run(f'DISPLAY=:4.0 sudo -u hoefkens dbus-launch /usr/bin/startplasma-x11 2> /dev/null')
	return
	
def stop(MNT):
	umount(MNT['proc'])
	umount(MNT['sys'])
	umount(MNT['dev'])
	umount(MNT['boot'])
	umount(MNT['root'])
	return 0

def home():
	path = f'{"/".join(os.path.realpath(__file__).split("/")[0:-1])}/'
	print(path)
	return path


def getargs(): #get arguments from commandline
	parser=argparse.ArgumentParser()
	parser.add_argument('cmd', help='[start|stop] chroot for [env]')
	parser.add_argument('env', type=str ,help='[env]')
	args = parser.parse_args()
	return args

def get_seqs(env):
	dict= cfg.to_dct(cfg.get(f'{"/".join(os.path.realpath(__file__).split("/")[0:-1])}/Rootes/{env.upper()}.ini'))['SEQUENCES']
	return dict
	
def main():
	root()
	a=getargs()
	seqs=get_seqs(a.env)
	print((seqs))
	
	
	dct_fnc = {
			'start': start,
			'stop' : stop
			}
	act = dct_fnc[a.cmd]
	#
	act(seqs,a.env)
	cmd=shlex.split(f'sudo konsole -e chroot /os/{a.env} /bin/bash')
	subprocess.Popen(cmd,start_new_session=True)

if __name__ == '__main__':
	main()
	
	

	
	#if args.cmd=='stop'else

	
	

	
	

	
	#mounted = is_mount(path.lower())
	#if mounted:




#
# print('Press s or n to continue:')
#
# with keyboard.Events() as events:
# 	# Block for as much as possible
# 	event = events.get(1e6)
# 	if event.key == keyboard.KeyCode.from_char('s'):
# 		print("YES")
#
#
#
#
#
		


	
	
#bash.run('chroot','/mnt/gentoo /bin/bash')
#bash.run('source','/etc/profile')
#bash.run('export PS1="(chroot) ${PS1}"')



