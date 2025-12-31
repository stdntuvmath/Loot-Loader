import os
import sys
import platform
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
import LLLib_Charles_Schwab_2 as lib2
import LLLib_Charles_Schwab_3 as lib3
import colorama as corama
import base64
import ast
import schwab
import httpx
import decimal
from LLLib_Charles_Schwab import Account_Management
from LLLib_Charles_Schwab import Authentication_Management
from schwab.orders.common import Duration, Session
from schwab.orders.common import OrderType, StopType
from schwab.orders.generic import OrderBuilder
from schwab.orders.equities import equity_buy_market


symbol = "AGR"


lib.Database_Management.Delete_Data_From_LootLoaderDataBase.Trading.Delete_the_Last_Trading_Row_For_Symbol("AAOI")




