import LLLib_Charles_Schwab as lib
import traceback

try:
    lib.Authentication_Management.Authentication_MyVersion.Authenticate_Manually()
except:
    error = traceback.format_exc()            
    lib.Logging.error(error)