# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:04:39 2019

@author: Elmar
"""

import os
import pandas as pd
import numpy as np
from IPython.display import display_html

data_dir_path = "data";
flights_filename_read = os.path.join(data_dir_path, "flights.csv")

columns = ['AIRLINE', 'LATE_AIRCRAFT_DELAY', 'AIRLINE_DELAY']

flights_df_dtypes = {
    columns[0]: np.string_,
    columns[1]: np.object,
    columns[2]: np.object,
}

flights_df = pd.read_csv(flights_filename_read, names=columns, dtype=flights_df_dtypes)
