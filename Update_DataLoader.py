#*************************************************
# NAME: DataLoader Updater.
#       
# AUTHOR: Brandon Turner
#
# PURPOSE: This will update the 
#        each DataLoader file
# 
# Creation Date: 20250326 
#
#
#*************************************************




import shutil
import traceback
import os

global windowsUsername
windowsUsername = os.getenv('USERNAME')#get the windows username of the user

def Update():

    try:


        #replace all the LLLib_Charles_Schwab library files with the main LLLib_Charles_Schwab library file

        source_file = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader.py"
        destination_file0 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader0.py"
        destination_file1 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader1.py"
        destination_file2 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader2.py"
        destination_file3 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader3.py"
        destination_file4 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader4.py"
        destination_file5 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader5.py"
        destination_file6 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader6.py"
        destination_file7 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader7.py"
        destination_file8 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader8.py"



        shutil.copy2(source_file, destination_file0)
        shutil.copy2(source_file, destination_file1)
        shutil.copy2(source_file, destination_file2)
        shutil.copy2(source_file, destination_file3)
        shutil.copy2(source_file, destination_file4)
        shutil.copy2(source_file, destination_file5)
        shutil.copy2(source_file, destination_file6)
        shutil.copy2(source_file, destination_file7)
        shutil.copy2(source_file, destination_file8)




        #now we need to edit each library to be its own

        # update 0

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader0.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_0")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader0.py", 'w') as file:
            file.write(filedata)

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader0")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader0.py", 'w') as file:
            file.write(filedata)


        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[0]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader0.py", 'w') as file:
            file.write(filedata)

        # Replace DataLoader with DataLoader0

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader0.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader0...")











        # update 1

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader1.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_1")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader1.py", 'w') as file:
            file.write(filedata)

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader1")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader1.py", 'w') as file:
            file.write(filedata)


        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[1]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader1.py", 'w') as file:
            file.write(filedata)


        # Replace DataLoader with DataLoader1

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader1.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader1...")






        # update 2

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader2.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_2")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader2.py", 'w') as file:
            file.write(filedata)

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader2")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader2.py", 'w') as file:
            file.write(filedata)


        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[2]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader2.py", 'w') as file:
            file.write(filedata)





        # Replace DataLoader with DataLoader2

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader2.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader2...")







        # update 3

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader3.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_3")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader3.py", 'w') as file:
            file.write(filedata)


        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader3")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader3.py", 'w') as file:
            file.write(filedata)




        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[3]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader3.py", 'w') as file:
            file.write(filedata)





        # Replace DataLoader with DataLoader3

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader3.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader3...")










        # update 4

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader4.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_4")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader4.py", 'w') as file:
            file.write(filedata)



        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader4")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader4.py", 'w') as file:
            file.write(filedata)




        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[4]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader4.py", 'w') as file:
            file.write(filedata)





        # Replace DataLoader with DataLoader4

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader4.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader4...")











        # update 5

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader5.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_5")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader5.py", 'w') as file:
            file.write(filedata)



        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader5")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader5.py", 'w') as file:
            file.write(filedata)




        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[5]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader5.py", 'w') as file:
            file.write(filedata)





        # Replace DataLoader with DataLoader5

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader5.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader5...")











        # update 6

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader6.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_6")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader6.py", 'w') as file:
            file.write(filedata)


        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader6")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader6.py", 'w') as file:
            file.write(filedata)




        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[6]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader6.py", 'w') as file:
            file.write(filedata)




        # Replace DataLoader with DataLoader6

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader6.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader6...")












        # update 7

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader7.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_7")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader7.py", 'w') as file:
            file.write(filedata)


        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader7")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader7.py", 'w') as file:
            file.write(filedata)




        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[7]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader7.py", 'w') as file:
            file.write(filedata)





        # Replace DataLoader with DataLoader7

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader7.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("Opening DataLoader...", "Opening DataLoader7...")











        # update 8

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader8.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("LLLib_Charles_Schwab", "LLLib_Charles_Schwab_8")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader8.py", 'w') as file:
            file.write(filedata)      



        # Replace the target string
        filedata = filedata.replace("Opening DataLoader", "Opening DataLoader8")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader8.py", 'w') as file:
            file.write(filedata)



        # Replace the target string
        filedata = filedata.replace("#symbolList = symbolList[]", "symbolList = symbolList[8]")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader8.py", 'w') as file:
            file.write(filedata)



        # Replace DataLoader with DataLoader8

        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\DataLoader8.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("DataLoader..", "Opening DataLoader8..")






    except:

        input(traceback.format_exc)





Update()
