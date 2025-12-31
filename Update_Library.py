#*************************************************
# NAME: LootLoader Library Updater.
#       
# AUTHOR: Brandon Turner
#
# PURPOSE: This will update the 
#        LLLib_Charles_Schwab library files
# 
# Creation Date: 20250319 
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

        source_file = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab.py"
        destination_file0 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_0.py"
        destination_file1 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_1.py"
        destination_file2 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_2.py"
        destination_file3 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_3.py"
        destination_file4 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_4.py"
        destination_file5 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_5.py"
        destination_file6 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_6.py"
        destination_file7 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_7.py"
        destination_file8 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_8.py"



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
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_0.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_0.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_0.py", 'w') as file:
            file.write(filedata)




        # update 1

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_1.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_1.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_1.py", 'w') as file:
            file.write(filedata)




        # update 2

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_2.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_2.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_2.py", 'w') as file:
            file.write(filedata)




        # update 3

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_3.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_3.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_3.py", 'w') as file:
            file.write(filedata)






        # update 4

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_4.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_4.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_4.py", 'w') as file:
            file.write(filedata)









        # update 5

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_5.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_5.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_5.py", 'w') as file:
            file.write(filedata)








        # update 6

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_6.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_6.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_6.py", 'w') as file:
            file.write(filedata)






        # update 7

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_7.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_7.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_7.py", 'w') as file:
            file.write(filedata)






        # update 8

        # Read in the file
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_8.py", 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(".log", "_8.log")

        # Write the file out again
        with open(f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\LLLib_Charles_Schwab_8.py", 'w') as file:
            file.write(filedata)



    except:

        input(traceback.format_exc())





Update()
