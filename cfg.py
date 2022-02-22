import os
import configparser

def new(*a):
	"""
	create an empty configparser with: extended interpolation, : for delimiter and allowing empty value's for keys
	:return: configerparser obj.
	"""
	cfg = configparser.ConfigParser(	interpolation		=	configparser.ExtendedInterpolation(),
																		delimiters			=	':',
																		allow_no_value	=	True	)  # create empty config
	cfg.optionxform = lambda option: option
	return cfg

def readfile(**k):
	"""
	gets config
	:param k: path,conf
	:keyword path: path
	:keyword c: config parser
	:return:
	"""
	config=k.get('c')
	path=k.get('path')
	config.read(path) if os.path.exists(path) else None
	return config

def savefile(**k) -> None:
	"""
	writes the configparser config to a file.
	:param k: keywords:file,conf
	:keyword file: file to save the config to
	:keyword conf: config(configparser) to be saved
	:return:
	"""
	f= k.get('f')
	c=k.get('c')
	with open(f, 'w') as file:
			c.write(file)

def set_key(**k):
	"""
	
	:keyword key:
	:keyword val:
	:keyword section:
	:keyword file:
	:return: config
	"""
	c=k.get('c')
	s=k.get('s')
	key=k.get('key')
	val=k.get('val')
	c[s]= c[s] if dict(c).get(s) else {}
	c[s][key]=str(val)
	return c

def save_key(**k):
	k['c']=set_key(**k)
	savefile(**k)



def set_dict(**k):
	"""
	loads a dictionary formatted config group into the config ,
	the dictionary needs to meet the following specifications:
	the first two key:val pairs are file:<filename >and section:<section-name> within the file
	example:
	config={file : btrwin,
					section: PATH,
					key1: val1}
	:param dct: dictionary where the first two key:val pairs are file:filename and section within the file
	:return:
	"""

	section= dct.pop('section')
	for key in dct.keys():
		G=set_key(key=key,val=dct[key],section=section,file=file,config=cfg)
	return G