#!/usr/bin/env python
import multiprocessing
import pickle
import shlex
import subprocess

import os
import sys

def cli_ctl():
	import ui.cli.main
	ui.cli.main.ctl()

def cmd(*a):
	os.system(*a)
	return

def fork(*a):
	shell= multiprocessing.Process(target=cmd ,args=a)
	shell.start()
	return shell

def umount(path):
	return subprocess.run(shlex.split(f'umount-l {path.lower()}') ,capture_output=True, universal_newlines=True).stdout

def mount(**k):
	opts= ''.join([f'--{opt} ' for opt in k.get('opts') if k.get('opts')])
	mountopts= '-o'+','.join(k.get('mntopts')) if k.get('mntopts') else ''
	return # subprocess.run(shlex.split(f"mount {opts} {k['args']}") ,capture_output=True, universal_newlines=True).stdout

def start(config,env):
	import cfg
	import lib.cfg
	path=os.path.join(home(),'cfg/roots',f'{config.upper()}.ini')
	print('USING:',path)
	dct=lib.cfg.to_dct(c=lib.cfg.readfile(c=lib.cfg.new(),f=path))
	seqs=dct['SEQUENCES']
	for seq in seqs:
		print(f'mount {seqs[seq]}')
		mount(args=seqs[seq])
	print('copieng resolf.conf...')
	#out=subprocess.run(shlex.split(f'cp -vf --dereference /etc/resolv.conf /os/{env}/etc') ,capture_output=True, universal_newlines=True).stdout
	return #out

def stop(MNT):
	umount(MNT['proc'])
	umount(MNT['sys'])
	umount(MNT['dev'])
	umount(MNT['boot'])
	umount(MNT['root'])
	return 0

def home():
	return f'{"/".join(os.path.realpath(__file__).split("/")[0:-1])}/'

def testenv(**k):
	n=k['n'];h=k['h'];m=k['m']
	[[print('\033[0m{n}\033[32m{k}={v}\033[0m'.format(n=n,v="\n".join([f'\033[0m',*os.environ.get(c).split(":")]),k=c)) for c in os.environ.keys() if t in c.casefold()]	for t in h]
	[print(f'{n}:\033[31m {v} : FAIL!\033[0m') for v in m  if not os.environ.get(v)]

def super_su(**k):
	print(f'GOT UID: {os.geteuid()}({os.environ.get("USER")}) NEED UID: 0 (root)!')
	args = [f'sudo env PYTHONPATH="{os.environ.get("PYTHONPATH")}" ', sys.executable] + sys.argv # + [os.environ]
	os.execvpe('sudo', args, os.environ)

def env_load():
	with open('/tmp/REROOT_USER.env','rb') as f :
		env_tmp=pickle.load(f)
	#only add keys that are missing, avoids overwriting USER ,USERHOME , ...
	os.environ={key : env_tmp[key] for key in env_tmp.keys()if key not in os.environ.keys() }
	

def env_store():
	with open('/tmp/REROOT_USER.env' , 'wb') as f:
		pickle.dump({**os.environ},f)