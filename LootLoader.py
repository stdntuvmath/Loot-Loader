import os
import json
import datetime
import os
import time
import traceback

import LLLib_Charles_Schwab as lib




def Run():

    numberOfSymbols = 85

    try:
        os.system("CLS")

        #start dataloaders

        os.system(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Run_DataLoader.py")


        todaysDay = lib.Date_Time_Management.Get_Todays_Weekday_Name()
        tday = datetime.datetime.today()
        todaysDate = tday.date()
        now = tday.time()

        print("Opening LootLoader...")
        print()

     
                 
        message = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\f"+str(now)+" - BEGIN LootLoader\r\r-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\r\f"        
    
        
        lib.Logging.info(message)

        allSymbols = ""
        allSymbols = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Symbol_List()
        
        symbolList = allSymbols
        lastRowData = []
        updateArray = []
        hlevs = []
        DB_Date = ""
        DB_Time = ""
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
        beforeStartTime1 = now.replace(hour=00, minute=00, second=0)
        beforeStartTime2 = now.replace(hour=10, minute=00, second=0)
        startTime = now.replace(hour=8, minute=29, second=0)
        #endTime = now.replace(hour=20, minute=00, second=0)
        endTime = now.replace(hour=23, minute=59, second=0)

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
        counter_ofSymbols = 1

        ema200AngleArray.clear()
        EMA200Array.clear()
        #jclosePriceArray.clear()
        stdDevArray.clear()

        while(beforeStartTime1 <= now and now <= endTime):

            counter_ofSymbols=1

            for symbol in symbolList:

                lastRowData = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Historical_Tables(symbol)
                
       
                DB_Date = str(lastRowData[1]).replace(" '","")
                DB_Date = DB_Date.replace("'","")
                DB_Date = DB_Date.replace(" ","")

                DB_Time = str(lastRowData[2]).replace(" '","")
                DB_Time = DB_Time.replace("'","")
                DB_Time = DB_Time.replace(" ","")

                #DB_Date = datetime.datetime.strptime(DB_Date, '%Y-%m-%d')
                DB_Time = datetime.datetime.strptime(DB_Time, '%H:%M:%S')
                
                now = tday.replace(microsecond=0)
                

                
                fourtyFiveMins = tday.replace(hour=00, minute=45, second=0).time()

                #print(type(fourtyFiveMins))

                fourtyFiveMinsAgo = now - datetime.timedelta(minutes=45)

                #fourtyFiveMinsAgo = datetime.datetime.combine(datetime.date.min, now) - datetime.datetime.combine(datetime.date.min,fourtyFiveMins)
                fourtyFiveMinsAgo = str(fourtyFiveMinsAgo.time().replace(microsecond=0))
                fourtyFiveMinsAgo = datetime.datetime.strptime(fourtyFiveMinsAgo, '%H:%M:%S')

                #print(str(fourtyFiveMinsAgo).replace("1900-01-01 ",""))
                message = "waiting on database loading..."
                print(message)
                lib.Logging.info(message)
                while(DB_Date < str(todaysDate)):

                    print(DB_Date+"   "+str(todaysDate))

                    lastRowData = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Historical_Tables(symbol)                
       
                    DB_Date = str(lastRowData[1]).replace(" '","")
                    DB_Date = DB_Date.replace("'","")
                    DB_Date = DB_Date.replace(" ","")

                while(DB_Time < str(fourtyFiveMinsAgo).replace("1900-01-01 ","")):

                    lastRowData = lib.Database_Management.Get_Data_From_LootLoaderDataBase.Historical.Get_Last_Row_of_Historical_Tables(symbol)

                    DB_Time = str(lastRowData[2]).replace(" '","")
                    DB_Time = DB_Time.replace("'","")
                    DB_Time = DB_Time.replace(" ","")

                    DB_Time = datetime.datetime.strptime(DB_Time, '%H:%M:%S')
                    
                    now = tday.replace(microsecond=0)
                

                
                    fourtyFiveMins = tday.replace(hour=00, minute=45, second=0).time()

                    #print(type(fourtyFiveMins))

                    fourtyFiveMinsAgo = now - datetime.timedelta(minutes=45)

                    #fourtyFiveMinsAgo = datetime.datetime.combine(datetime.date.min, now) - datetime.datetime.combine(datetime.date.min,fourtyFiveMins)
                    fourtyFiveMinsAgo = str(fourtyFiveMinsAgo.time().replace(microsecond=0))
                    fourtyFiveMinsAgo = datetime.datetime.strptime(fourtyFiveMinsAgo, '%H:%M:%S')

                message = "looking for trades..."
                print(message)
                lib.Logging.info(message)

                lib.Trading_Management.LootLoader_Method(symbol)


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
       
        if("Expecting value:" in traceback.format_exc()):
            os.system(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Run_DataLoader.py")
            quit()
        lib.Logging.error(error)


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