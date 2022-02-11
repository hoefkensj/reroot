#from pynput import keyboard
from sys import stdout

def wxl(line):
	stdout.write(f'\t{line}')

def wrl(line):
	stdout.write(f'\r{line}')

def wnl(line):
	stdout.write(f'\n{line}')

