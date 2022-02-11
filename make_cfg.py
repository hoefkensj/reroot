#!/usr/bin/python
from reroot.cfg import cfg_write
def make_ini(file_name):
	with open(f'{file_name}.ini' , 'w') as file:
		file.write(f'[DEFAULT]\nfilename\t:\t{file_name}\nfiletype\t:\tini')
	return f'{file_name}.ini'

def cfg_skell(cfg):
	cfg['DEFAULT']['NAME']=''
	cfg['DEFAULT']['ROOT']=''
	cfg['LABELS']['ROOT']= ''
	cfg['LABELS']['BOOT']=''
	cfg['LABELS']['ESP']=''
	return cfg

def make_new(cfg_name):
	file=make_ini(cfg_name)
	config=cfg()
	cfg=cfg_skell(config)
	cfg_write(file,cfg)
	
	return cfg_name



	
def main():
	pass


if __name__ == '__main__':
	main()


def create(file_Config, dct_Config, cfg_config):
	cfg = tocfg(dct_Config, cfg_config)
	write(file_Config, cfg)
