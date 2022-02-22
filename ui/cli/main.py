#!/usr/bin/env python
import click as C
import subprocess
import shlex

import main

@C.group()
def ctl():
	"""
	help for this
	"""
	pass

@ctl.command()
@C.argument('config',required=True,type=str)
def start(config):
	"""
	start help
	:param config:
	:return:
	"""
	import main
	main.start(config,config)
	subprocess.run(shlex.split(f'konsole -e chroot /os/{config} /bin/bash'),start_new_session=True)


@ctl.command()
@C.argument('config',required=True,type=str)
def stop(config):
	"""
	stop help
	:param config:
	:return:
	"""
	main.stop(reroot.get_seqs(config), config)
	
