# This file is part of Sample Database Utils.
# Copyright (C) 2019 INPE.
#
# Sample Database Utils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

""" Brazil Data Cube Class."""

from ..core.driver import Shapefile

class BDC(Shapefile):
    """Driver for data loading to `sampledb`"""

    def __init__(self, entries, storager, **kwargs):

        mappings = dict(
            class_name="label",
            start_date=dict(value='31/08/2019'),
            end_date=dict(value='01/09/2018'),
            collection_date= None
        )

        super(BDC, self).__init__(entries, mappings, storager, **kwargs)

