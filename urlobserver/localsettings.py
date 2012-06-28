# -*- coding: utf-8 -*-
import os

BASEDIR = os.path.dirname(os.path.realpath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin Name', 'admin@email'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASEDIR, 'sqlite.db'),
    }
}
SECRET_KEY = 'iosnrfe1kf!uv*pkmprrijm-k10gb*)3t_hhujl#h4)qdjwt@+'
