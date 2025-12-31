import LootLoader
import traceback
import LLLib_Charles_Schwab as lib


def RunLL():

    try:
        LootLoader.Run()

    except:
        error = traceback.format_exc()
        lib.Logging.error(error)  

RunLL()