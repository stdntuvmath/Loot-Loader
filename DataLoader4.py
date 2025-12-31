
import os
import json
import datetime
import os
import time
import traceback

import LLLib_Charles_Schwab_4 as lib

global windowsUsername
windowsUsername = os.getlogin()


def Run():
    

    numberOfSymbols = 85

    try:
        #os.system("CLS")
        todaysDay = lib.Date_Time_Management.Get_Todays_Weekday_Name()
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        now = tday.time()

        print("Opening DataLoader4...")
        print()

     
                 
        message = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\r"+str(now)+" - BEGIN DATALOADER\r\r-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\r"        
    
        
        lib.Logging.info(message)

        allSymbols = ""
        #allSymbols = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Symbol_List()
        symbolList = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Sectioned_Symbol_List_85()
        symbolList = symbolList[4]
        lastRowData = []
        updateArray = []
        hlevs = []
        DB_Date = ""
        previousEma200Value=0
        counter_ofSymbols=1
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
        newStdDev10 = 0

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
        #yesterdays time will need reloaded in the morning because of the reconciliation process of schwabs data
        beforeStartTime1 = now.replace(hour=1, minute=00, second=0)
        beforeStartTime2 = now.replace(hour=10, minute=00, second=0)
        startTime = now.replace(hour=00, minute=00, second=0)
        #endTime = now.replace(hour=20, minute=00, second=0)
        endTime = now.replace(hour=23, minute=59, second=59)

        #time.sleep(1)#pause between symbol list iterations

        previousEma200Value = 0
        previousStdDev10 = 0
        newEma200Value = 0
        newEMA200AngleValue = 0
        newStdDev10Avg = 0

        hlevOrigin = 0.0
        hlevPercentage = 0.0
        hlev2000_UpperArm = 0.0
        hlev2000_MiddleArm = 0.0
        hlev2000_LowerArm = 0.0
        doneOnceAlready = False

        ema200AngleArray.clear()
        EMA200Array.clear()
        #jclosePriceArray.clear()
        stdDevArray.clear()

        while(startTime <= now and now <= endTime):
        #while(True):
            if(counter_ofSymbols >= numberOfSymbols):
                counter_ofSymbols=1 
            for symbol in symbolList:

                if(beforeStartTime1 <= now and now <= beforeStartTime2 and wholeCycleOccurred == False):

                    #check if symbol table exists
                    if(lib.Database_Management.Check_LootLoaderDataBase.Check_If_Table_Exists_in_LLDB("lootloaderdatabase","{}_historical".format(symbol))):
                        #delete yesterdays and todays data only
                    
                        lib.Database_Management.Delete_Data_From_LootLoaderDataBase.Historical.Delete_Yesterdays_and_Todays_Data_Only_for_Symbol(symbol)
                    wholeCycleOccurred = True               

            for symbol in symbolList: 

                #this is required because with the amount of symbols set to 85 we hit the 
                # ping limit for CSchwab server without it
                #####################################################
                time.sleep(1) # taken out because of the Delete_Todays_Data_Only_for_Symbol adding time between pings            
                #####################################################
                if(lib.Database_Management.Check_LootLoaderDataBase.Check_If_Table_Exists_in_LLDB("lootloaderdatabase","{}_historical".format(symbol))):

                                     
                    #we must reformulate todays data and yesterdays data by deleting the previous historical data
                    # and recalculating everything during stock market hours. This refreshes the data ever time interval
                    # 
                    #                    
                    
                    
                        
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

                            isThisANewTable = False
                    
                            tday = datetime.datetime.today()
                            start = tday - datetime.timedelta(days=200)

                            minute_candle_data = ""
                            minute_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Minute_Data_from_Schwab(symbol,start,tday)))
                            if(str(minute_candle_data) == "Null"):
                                print("Error occurred - check log")
                                continue
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









                            message = "{} of {}. Filling data for: {}\r".format(counter_ofSymbols, numberOfSymbols, symbol)
                            print(message)
                            lib.Logging.info(message)



                            for candle in minute_candle_data['candles']:

                                #take their epoch time and turn it into current local time

                                t = candle.get('datetime')
                                t = int(str(t)[:-3])#take last 3 digits off
                                charlesSchwabTime = datetime.datetime.fromtimestamp(t).strftime('%X')# insert local time according to your computers time
                                charlesSchwabDate = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
                                #localDate = datetime.date.strftime(localDate, "%Y-%m-%d")

                                closePrice = candle.get('close')
                                if(float(closePrice) < 5.00):
                                    continue
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

                                #newStdDev10Avg = lib.Calculation_Management.Calculate_Newest_StdDev10Avg_Method(previousStdDev10Avg,standardDev10)

                                standardDev10Array.append(standardDev10)
                                # #newStdDev10 = 0
                                if(len(standardDev10Array) > 200):
                                    standardDev10Array.remove(standardDev10Array[0])                                    
                                    #calc avg of stdDev10
                                    newStdDev10Avg = lib.Calculation_Management.Calculate_stdDev10Avg(standardDev10Array)

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
                                                                                                                            negStandardDev10, newStdDev10Avg, hlevOrigin, rowID,
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
                            tableName = "{}_historical".format(symbol)

                            #isThisANewTable = False                                             
                     
                             

                            status = lib.Database_Management.Create_Delete_Tables.Delete_Tables.Purge_SymbolsTable_of_LowData_Symbols(symbol, counter_ofSymbols, numberOfSymbols)
                            counter_ofSymbols+=1
                            if(status == "Good to trade"):
                                lib.Trading_Management.LootLoader_Method(symbol)
                            print()
                            continue



                        #-------------------------------if Minute data exists

                        if(lastRowData != None):

                            isThisANewTable = True

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


                            print("{} of {}. Backfilling from specified date ".format(counter_ofSymbols, numberOfSymbols)+str(DB_Date)+" - "+str(DB_Time)+" for: {}\r\r".format(symbol))

                            message = "{} of {}. Backfilling from specified date ".format(counter_ofSymbols, numberOfSymbols)+str(DB_Date)+" - "+str(DB_Time)+" for: {}\r\r".format(symbol)
                            lib.Logging.info(message) 
                            

                            rowID = lastRowData[31]
                            rowID = int(rowID)+1



                            tday = datetime.datetime.today()
                            start = tday - datetime.timedelta(days=200)
                            #start = datetime.datetime.strptime(DB_Date, "%Y-%m-%d")

                            minute_candle_data = ""
                            minuteCandle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Minute_Data_from_Schwab(symbol,start,tday)))
                            if(str(minute_candle_data) == "Null"):
                                print("Error occurred - check log")
                                continue
                            daily_candle_data = json.loads(str(lib.Pull_From_Schwab_Management.Get_Historical_Day_Data_from_Schwab(symbol,start,tday)))


                            dailyClosePriceArray = []
                            dateArray = [] 
                            prices_for_last_30_days = []
                            hlevArray = []  
                            Hlevs = []
                            standardDev10Array = []                                

                            message = "{} of {}. Adding records for... {}\r\r".format(counter_ofSymbols, numberOfSymbols, symbol)
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
                                if(float(closePrice) < 5.00):
                                    continue
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
                                        
                                        previousStdDev10 = str(lastRowData[18])
                                        previousStdDev10 = float(previousStdDev10) 

                                        previousStdDev10Avg = str(lastRowData[29])
                                        previousStdDev10Avg = float(previousStdDev10Avg)

                                    newEma200Value = lib.Calculation_Management.Calculate_NewestEMA200_Method(previousEma200Value,closePrice)

                                    newEMA200AngleValue = lib.Calculation_Management.CalculateAngle(newEma200Value, previousEma200Value)

                                    if(prCounter == 0):
                                        
                                        stdDevArray = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Previous_200_EMA200Angles_from_DB(symbol)
                                        prevStdDev10Array = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Previous_200_StdDev10Values_from_DB(symbol)

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


                                    
                                    prevStdDev10Array.append(standardDev10)#add the new one
                                    prevStdDev10Array.remove(prevStdDev10Array[0])#remove the last old one
                                    newStdDev10Avg = lib.Calculation_Management.Calculate_stdDev10Avg(prevStdDev10Array)

                                    #standardDev10Array.append(standardDev10)
                                    #newStdDev10 = 0
                                    # if(len(standardDev10Array) > 200):
                                    #     standardDev10Array.remove(standardDev10Array[0])                                    
                                    #     #calc avg of stdDev10
                                    #     newStdDev10 = lib.Calculation_Management.Calculate_stdDev10Avg(standardDev10Array)

                                    # newStdDev10Avg = lib.Calculation_Management.Calculate_Newest_StdDev10Avg_Method(previousStdDev10Avg,standardDev10)

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
                                                                                        negStandardDev10, newStdDev10Avg, hlevOrigin, rowID,
                                                                                        hlevPercentage, hlev2000_UpperArm, hlev2000_MiddleArm, hlev2000_LowerArm)




                                            


                                    
                                    prCounter +=1


                                    




                                    counter_ofAnglePoints+=1

                                    
                                    rowID +=1

                                    previousEma200Value = newEma200Value
                                    previousStdDev10 = newStdDev10

                            tableName = "{}_historical".format(symbol)
                                                    
                            #recordCount = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Total_Amount_of_Records_InTable(tableName, isThisANewTable)
                            
                            message = "{} of {}. {} - Backfilled to present.".format(counter_ofSymbols, numberOfSymbols,symbol)+"\r\r"
                            print(message)
                            
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

                            lib.Trading_Management.LootLoader_Method(symbol)
                            print()
                        counter_ofSymbols+=1

                        if(counter_ofSymbols > numberOfSymbols):
                                break

         #else:   
                        
        message = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\r"+str(now)+" - END DATALOADER\r\r-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\r"        
                    
        lib.Logging.info(message)

    except Exception:

        error = traceback.format_exc()
        
        if("An attempt" in error):
            os.system(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Authenticate_Manually.py")
            lib.Logging.error(error)
            return

        if("Unknown table '{}'".format(symbol) in traceback.format_exc()):
            message = " - \r\r"+traceback.format_exc()+"\r\r"
            lib.Logging.error(message)
            counter_ofSymbols+=1
            return
       
        if("Expecting value:" in traceback.format_exc()):
            lib.Logging.error(error)
            print()
            print()
            inputResponse = input("Please check the internet connection and and restart Run_DataLoader.py. Press ENTER to close.")
            quit()

            # os.system(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Run_DataLoader.py")
            # return
            


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



            
            
            message = " - \r\r"+traceback.format_exc()+"\r\rInternet connection is closed. Reopening program in 10 seconds...\r\r"
            lib.Logging.error(message)
            os.system(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\RunDataLoader.bat")
            quit()

        else:
            message = " - \r\r"+traceback.format_exc()+"\r\r\r\r - END PROGRAM\r\r-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\r"
            lib.Logging.error(message)
            return




