#!/usr/bin/env python
import os
def PYTHONPATH_ADD_REQUIRED_FOLDERS():
	import os
	import os.path as P
	PYPATHS=os.environ['PYTHONPATH'].split(':') if os.environ.get('PYTHONPATH') else []
	PKGDIR=P.dirname(__file__)
	PARDIR=P.dirname(PKGDIR)
	if PKGDIR not in PYPATHS:
		PYPATHS = '{}:{}'.format(PKGDIR, ':'.join(PYPATHS))
		os.environ['PYTHONPATH']	= PYPATHS
	if PARDIR not in PYPATHS:
		PYPATHS = '{}:{}'.format(PARDIR, ':'.join(PYPATHS))
		os.environ['PYTHONPATH']	= PYPATHS

def procedure_user():
	import reroot
	reroot.main.env_store()
	reroot.main.super_su(helper='pkexec')
	
def procedure_root():
	import main
	print(f'running as  UID: {os.geteuid()} ({os.environ.get("USER")}) [OK]')
	main.env_load()
	main.cli_ctl()

if os.geteuid() == 0:	procedure_root()
else: procedure_user()


