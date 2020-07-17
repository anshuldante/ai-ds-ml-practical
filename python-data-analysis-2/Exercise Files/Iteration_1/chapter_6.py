import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp


nobels = pd.read_csv('../chapter6/nobels.csv', names=['year','discipline','nobelist'])


nobels.set_index('discipline').sort_index()
nobels.index.nlevels()

nobels.pivot_table