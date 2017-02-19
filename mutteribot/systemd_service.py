#!python
# -*- coding: utf-8 -*-
from os import path
from mutteribot import config
import shutil

def install():
    filename = config.NAME + '.service'
    install_path = path.join('/etc/systemd/system', filename)
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, filename), 'r') as f:
        service = f.read()
    service = service.format(working_dir=config.HOME, exec_start=shutil.which(config.NAME))
    with open(install_path, 'w') as f:
        f.write(service)