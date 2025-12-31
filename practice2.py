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
from LLLib_Charles_Schwab import Account_Management
from LLLib_Charles_Schwab import Authentication_Management
from schwab.orders.common import Duration, Session
from schwab.orders.common import OrderType, StopType
from schwab.orders.generic import OrderBuilder
from schwab.orders.equities import equity_buy_market



lib.Database_Management.Delete_Data_From_LootLoaderDataBase.Historical.Delete_All_HistoricalData_For_OneSymbol("API")