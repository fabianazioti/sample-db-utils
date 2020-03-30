#
# This file is part of Sample Database Utils.
# Copyright (C) 2019 INPE.
#
# Sample Database Utils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

""" Sample DB Utils Drives Factory"""

from .inSitu import InSitu
from .bdc import BDC


class DriversFactory:
    """Factory for Drives."""

    @staticmethod
    def make(driverType, entries, storager):
        """Factory method for creates datasource."""
        factorys = ["Cerrado", "VMaus", "Canasat", "Lapig", "Fototeca" , "Embrapa", "InSitu", "BDC"]

        assert driverType in factorys

        driver = eval(driverType)(entries, storager)

        return driver