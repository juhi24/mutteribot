# -*- coding: utf-8 -*-
import os
import shutil
import configparser

NAME = 'mutteribot'
HOME = os.path.expanduser('~')
CONF_FILENAME = NAME+'.conf'
CONF_TEMPLATE_PATH = CONF_FILENAME + '.template'
CONFIG_PATH = os.path.join('/etc', CONF_FILENAME)
CONFIG_PATH_USER = os.path.join(HOME, '.'+NAME, CONF_FILENAME)
CONFIG_PATHS = [CONFIG_PATH_USER, CONFIG_PATH]

def ensure_dir(path):
    """Make sure the directory exists. If not, create it including subdirs."""
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def install_config():
    if os.path.isfile(CONFIG_PATH_USER):
        conf_path = CONFIG_PATH_USER
    elif not os.path.isfile(CONFIG_PATH):
        try:
            conf_path = CONFIG_PATH
            shutil.copy(CONF_TEMPLATE_PATH, conf_path)
        except PermissionError as e:
            conf_path = CONFIG_PATH_USER
            if not os.path.isfile(conf_path):
                print('Not installing as root. Installing configuration file to {}.'.format(conf_path))
                ensure_dir(os.path.dirname(conf_path))
                shutil.copy(CONF_TEMPLATE_PATH, conf_path)
    return conf_path

def get_config_path():
    for p in CONFIG_PATHS:
        if os.path.isfile(p):
            return p
    return install_config()

def initialize_config():
    config_path = get_config_path()
    conf = configparser.ConfigParser()
    conf.read(config_path)
    return conf