#
# This file is part of Sample Database Utils.
# Copyright (C) 2019 INPE.
#
# Sample Database Utils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Sample Database Utils Exemple"""

import os
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('../'))

#pylint: disable=wrong-import-position

from sample_db_utils.core.postgis_accessor import PostgisAccessor
from lccs_db.models import LucClassificationSystem, db
from lccs_db.cli import create_app

from examples.inSitu import InSitu
from flask import Flask

storager = PostgisAccessor()

samples = [
    {
        'authority_name': 'insitu',
        'name': 'InSitu',
        'description': 'InSitu\'s sample in R',
        'version': '0.1.0',
        'sample': [
            InSitu('/data/inSitu', storager=storager)
        ]
    }
]

if __name__ == '__main__':
    # Initialize SQLAlchemy Models
    # uri = os.environ.get('SQLALCHEMY_URI', 'postgresql://postgres:12345@localhost:5432/geodatabase')

    user = "1"

    create_app()



    # app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/geodatabase'
    #
    # db
    for sample in samples:
        try:
            luc_system = LucClassificationSystem.get(name=sample['name'])
        except BaseException:
            luc_system = LucClassificationSystem()
            luc_system.authority_name = sample['authority_name']
            luc_system.description = sample['description']
            luc_system.system_name = sample['name']
            luc_system.system_name = sample['version']
            luc_system.save()
