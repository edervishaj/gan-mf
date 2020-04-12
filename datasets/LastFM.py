#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Ervin Dervishaj
@email: vindervishaj@gmail.com
'''

import os
from datasets.DataReader import DataReader

class LastFM(DataReader):
    """
    This class reads/downloads LastFM dataset and provides methods to access 3 sparse
    matrices URM_train, URM_validation, URM_test or create cross-validation folds from
    the full URM.
    """

    DATASET_NAME = 'LastFM'

    url = 'http://files.grouplens.org/datasets/hetrec2011/hetrec2011-lastfm-2k.zip'
    dataset_dir = 'hetrec2011-lastfm-2k'
    data_file = 'user_artists.dat'

    def __init__(self, split=True, **kwargs):
        """
        Constructor

        Parameters
        ----------
        kwargs:
            Keyword arguments that go into the constructor of the superclass constructor
        """

        super(LastFM, self).__init__(delim='\t', header=True, **kwargs)
        self.process(split)