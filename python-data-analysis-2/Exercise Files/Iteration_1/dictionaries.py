import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp
from dataclasses import dataclass


capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome', 'Spain': 'Madrid'}

print(capitals)

@dataclass
class personclass:
    firstname: str
    lastname: str
    birthday: str = 'unknown'

michele = personclass('Michele', 'Vallisneri')

print(michele)

michele.firstname, michele.lastname, michele.birthday