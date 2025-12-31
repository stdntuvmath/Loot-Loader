import os
import datetime
import json
import requests as req
import numpy as np
import schwab
import traceback
import pyodbc
import regex as re
import pandas as pd
import time
from dateutil.tz import tz
from datetime import date
from datetime import datetime as dt
from datetime import timedelta as td
import datetime
import LLLib_Charles_Schwab as lib
import colorama as corama
import base64
import ast
import schwab
import httpx
import decimal








#binomials

#  x^2 = (x-1)^2 + (2x - 1)

numArray = {1,2,3,4,5,6,7,8,9,10}

# for num in numArray:

#     print(num**2)
#     print((num - 1)**2 + (2*num - 1))





# equation odds

#  x^2 - (x-1)^2 = (2x - 1)

oddNumber = 0
for num in numArray:
    if(num == 1):
        continue

    oddNumber = (num**2 - (num - 1)**2) * (2*num-1)
    print(oddNumber)






