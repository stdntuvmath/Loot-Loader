

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


# lib.Database_Management.Delete_Data_From_LootLoaderDataBase.Delete_All_HistoricalData_For_OneSymbol("AA")
# time.sleep(2)

#lib.Database_Management.Create_Delete_Tables.Create_Tables.Create_Historical_Table_By_Name("a_historical")



def accountBalance_Test():

    accountBalance = lib.Account_Management.Get_Account_Balance_Available_For_Trading()
    print(accountBalance)


def calc_numberOfShares_test():

    #closePrice = 

    numberOfShares = lib.Calculation_Management.Calculate_Share_Amount(closePrice, accountBalance)


def hlev_Testing():


    symbol = "A"

    todaysDate = "2024-11-04"

    closePrice = 145.17

    tday = datetime.datetime.today()
    start = tday - datetime.timedelta(days=30)
    end = tday - datetime.timedelta(days=26)

    #lib.Database_Management.Delete_Data_From_LootLoaderDataBase.Delete_All_HistoricalData_For_OneSymbol(symbol)

    # stuff = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Get_Previous_200_EMA200Angles_from_DB(symbol)
    # print(len(stuff))

    # hlev = lib.Calculation_Management.Calculate_HLEVs(symbol, closePrice, todaysDate)
    # print(hlev)
    closePriceArray = []


    candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,start,end)))

    print(candle_data)


    if("bad request" in candle_data):
        print(candle_data)

    for candle in candle_data['candles']:

        #take their epoch time and turn it into current local time

        t = candle.get('datetime')
        t = int(str(t)[:-3])#take last 3 digits off
        charlesSchwabTime = datetime.datetime.fromtimestamp(t).strftime('%X')
        charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
        #localDate = datetime.date.strftime(localDate, "%Y-%m-%d")

        closePrice = candle.get('close')
        #highPrice = candle.get("high")
        #lowPrice = candle.get("low")
        closePriceArray.append(closePrice)

    monthlyHigh = max(closePriceArray)
    monthlyLow = min(closePriceArray)
    monthlyDistance = monthlyHigh - monthlyLow

    monthlyMiddle = monthlyLow + monthlyDistance/2

    if(monthlyMiddle == monthlyLow):
        percentage = 987654321
    if(monthlyMiddle != monthlyLow):
        percentage = (closePrice - monthlyMiddle)/(monthlyMiddle - monthlyLow)

    print("monthly high: "+str(monthlyHigh))
    print()
    print("monthly middle: "+str(monthlyMiddle))
    print()
    print("monthly low: "+str(monthlyLow))
    print()
    print()
    print("percentage: "+str(percentage))
    print()


def mimic_CharSchwabs_HLEV_Origin():

    os.system("CLS")

    daysToCount = 200
    daees = 30

    #first mimic the monthlyhigh

    symbol = "A"
    tday = datetime.datetime.today()
    start = tday - datetime.timedelta(days=daysToCount)

    minute_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Minute_Data_from_Schwab(symbol,start,tday)))
    daily_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,start,tday)))

    dailyClosePriceArray = []
    dateArray = []
    
    for candle in daily_candle_data['candles']:

        dailyClosePrice = candle.get('close') 

        t = candle.get('datetime')
        t = int(str(t)[:-3])#take last 3 digits off
        charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
        

        dailyClosePriceArray.append(dailyClosePrice)
        dateArray.append(datetime.datetime.strptime(charlesSchwabDate, "%Y-%m-%d").date())


    print()
    print("Processing data...")
    print()
    print()

           


    prices_for_last_30_days = []

    for i, close_date in enumerate(dateArray):
        
        startDate = close_date - datetime.timedelta(days=daees) 



        if startDate <= close_date:
            prices_for_last_30_days.append(dailyClosePriceArray[i])
    


        monthlyHigh =  lib.Calculation_Management.round(max(prices_for_last_30_days), 2)
        
        monthlyLow =  lib.Calculation_Management.round(min(prices_for_last_30_days), 2)

        origin = lib.Calculation_Management.round(monthlyLow + (monthlyHigh - monthlyLow)/2, 2)


        hlevs = str(close_date), monthlyHigh, origin, monthlyLow
        fileLabel = "{}_mimic_CharSchwabs_HLEV_Origin(daysToCount={},days={})".format(symbol, daysToCount, daees)
        lib.Logging.test(fileLabel, hlevs)


        if(len(prices_for_last_30_days) == 30):
            prices_for_last_30_days.remove(prices_for_last_30_days[0])

    print("Done.")
    print()
    

def CharSchwabs_HLEVs():

    os.system("CLS")

    daysToCount = 200
    daees = 30

    #first mimic the monthlyhigh

    symbol = "A"
    tday = datetime.datetime.today()
    start = tday - datetime.timedelta(days=daysToCount)

    minute_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Minute_Data_from_Schwab(symbol,start,tday)))
    daily_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,start,tday)))

    dailyClosePriceArray = []
    dateArray = []
    
    for candle in daily_candle_data['candles']:

        dailyClosePrice = candle.get('close') 

        t = candle.get('datetime')
        t = int(str(t)[:-3])#take last 3 digits off
        charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
        

        dailyClosePriceArray.append(dailyClosePrice)
        dateArray.append(datetime.datetime.strptime(charlesSchwabDate, "%Y-%m-%d").date())


    print()
    print("Processing data...")
    print()
    print()

           


    prices_for_last_30_days = []

    for i, close_date in enumerate(dateArray):
        
        startDate = close_date - datetime.timedelta(days=daees) 



        if startDate <= close_date:
            prices_for_last_30_days.append(dailyClosePriceArray[i])
    


        monthlyHigh =  lib.Calculation_Management.round(max(prices_for_last_30_days), 2)
        
        monthlyLow =  lib.Calculation_Management.round(min(prices_for_last_30_days), 2)

        #origin = lib.Calculation_Management.round(monthlyLow + (monthlyHigh - monthlyLow)/2, 2)


        hlevs = lib.Calculation_Management.Calculate_HLEVs(symbol, 9.99, monthlyHigh, monthlyLow, 99.99, 999.99)


        #hlevs = str(close_date), monthlyHigh, origin, monthlyLow
        fileLabel = "{}_CharSchwabs_HLEVs(daysToCount={},days={})".format(symbol, daysToCount, daees)
        lib.Logging.test(fileLabel, hlevs)


        if(len(prices_for_last_30_days) == 30):
            prices_for_last_30_days.remove(prices_for_last_30_days[0])

    print("Done.")
    print()
  

def orderID_Testing():

    startDate = "2024-11-04"

    closePrice = 145.17

    tday = datetime.datetime.today()
    start = tday - datetime.timedelta(days=30)
    end = tday - datetime.timedelta(days=26)


    # tradeID = lib.Trading_Management.Initiate_Sell_at_MarketValue("ARBB",1)
    # print(tradeID)

    accountHash = lib.Account_Management.Get_Account_Hash()

    #print(accountHash)

    auth = lib.Authentication_Management.Schwab_Wrapper_Authentication.Get_Schwab_Account_Authorization()

    transactions = auth.get_transactions(accountHash)

    stuff = json.dumps(transactions.json(), indent=4)

    f = open('test_OrderID1.json', "w")
    f.write(stuff)
    f.close()

    f = open('test_OrderID1.json')
    jsonString = json.dumps(json.load(f))
    f.close()

    jsonDictionary = json.loads(jsonString)

    for i in jsonDictionary:



        if('1002459335901' in i):

        #take their epoch time and turn it into current local time
        # if(i['orderID'] == 1002459335901):
        #     print(i['orderID'])
        # closePrice = candle.get('close')
        # highPrice = candle.get("high")
        # lowPrice = candle.get("low")
        # volume = candle.get("volume")
            print(i)


def GetHighestFromDB():

    symbol = "A"
    tday = datetime.datetime.today()
    todaysDate = tday.date()
    yesterdaysDate = todaysDate - datetime.timedelta(days=1)

    try:
        #we need to get a list of final daily close prices for the last 30 days


        #then we need to find the highest out of that list

        dateArray = []
        #parse todaysDate
        dateArray = str(todaysDate).split("-")

        todaysDate = datetime.date(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]))

        previousDate = todaysDate - datetime.timedelta(days=30)
        nTime = "14:59"

        connection = lib.Database_Management.Create_My_Connection()
        mycursor = connection.cursor()

        mycursor.execute("SELECT MAX(ClosePrice) FROM lootloaderdatabase.{}_historical WHERE(nDate BETWEEN '{}' AND '{}') AND nTime='{}' LIMIT 1".format(symbol,previousDate,yesterdaysDate, nTime))

        HighPrice = str(mycursor.fetchall())
        HighPrice = HighPrice.replace("[","")
        HighPrice = HighPrice.replace("]","")
        HighPrice = HighPrice.replace("(","")
        HighPrice = HighPrice.replace(")","")
        HighPrice = HighPrice.replace(",","")
        HighPrice = HighPrice.replace(" ","")
        mycursor.close()


        #print("'"+HighPrice+"'")
        #print(type(HighPrice))

        if(HighPrice == "None"):
            return float("0.00")

        if(HighPrice != "None"):
            print(HighPrice)
            return float(HighPrice)


    
    except:
        error = traceback.format_exc()                                       
        lib.Logging.error(error)


def monthlyHigh_monthlyLow_Origin():  

    symbol = "A"
    tday = datetime.datetime.today()
    minutestart = tday - datetime.timedelta(days=31)
    dailyStart = tday - datetime.timedelta(days=200)
    dailyClosePriceArray = []
    minuteClosePriceArray = []
    dailyDateArray = []


    daily_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,dailyStart,tday)))
    messageArray = []
    
    os.system("CLS")
    print("Processing...")

    dailyClosePriceArray = []
    dateArray = []

    for candle in daily_candle_data['candles']:

        dailyClosePrice = candle.get('close')

        #take their epoch time and turn it into current local time
        #-------------------------------------------------------------------------
        t = candle.get('datetime')
        t = int(str(t)[:-3])#take last 3 digits off
        #charlesSchwabTime = datetime.datetime.fromtimestamp(t).strftime('%X')
        charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")    
        #-------------------------------------------------------------------------

    #     message = charlesSchwabDate, dailyClosePrice
    #     messageArray.append(message)


    # messageArray = messageArray[:-1]

   
        dailyClosePriceArray.append(dailyClosePrice)
        dateArray.append(datetime.datetime.strptime(charlesSchwabDate, "%Y-%m-%d").date())



        prices_for_last_30_days = []

        for i, close_date in enumerate(dateArray):
            
            startDate = close_date - datetime.timedelta(days=30) 



            if startDate <= close_date:
                prices_for_last_30_days.append(dailyClosePriceArray[i])
        


            monthlyHigh =  lib.Calculation_Management.round(max(prices_for_last_30_days), 2)
            
            monthlyLow =  lib.Calculation_Management.round(min(prices_for_last_30_days), 2)
    

            hlevOrigin = monthlyLow + (monthlyHigh - monthlyLow)/2
            
            messageArray = monthlyHigh, hlevOrigin, monthlyLow

            fileLabel = "{}_dailyHistorical_Check".format(symbol)

            lib.Logging.test(fileLabel, messageArray)


    print()
    print("Done.")
    print() 



def Match_HighLow_Data_Test():


    symbol = "A"
    tday = datetime.datetime.today()
    todaysDate = tday.date()
    yesterdaysDate = tday - datetime.timedelta(days=10)#around 2000 stock market minutes

    try:
       # get close day data from schwab
       dayData = lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol, tday, yesterdaysDate)
       print(dayData)

    
    except:
        error = traceback.format_exc()                                       
        lib.Logging.error(error)


def Insert_Into_Trading_DB_Test():
    symbol = "A"
    localDate = "2024-12-26"
    localTime = "14:32"
    accountBalance = 1919564236.32
    lookingForBuy = 1
    alreadyBought = 1
    lookingForSell = 1
    alreadySold = 1
    orderType = "BUY" 
    closePrice = 1.23
    numberOfShares = 1
    riskAmount = 1
    Profit_or_Loss = 1919564236.32
    roi = 99.999999
    Good_Bad_Trade = "GOOD"
    orderID =  123456789321654987
    rowID = 1


    lib.Database_Management.Give_Data_To_LootLoaderDataBase.Give_TradeData_To_DB(symbol, localDate, localTime, accountBalance, lookingForBuy, alreadyBought, lookingForSell, alreadySold, orderType, 
                                        closePrice, numberOfShares, riskAmount, Profit_or_Loss, roi, Good_Bad_Trade, orderID, 
                                        rowID)


def Get_Last_Row_of_Trading_Tables_test():
    symbol = "A"
    lastTradingRow = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Trading_Tables(symbol)
    print(lastTradingRow)


def dailyHistorical_Check():
    #I need to find a way to do everything in the first for loop 


    symbol = "A"
    tday = datetime.datetime.today()
    minutestart = tday - datetime.timedelta(days=31)
    dailyStart = tday - datetime.timedelta(days=200)
    dailyClosePriceArray = []
    minuteClosePriceArray = []
    dailyDateArray = []


    daily_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,dailyStart,tday)))
    messageArray = []
    
    os.system("CLS")
    print("Processing...")

    for candle in daily_candle_data['candles']:

        dailyClosePrice = candle.get('close')

        #take their epoch time and turn it into current local time
        #-------------------------------------------------------------------------
        t = candle.get('datetime')
        t = int(str(t)[:-3])#take last 3 digits off
        #charlesSchwabTime = datetime.datetime.fromtimestamp(t).strftime('%X')
        charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")    
        #-------------------------------------------------------------------------

        message = charlesSchwabDate, dailyClosePrice
        messageArray.append(message)


    messageArray = messageArray[:-1]

    stuff = 200

    

        
    for item in messageArray:


        fileLabel = "{}_dailyHistorical_Check_{}".format(symbol, stuff)

        lib.Logging.test(fileLabel, item)


    print()
    print("Done.")
    print()


def print_HistoricalMinute_to_File(symbol):

    tday = datetime.datetime.today()
    start = tday - datetime.timedelta(days=100)

    minute_candle_data = lib.Pull_From_Schwab_Management.Get_Historical_Minute_Data_from_Schwab(symbol,start,tday)

    fileLabel = "{}_historicalChecking_test".format(symbol)
    lib.Logging.test(fileLabel, minute_candle_data)


def lookingForBuy_Test(symbol):

    tday = datetime.datetime.today()
    todaysDate = str(tday.date())
    now = tday.time()

    array = []

    difference = 90

    newestRow = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Historical_Tables(symbol)
    #print(newestRow)


    # dBdate = str(newestRow[1]).replace(" '","")
    # dBdate = dBdate.replace("'","")
    # dBdate = dBdate.replace(" ","")

    # time = str(newestRow[2]).replace(" '","")
    # time = time.replace("'","")
    # time = time.replace(" ","")
    

    # time = datetime.datetime.strptime(time, '%H:%M:%S')

    # hour = now.replace(hour=1, minute=00, second=0)
    # thirtyMins = now.replace(hour=00, minute=30, second=0)
    # fifteenMins = now.replace(hour=00, minute=15, second=0)

    # # halfHourAgo = datetime.datetime.combine(date.min, now) - datetime.datetime.combine(date.min,thirtyMins)
    # # halfHourAgo = str(halfHourAgo)
    # # halfHourAgo = datetime.datetime.strptime(halfHourAgo, '%H:%M:%S')

    # # fifteenMinsAgo = datetime.datetime.combine(date.min, now) - datetime.datetime.combine(date.min,fifteenMins)
    # # fifteenMinsAgo = str(fifteenMinsAgo)
    # # fifteenMinsAgo = datetime.datetime.strptime(fifteenMinsAgo, '%H:%M:%S')

    # hourAgo = datetime.datetime.combine(date.min, now) - datetime.datetime.combine(date.min,hour)
    # hourAgo = str(hourAgo)
    # hourAgo = datetime.datetime.strptime(hourAgo, '%H:%M:%S')


    newestIndex = int(newestRow[31])

    index = newestIndex - difference

    
    while(index <= newestIndex):
        #print(index)

        newestRow = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Row_By_Index(symbol, index)
        previousRow = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Row_By_Index(symbol, index-1)
        #print(newestRow)
        if(newestRow == "" or previousRow == ""):

            newestAngle = 0
            previousAngle = 0
            newest_StdDev2 = 0
            previous_StdDev2 = 0
            newest_StdDev3 = 0
            previous_StdDev3 = 0

            avgStdDev10 = 0
            StdDev10 = 0
            hlev_percentage = 0
            ema200_value = 0
            hlev2000_UpperArm = 0
            hlevOrigin = 0

            dBdate = todaysDate
            time = now
        else:
            #print("in here")
            newestAngle = float(newestRow[8])
            previousAngle = float(previousRow[8])
            newest_NegStdDev2 = float(newestRow[20])
            previous_NegStdDev2 = float(newestRow[20])
            newest_NegStdDev3 = float(newestRow[21])
            previous_NegStdDev3 = float(previousRow[21])

            avgStdDev10 = float(newestRow[29])
            StdDev10 = float(newestRow[18])
            hlev_percentage = float(newestRow[32])
            ema200_value = float(newestRow[7])
            hlev2000_UpperArm = float(newestRow[33])
            hlev2000_LowerArm = float(newestRow[35])
            hlevOrigin = float(newestRow[30])



            dBdate = str(newestRow[1]).replace(" '","")
            dBdate = dBdate.replace("'","")
            dBdate = dBdate.replace(" ","")

            time = str(newestRow[2]).replace(" '","")
            time = time.replace("'","")
            time = time.replace(" ","")

            time = datetime.datetime.strptime(time, '%H:%M:%S')


            index = index + 1

            #ema200Angle crosses above NegstdDev3 or ema200Angle crosses above NegstdDev2
            if((previousAngle < previous_NegStdDev3 and newestAngle > newest_NegStdDev3) or (previousAngle < previous_NegStdDev2 and newestAngle > newest_NegStdDev2)): #emaAngle crosses above stdDev3 on todays date
                #and avgStdDev10 < stdDev10
                if(avgStdDev10 < StdDev10):

                    if(hlev_percentage <= -1):

                        if(hlev2000_UpperArm < hlevOrigin):

                            if(ema200_value < hlev2000_LowerArm):

                                print("true "+str(dBdate)+" "+str(time))
                                localDate = dBdate
                                localTime = time                        
                                lookingForBuy = 1
                                alreadyBought = 0
                                lookingForSell = 0
                                alreadySold = 0
                                orderType = "LKFB"                                                              
                                Profit_or_Loss = 0.00
                                roi = 0.00
                                Good_Bad_Trade = "NA"
                                orderID = 0
                                riskAmount = 0
                                #rowID = int(lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Trading_Tables(symbol)[16])+1

                                incomeTaxesDue = 0
                                sellPrice = 0
                                # lib.Database_Management.Give_Data_To_LootLoaderDataBase.Give_TradeData_To_DB(symbol, localDate, localTime, accountBalance, 
                                #                                                                         lookingForBuy, alreadyBought, lookingForSell, 
                                #                                                                         alreadySold, orderType, closePrice, numberOfShares, 
                                #                                                                         riskAmount, Profit_or_Loss, roi, incomeTaxesDue, buyPrice, sellPrice,Good_Bad_Trade, 
                                #                                                                         orderID, rowID)
                                # #-------------

                                fileLabel = "{}_lookForBuyTest".format(symbol)
                                
                                
                                time = str(time).replace("1900-01-01 ","")
                                message = True, dBdate, time
                                print(message)
                                lib.Logging.test(fileLabel, message)
                                array.append(True)              
                                array.append(dBdate) 
                                            
                                array.append(time) 
                                return array

        
    else:

        array.append(False)              
        array.append(dBdate) 
        fileLabel = "{}_lookForBuyTest".format(symbol)
                        
                        
        time = str(time).replace("1900-01-01 ","")
        message = False, dBdate, time
        print(message)
        lib.Logging.test(fileLabel, message)             
        array.append(str(time)) 
        return array


def getting_HLEVs_in_DataLoader(numberOfSymbols):

    try:
        os.system("CLS")
        dayOfWeek = lib.Date_Time_Management.Get_Todays_Weekday_Name()
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        now = tday.time()
        

        print("Opening DataLoader...")
        print()
            
        message = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\f"+str(now)+" - BEGIN DATALOADER\r\f"
        lib.Logging.info(message)
    
        allSymbols = ""
        allSymbols = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Symbol_List()
        lastRowData = []
        updateArray = []
        hlevs = []
        DB_Date = ""
        previousEma200Value=0
        counter_ofSymbols=0
        newEma200Value=0
        newEMA200AngleValue = 0
        counter_ofAnglePoints = 0
        counter_ofDataPoints = 0
        buyPrice = 0
        sellPrice = 0
        dataInserted = False
        previousEMA200AngleValue=0
        previousEma200Value=0
        previousEma3900Value=0
        previousVariance10Value=0
        newVariance10Value=0
        origin = 0
        rowID = 1
        n=0
        wholeCycleOccurred = False

        standardDev=0
        shareAmount=0
        goodTradeArray=[]
        badTradeArray=[]
        ema200AngleArray = []
        EMA200Array = []
        
        stdDevArray=[]
        variance10Array=[]
        okToBuy = True
        okToSell = False
        dayOfWeek = ""
        closeDate = ""
        closeTime = ""
        startTime = now.replace(hour=8, minute=00, second=0)
        endTime = now.replace(hour=23, minute=59, second=0)

        #time.sleep(1)#pause between symbol list iterations

        previousEma200Value = 0
        previousStdDev10 = 0
        newEma200Value = 0
        newEMA200AngleValue = 0
        newStdDevAvg10 = 0

        hlevOrigin = 0.0
        hlevPercentage = 0.0
        hlev2000_UpperArm = 0.0
        hlev2000_MiddleArm = 0.0
        hlev2000_LowerArm = 0.0

        counter_ofSymbols = 1

        ema200AngleArray.clear()
        EMA200Array.clear()
        #jclosePriceArray.clear()
        stdDevArray.clear()

        while(startTime <= now and now <= endTime):

            counter_ofSymbols=1           

            for symbol in allSymbols: 

                time.sleep(0.25)             


                if(lib.Database_Management.Check_LootLoaderDataBase.Check_If_Table_Exists_in_LLDB("lootloaderdatabase","{}_historical".format(symbol))):

                    #we must reformulate todays data by deleting the previous historical data
                    # and recalculating everything during stock market hours                    
                    if(dayOfWeek != "Saturday" and dayOfWeek != "Sunday"):

                        lib.Database_Management.Delete_Data_From_LootLoaderDataBase.Historical.Delete_Todays_Data_Only_for_Symbol(symbol)
                    
                    if(counter_ofSymbols <= numberOfSymbols):
                
                        todaysDay = lib.Date_Time_Management.Get_Todays_Weekday_Name()
                        tday = datetime.datetime.today()
                        todaysDate = tday.date()
                        now = tday.time()
                        


                        lastRowData = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Historical_Tables(symbol)


                        #------------------------------- #IF NO DATA IS THERE Minute data
                        if(lastRowData == None):
                    
                            tday = datetime.datetime.today()
                            start = tday - datetime.timedelta(days=200)


                            minute_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Minute_Data_from_Schwab(symbol,start,tday)))

                            daily_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,start,tday)))

                        

                            dailyClosePriceArray = []
                            dateArray = [] 
                            prices_for_last_30_days = []
                            hlevArray = []
                            closePriceArray = []
                            standardDev10Array = []


                            for candle in daily_candle_data['candles']:

                                dailyClosePrice = candle.get('close') 

                                #begin the hlev process by storing the closePrices in an array
                                #and getting the highest and lowest weekly closePrice

                                t = candle.get('datetime')
                                t = int(str(t)[:-3])#take last 3 digits off
                                charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
                                

                                dailyClosePriceArray.append(dailyClosePrice)
                                dateArray.append(datetime.datetime.strptime(charlesSchwabDate, "%Y-%m-%d").date())

                                
                            dailyClosePriceArray = dailyClosePriceArray[:-1]
                            dateArray = dateArray[:-1]



                            for i, close_date in enumerate(dateArray):
                                
                                startDate = close_date - datetime.timedelta(days=30) 



                                if startDate <= close_date:
                                    prices_for_last_30_days.append(dailyClosePriceArray[i])



                                monthlyHigh =  lib.Calculation_Management.round(max(prices_for_last_30_days), 2)
                                
                                monthlyLow =  lib.Calculation_Management.round(min(prices_for_last_30_days), 2)


                                hlevs = str(close_date), monthlyHigh, monthlyLow
                                hlevArray.append(hlevs)

                                #print(hlevArray)

                                if(len(prices_for_last_30_days) == 30):
                                    prices_for_last_30_days.remove(prices_for_last_30_days[0])








                            print("Processing data...")

                            for candle in minute_candle_data['candles']:

                                #take their epoch time and turn it into current local time

                                t = candle.get('datetime')
                                t = int(str(t)[:-3])#take last 3 digits off
                                charlesSchwabTime = datetime.datetime.fromtimestamp(t).strftime('%X')
                                charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
                                #localDate = datetime.date.strftime(localDate, "%Y-%m-%d")

                                closePrice = candle.get('close')
                                highPrice = candle.get("high")
                                lowPrice = candle.get("low")
                                volume = candle.get("volume")


                                if(len(closePriceArray) <= 2000):

                                    closePriceArray.append(closePrice)
                                    highestWeeklyClosePrice = max(closePriceArray)
                                    lowestWeeklyClosePrice = min(closePriceArray)

                                if(len(closePriceArray) > 2000):

                                    closePriceArray.remove(closePriceArray[0])



                                #this starts the beginning ema value really 
                                #close to what it currently is instead of zero
                                #----------------------------------
                                if(rowID == 1):
                                    previousEma200Value = closePrice
                                #----------------------------------

                                newEma200Value = lib.Calculation_Management.Calculate_NewestEMA200_Method(previousEma200Value,closePrice)

                                EMA200Array.append(newEma200Value)

                                if(len(EMA200Array) > 200):
                                    EMA200Array.remove(EMA200Array[0])

                                                        
                                newEMA200AngleValue = lib.Calculation_Management.CalculateAngle(newEma200Value, previousEma200Value)


                            
                                ema200AngleArray.append(newEMA200AngleValue)

                                if(len(ema200AngleArray) > 200):
                                    ema200AngleArray.remove(ema200AngleArray[0])                                    
                                    standardDev = lib.Calculation_Management.Calculate_Standard_Dev_of_Angle_of_EMA200(ema200AngleArray)


                                    
                                stdDevArray.append(standardDev)

                                if(len(stdDevArray)>2):
                                    stdDevArray.remove(stdDevArray[0])



                                standardDev2 = standardDev*2
                                standardDev3 = standardDev*3
                                standardDev4 = standardDev*4
                                standardDev5 = standardDev*5
                                standardDev6 = standardDev*6
                                standardDev7 = standardDev*7
                                standardDev8 = standardDev*8
                                standardDev9 = standardDev*9
                                standardDev10 = standardDev*10

                                standardDev10Array.append(standardDev10)
                                newStdDev10 = 0
                                if(len(standardDev10Array) > 200):
                                    standardDev10Array.remove(standardDev10Array[0])                                    
                                    #calc avg of stdDev10
                                    newStdDev10 = lib.Calculation_Management.Calculate_stdDev10Avg(standardDev10Array)
                                # if(len(standardDev10Array)>2):
                                #     standardDev10Array.remove(standardDev10Array[0])

                                negStandardDev = standardDev*-1
                                negStandardDev2 = standardDev*-2
                                negStandardDev3 = standardDev*-3
                                negStandardDev4 = standardDev*-4
                                negStandardDev5 = standardDev*-5
                                negStandardDev6 = standardDev*-6
                                negStandardDev7 = standardDev*-7
                                negStandardDev8 = standardDev*-8
                                negStandardDev9 = standardDev*-9
                                negStandardDev10 = standardDev*-10                
                                


                                hlevOrigin = 0

                                hlevPercentage = 0

                                hlev2000_UpperArm = 0

                                hlev2000_MiddleArm = 0

                                hlev2000_LowerArm = 0

                                for hlv in hlevArray:
                                    highestMonthlyClosePrice = 0
                                    lowestMonthlyClosePrice = 0

                                    if(str(charlesSchwabDate) == str(hlv[0])):

                                        highestMonthlyClosePrice = float(hlv[1])
                                        lowestMonthlyClosePrice = float(hlv[2])





                                        #calc and get hlev
                                        #---------------------------------------------------------------
                                        Hlevs = lib.Calculation_Management.Calculate_HLEVs(symbol, closePrice, highestMonthlyClosePrice, lowestMonthlyClosePrice, highestWeeklyClosePrice,lowestWeeklyClosePrice)
                                        # print(Hlevs)
                                        # if(Hlevs is None):

                                        #     continue

                                        hlevOrigin = Hlevs[0]

                                        hlevPercentage = Hlevs[1]

                                        hlev2000_UpperArm = Hlevs[2]

                                        hlev2000_MiddleArm = Hlevs[3]

                                        hlev2000_LowerArm = Hlevs[4]

                                    if(str(charlesSchwabDate) == str(todaysDate)):

                                        highestMonthlyClosePrice = lib.Calculation_Management.round(float(hlv[1]),2)
                                        lowestMonthlyClosePrice = lib.Calculation_Management.round(float(hlv[2]),2)

                                        #calc and get hlev
                                        #---------------------------------------------------------------
                                        Hlevs = lib.Calculation_Management.Calculate_HLEVs(symbol, closePrice, highestMonthlyClosePrice, lowestMonthlyClosePrice, highestWeeklyClosePrice,lowestWeeklyClosePrice)
                                        # print(Hlevs)
                                        # if(Hlevs is None):

                                        #     continue

                                        hlevOrigin = Hlevs[0]

                                        hlevPercentage = Hlevs[1]

                                        hlev2000_UpperArm = Hlevs[2]

                                        hlev2000_MiddleArm = Hlevs[3]

                                        hlev2000_LowerArm = Hlevs[4]

                                newEma200FaceValue = lib.Calculation_Management.round(newEma200Value,2)
                                
                                lib.Database_Management.Give_Data_To_LootLoaderDataBase.Give_HistoricalData_To_DB(symbol, charlesSchwabDate, charlesSchwabTime, 
                                                                                                                            closePrice, highPrice, lowPrice, volume, newEma200FaceValue, 
                                                                                                                            newEMA200AngleValue, standardDev, 
                                                                                                                            standardDev2, standardDev3, standardDev4, 
                                                                                                                            standardDev5, standardDev6, standardDev7, 
                                                                                                                            standardDev8, standardDev9, standardDev10,
                                                                                                                            negStandardDev, negStandardDev2, negStandardDev3,
                                                                                                                            negStandardDev4, negStandardDev5, negStandardDev6,
                                                                                                                            negStandardDev7, negStandardDev8, negStandardDev9,
                                                                                                                            negStandardDev10, newStdDev10, hlevOrigin, rowID,
                                                                                                                            hlevPercentage, hlev2000_UpperArm, hlev2000_MiddleArm, hlev2000_LowerArm)
                                counter_ofAnglePoints+=1

                                previousEma200Value = newEma200Value
                                previousStdDev10 = newStdDev10
                                rowID +=1
                                            
                            
                            closePrice = None
                            highPrice = None
                            lowPrice = None
                            volume = None
                            previousEma200Value = 0
                            newEma200Value = 0
                            newEMA200AngleValue = 0
                            
                            counter_ofDataPoints+=1
                            rowID = 1
                            print("Done.")
                            tableName = "{}_historical".format(symbol)
                                                    
                            recordCount = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Total_Amount_of_Records_InTable(tableName)
                            
                            message = "{} of {}. {} - Backfill to present with {} records stored.".format(counter_ofSymbols, numberOfSymbols,symbol, recordCount)+"\r\f"
                            print(message)
                            lib.Logging.info(message) 

                            #lib.Database_Management.Create_Delete_Tables.Delete_Tables.Purge_SymbolsTable_of_LowData_Symbols(symbol)
                            #continue



                        #-------------------------------if Minute data exists

                        if(lastRowData != None):

                            #GET last database DATE

                            dailyClosePriceArray = []
                            dateArray = [] 
                            prices_for_last_30_days = []
                            hlevArray = []
                            closePriceArray = []
                            standardDev10Array = []

                            DB_Date = str(lastRowData[1])
                            DB_Time = str(lastRowData[2])
                            DB_DateTime = [DB_Date, DB_Time]
                            epoch_DB_DateTime = lib.Date_Time_Management.Convert_GivenDateTime_to_EpochTime(DB_DateTime)


                            print("{} of {}. Backfilling from specified date ".format(counter_ofSymbols, numberOfSymbols)+str(DB_Date)+" - "+str(DB_Time)+" for: {}\r\f".format(symbol))

                            message = "{} of {}. Backfilling from specified date ".format(counter_ofSymbols, numberOfSymbols)+str(DB_Date)+" - "+str(DB_Time)+" for: {}\r\f".format(symbol)
                            lib.Logging.info(message) 
                            

                            rowID = lastRowData[31]
                            rowID = int(rowID)+1



                            tday = datetime.datetime.today()
                            start = tday - datetime.timedelta(days=200)
                            #start = datetime.datetime.strptime(DB_Date, "%Y-%m-%d")


                            minuteCandle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Minute_Data_from_Schwab(symbol,start,tday)))
                            daily_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,start,tday)))


                            dailyClosePriceArray = []
                            dateArray = [] 
                            prices_for_last_30_days = []
                            hlevArray = []  
                            Hlevs = []
                            standardDev10Array = []                                

                            message = "{} of {}. Adding records for... {}\r\f".format(counter_ofSymbols, numberOfSymbols, symbol)
                            print(message)
                            lib.Logging.info(message)

                            for candle in daily_candle_data['candles']:

                                dailyClosePrice = candle.get('close') 

                                #begin the hlev process by storing the closePrices in an array
                                #and getting the highest and lowest weekly closePrice

                                t = candle.get('datetime')
                                t = int(str(t)[:-3])#take last 3 digits off
                                charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
                                

                                dailyClosePriceArray.append(dailyClosePrice)
                                dateArray.append(datetime.datetime.strptime(charlesSchwabDate, "%Y-%m-%d").date())


                            

                            for i, close_date in enumerate(dateArray):
                                
                                startDate = close_date - datetime.timedelta(days=30) 



                                if startDate <= close_date:
                                    prices_for_last_30_days.append(dailyClosePriceArray[i])
                            


                                monthlyHigh =  lib.Calculation_Management.round(max(prices_for_last_30_days), 2)
                                
                                monthlyLow =  lib.Calculation_Management.round(min(prices_for_last_30_days), 2)

                                #origin = lib.Calculation_Management.round(monthlyLow + (monthlyHigh - monthlyLow)/2, 2)


                                #hlevs = str(close_date), monthlyHigh, origin, monthlyLow

                                hlevs = str(close_date), monthlyHigh, monthlyLow
                                hlevArray.append(hlevs)

                                if(len(prices_for_last_30_days) == 30):
                                    prices_for_last_30_days.remove(prices_for_last_30_days[0])



                            prCounter = 0

                            for candle in minuteCandle_data['candles']:

                                Hlevs = []
                                highestWeeklyClosePrice = 0
                                lowestWeeklyClosePrice = 0

                                #take their epoch time and turn it into current local time

                                t = candle.get('datetime')
                                t = int(str(t)[:-3])#take last 3 digits off
                                charlesSchwabTime = datetime.datetime.fromtimestamp(t).strftime('%X')
                                charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")

                                closePrice = candle.get('close')
                                highPrice = candle.get("high")
                                lowPrice = candle.get("low")
                                volume = candle.get("volume")

                                #begin the hlev process by storing the closePrices in an array
                                #and getting the highest and lowest weekly closePrice

                                if(len(closePriceArray) <= 2000):

                                    closePriceArray.append(closePrice)
                                    highestWeeklyClosePrice = max(closePriceArray)
                                    lowestWeeklyClosePrice = min(closePriceArray)

                                if(len(closePriceArray) > 2000):

                                    closePriceArray.remove(closePriceArray[0])

                                


                                
                                if(lib.Date_Time_Management.Compare_Epoch_DateTime_D1_GreaterThan_D2(t, epoch_DB_DateTime)):

                                    if(prCounter == 0):
                                        previousEma200Value = str(lastRowData[7])
                                        previousEma200Value = float(previousEma200Value)

                                        previousStdDev10AvgValue = str(lastRowData[27])
                                        previousStdDev10AvgValue = float(previousStdDev10AvgValue)

                                    newEma200Value = lib.Calculation_Management.Calculate_NewestEMA200_Method(previousEma200Value,closePrice)

                                    newEMA200AngleValue = lib.Calculation_Management.CalculateAngle(newEma200Value, previousEma200Value)

                                    if(prCounter == 0):
                                        
                                        stdDevArray = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Previous_200_EMA200Angles_from_DB(symbol)
                                        # standardDev10Array = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Previous_200_StdDev10Values_from_DB(symbol)
                                        # standardDev10Array.remove(standardDev10Array[0])
                                        # newStdDev10 = lib.Calculation_Management.Calculate_stdDev10Avg(standardDev10Array)

                                    stdDevArray.append(newEMA200AngleValue)                                               
                                                                                    


                                    stdDevArray.remove(stdDevArray[0])
                                    standardDev = lib.Calculation_Management.Calculate_Standard_Dev_of_Angle_of_EMA200(stdDevArray)

                                    

                                    standardDev2 = standardDev*2
                                    standardDev3 = standardDev*3
                                    standardDev4 = standardDev*4
                                    standardDev5 = standardDev*5
                                    standardDev6 = standardDev*6
                                    standardDev7 = standardDev*7
                                    standardDev8 = standardDev*8
                                    standardDev9 = standardDev*9
                                    standardDev10 = standardDev*10

                                    if(prCounter > 0):
                                        standardDev10Array.append(standardDev10)
                                        
                                        newStdDevAvg10 = 0
                                        if(len(standardDev10Array) > 200):
                                            standardDev10Array.remove(standardDev10Array[0])
                                        
                                        newStdDevAvg10 = lib.Calculation_Management.Calculate_stdDev10Avg(standardDev10Array)

                                        #newStdDevAvg10 = newStdDevAvg10 - (newStdDevAvg10 - previousStdDev10AvgValue)

                                    negStandardDev = standardDev*-1
                                    negStandardDev2 = standardDev*-2
                                    negStandardDev3 = standardDev*-3
                                    negStandardDev4 = standardDev*-4
                                    negStandardDev5 = standardDev*-5
                                    negStandardDev6 = standardDev*-6
                                    negStandardDev7 = standardDev*-7
                                    negStandardDev8 = standardDev*-8
                                    negStandardDev9 = standardDev*-9
                                    negStandardDev10 = standardDev*-10                
                                    


                                    hlevOrigin = 0

                                    hlevPercentage = 0

                                    hlev2000_UpperArm = 0

                                    hlev2000_MiddleArm = 0

                                    hlev2000_LowerArm = 0

                                    for hlv in hlevArray:
                                
                                        highestMonthlyClosePrice = 0
                                        lowestMonthlyClosePrice = 0

                                        if(str(charlesSchwabDate) == str(hlv[0])):

                                            highestMonthlyClosePrice = float(hlv[1])
                                            lowestMonthlyClosePrice = float(hlv[2])

                                            # print(highestMonthlyClosePrice)
                                            # print(lowestMonthlyClosePrice)

                                            #calc and get hlev
                                            #---------------------------------------------------------------
                                            Hlevs = lib.Calculation_Management.Calculate_HLEVs(symbol, closePrice, highestMonthlyClosePrice, lowestMonthlyClosePrice, highestWeeklyClosePrice,lowestWeeklyClosePrice)
                                            # print(Hlevs)
                                            # if(Hlevs is None):

                                            #     continue

                                            hlevOrigin = Hlevs[0]

                                            hlevPercentage = Hlevs[1]

                                            hlev2000_UpperArm = Hlevs[2]

                                            hlev2000_MiddleArm = Hlevs[3]

                                            hlev2000_LowerArm = Hlevs[4]

                                        if(str(charlesSchwabDate) == str(todaysDate)):

                                            highestMonthlyClosePrice = lib.Calculation_Management.round(float(hlv[1]),2)
                                            lowestMonthlyClosePrice = lib.Calculation_Management.round(float(hlv[2]),2)

                                            #calc and get hlev
                                            #---------------------------------------------------------------
                                            Hlevs = lib.Calculation_Management.Calculate_HLEVs(symbol, closePrice, highestMonthlyClosePrice, lowestMonthlyClosePrice, highestWeeklyClosePrice,lowestWeeklyClosePrice)
                                            # print(Hlevs)
                                            # if(Hlevs is None):

                                            #     continue

                                            hlevOrigin = Hlevs[0]

                                            hlevPercentage = Hlevs[1]

                                            hlev2000_UpperArm = Hlevs[2]

                                            hlev2000_MiddleArm = Hlevs[3]

                                            hlev2000_LowerArm = Hlevs[4]

                                    newEma200FaceValue = lib.Calculation_Management.round(newEma200Value,2)

                                    lib.Database_Management.Give_Data_To_LootLoaderDataBase.Give_HistoricalData_To_DB(symbol, charlesSchwabDate, charlesSchwabTime, 
                                                                                        closePrice, highPrice, lowPrice, volume, newEma200FaceValue, 
                                                                                        newEMA200AngleValue, standardDev, 
                                                                                        standardDev2, standardDev3, standardDev4, 
                                                                                        standardDev5, standardDev6, standardDev7, 
                                                                                        standardDev8, standardDev9, standardDev10,
                                                                                        negStandardDev, negStandardDev2, negStandardDev3,
                                                                                        negStandardDev4, negStandardDev5, negStandardDev6,
                                                                                        negStandardDev7, negStandardDev8, negStandardDev9,
                                                                                        negStandardDev10, newStdDevAvg10, hlevOrigin, rowID,
                                                                                        hlevPercentage, hlev2000_UpperArm, hlev2000_MiddleArm, hlev2000_LowerArm)




                                            


                                    
                                    prCounter +=1


                                    




                                    counter_ofAnglePoints+=1

                                    
                                    rowID +=1

                                    previousEma200Value = newEma200Value
                                    #previousStdDev10 = newStdDev10

                            tableName = "{}_historical".format(symbol)
                                                    
                            recordCount = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Total_Amount_of_Records_InTable(tableName)
                            
                            message = "{} of {}. {} - Backfilled to present with {} records stored.".format(counter_ofSymbols, numberOfSymbols,symbol, recordCount)+"\r\f"
                            print(message)
                            print()
                            lib.Logging.info(message) 

                        
                            DB_DatePlus = None

                            closePrice = None
                            highPrice = None
                            lowPrice = None
                            volume = None
                            
                            previousEma200Value = 0
                            newEma200Value = 0
                            newEMA200AngleValue = 0
                            rowID = 1
                            counter_ofDataPoints+=1

                        counter_ofSymbols+=1

                        if(counter_ofSymbols > numberOfSymbols):
                            break
            
                        
        
                    

    except Exception:

        error = traceback.format_exc()
        
        if("An attempt" in error):
            os.system(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Authenticate_Manually.py")
        lib.Logging.error(error)


        if("Unknown table '{}'".format(symbol) in traceback.format_exc()):
            message = " - \r\f"+traceback.format_exc()+"\r\f"
            lib.Logging.error(message)
            counter_ofSymbols+=1
            return
       
        


        if("connection.py" in traceback.format_exc() or "connectionpool.py" in traceback.format_exc()):
            print("Internet connection is closed. Reopening program in 10 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 10 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 9 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 8 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 7 seconds...")
            time.sleep(1) 
            os.system("cls")
            print("Internet connection is closed. Reopening program in 6 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 5 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 4 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 3 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 2 seconds...")
            time.sleep(1)
            os.system("cls")
            print("Internet connection is closed. Reopening program in 1 second...")
            time.sleep(1)



            
            
            message = " - \r\f"+traceback.format_exc()+"\r\rInternet connection is closed. Reopening program in 10 seconds...\r\f"
            lib.Logging.error(message)
            os.system(f"C:\\Users\\"+windowsUsername+f"\Desktop\LootLoader\RunDataLoader.bat")
            quit()

        else:
            message = " - \r\f"+traceback.format_exc()+"\r\r\r\r - END PROGRAM\r\r-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\f"
            lib.Logging.error(message)




def give_Data_to_Trading_DB_Test(symbol):
        
    try:
    
        dBdate = datetime.datetime.now().date()
        time = datetime.datetime.now().time()
        print("true "+str(dBdate)+" "+str(time))
        localDate = dBdate
        localTime = time                        
        lookingForBuy = 1
        alreadyBought = 0
        lookingForSell = 0
        alreadySold = 0
        orderType = "LKFB"                                                              
        Profit_or_Loss = 0.00
        roi = 0.00
        Good_Bad_Trade = "NA"
        orderID = 0
        riskAmount = 0
        accountBalance = 0
        closePrice = 0
        numberOfShares = 0
        buyPrice = 0

        #rowID = int(lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Trading_Tables(symbol)[16])+1
        rowID = 1
        incomeTaxesDue = 0
        sellPrice = 0
        lib.Database_Management.Give_Data_To_LootLoaderDataBase.Give_TradeData_To_DB(symbol, localDate, localTime, accountBalance, 
                                                                                lookingForBuy, alreadyBought, lookingForSell, 
                                                                                alreadySold, orderType, closePrice, numberOfShares, 
                                                                                riskAmount, Profit_or_Loss, roi, incomeTaxesDue, buyPrice, sellPrice,Good_Bad_Trade, 
                                                                                orderID, rowID)
        #-------------

    except:
        error = traceback.format_exc()  
        fileName = "Give_TradeData_To_DB"                                     
        lib.Logging.test(fileName, error)








symbol = "A"
numberOfSymbols = 2

give_Data_to_Trading_DB_Test(symbol)

#mimic_CharSchwabs_HLEV_Origin()

#mimic_CharSchwabs_HLEV_Origin2()


#dailyHistorical_Check()

#CharSchwabs_HLEVs()

#getting_HLEVs_in_DataLoader(numberOfSymbols)

#lookingForBuy_Test(symbol)


# num = 135.517

# print(lib.Calculation_Management.round(num, 2))









