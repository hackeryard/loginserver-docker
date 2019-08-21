'''
loginserver's config file
'''
import os
from configparser import ConfigParser

env = os.environ
#print(env)

conf_file = env['LOGINSERVER_CONF_FILE']
print("conf_file: ", conf_file)

cfg = ConfigParser()
cfg.read(conf_file)
# cfg.get('database','user')
# cfg.getint('server','port')
