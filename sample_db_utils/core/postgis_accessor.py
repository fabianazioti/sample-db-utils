#
# This file is part of Sample Database Utils.
# Copyright (C) 2019 INPE.
#
# Sample Database Utils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

""" Postgis Acessor Class."""

from sample_db.models import Provenance, Datasets,  Users, make_midias, make_observation
from lccs_db.models import LucClass, db


class PostgisAccessor(object):
    def __init__(self):
        self.sample_classes = []
        self.samples_map_id = {}

    def store_classes(self, classes):
        """
        Utility method to insert multiple sample classes on database
        Args:
            classes (dict[]): list List of classes objects to save
        """
        db.session.bulk_insert_mappings(LucClass, classes)
        db.session.commit()

    def store_observations(self, data_sets, observation_table):
        """
        Stores sample observation into database.
        Args:
            data_sets (dict[]): List of data sets observation to store
        """
        db.engine.execute(
            observation_table.__table__.insert(),
            data_sets
        )
        db.session.commit()

    def load(self):
        """Load sample classes in memory"""
        self.sample_classes = LucClass.filter()
        self.samples_map_id = {}

        for sample in self.sample_classes:
            self.samples_map_id[sample.name] = sample.id