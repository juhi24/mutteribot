# -*- coding: utf-8 -*-
import pandas as pd
from glob import glob
from os import path

DB_DIR = '/var/lib/ilmaruuvi'
FILE_NAMING_SCHEME = '%Y%m%d.csv'


def filepath2dt(filepath):
    filename = path.basename(filepath)
    return pd.datetime.strptime(filename, FILE_NAMING_SCHEME)


def dates():
    fnames = glob(path.join(DB_DIR, '*.csv'))
    dlist = list(map(filepath2dt, fnames))
    dlist.sort()
    return dlist


def latest_filename():
    last_date = dates()[-1]
    return path.join(DB_DIR, last_date.strftime(FILE_NAMING_SCHEME))


def latest_values():
    col_names = ['time', 'temperature', 'rh', 'pressure']
    data = pd.read_csv(latest_filename(), header=None, names=col_names)
    return data.iloc[-1]
