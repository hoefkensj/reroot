#!/usr/bin/env python
import os
import sys

def PYTHONPATH_ADD_REQUIRED_FOLDERS():
	python,script=sys.executable,sys.argv
	PYPATHORG=os.environ.get('PYTHONPATH')
	PYPATHPYX=os.path.dirname(os.path.dirname(python))
	PYPATHPKG=os.path.dirname(os.path.dirname(script[0]))
	PYTHONPATH='{}:{}:{}'.format(PYPATHORG,PYPATHPYX,PYPATHPKG)
	os.environ['PYTHONPATH']	= PYTHONPATH

def procedure_user():
	import reroot
	reroot.main.env_store()
	reroot.main.super_su(su='pkexec')
	
def procedure_root():
	import main
	print(f'running as  UID: {os.geteuid()} ({os.environ.get("USER")}) [OK]')
	main.env_load()
	main.cli_ctl()

def run():
	PYTHONPATH_ADD_REQUIRED_FOLDERS()
	procedure_root() if os.geteuid() == 0 else procedure_user()
run()

#


