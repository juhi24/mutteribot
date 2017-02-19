#!python
# -*- coding: utf-8 -*-
from os import path
import sys
import config

def install():
    filename = config.NAME + '.service'
    install_path = path.join('/etc/systemd/system', filename)
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, filename), 'r') as f:
        service = f.read()
    service = service.format(working_dir=here, exec_start=sys.executable + ' ' + here)
    with open(install_path, 'w') as f:
        f.write(service)