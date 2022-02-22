#!/usr/bin/python

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


	
def main():
	pass


if __name__ == '__main__':
	main()


