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

    def __init__(self, entries, storage, **kwargs):

        invalid_parameters = set(kwargs) - {"start_date", "end_date"}
        if invalid_parameters:
            raise AttributeError('invalid parameter(s): {}'.format(invalid_parameters))

        mappings = dict(
            class_name="label",
            start_date=dict(value=kwargs['start_date']),
            end_date=dict(value=kwargs['end_date']),
            collection_date= None
        )

        super(BDC, self).__init__(entries, mappings, **kwargs)