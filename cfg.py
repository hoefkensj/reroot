from configparser import ConfigParser,ExtendedInterpolation


def __init__():
	return new()


def new():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':')  # create empty config
	cfg.optionxform = lambda option: option
	return cfg
	
def create(file,config):
	cfg= tocfg(dct_Config, config)
	write(file, config)
	


def read_from(file,config):
	config.read(file)
	return config

def to_dct(cfg,dct={}):
	for section in cfg.keys():
		dct[section]= dict(cfg[section])
	return dct

def to_cfg(dct,cfg):
	cfg.read_dict(dct)
	return dct


def get(ini):
	cfg=new()
	cfg = read_from(ini, cfg)
	return cfg

def write(filename,cfg):
	with open(filename, 'w') as file:
		cfg.write(file)
		
		
if __name__ == '__main__':
	new()

