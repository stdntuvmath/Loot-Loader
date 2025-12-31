import subprocess
import traceback
import multiprocessing
import LLLib_Charles_Schwab



def run_script(script_path):
    try:
        # This opens a new Command Prompt window and runs the script
        subprocess.run(f'start cmd /K python "{script_path}"', shell=True, check=True)
    except Exception as e:
        input(f"Error running {script_path}: {traceback.format_exc()}")
        LLLib_Charles_Schwab.Logging.error(f"Error running {script_path}: {traceback.format_exc()}")


def run_parallel():
    # Define the paths to your scripts
    script0 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Run_DataLoader0.py"
    script1 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Run_DataLoader1.py"
    script2 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Run_DataLoader2.py"
    script3 = f"C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Run_DataLoader3.py"

    # Create processes for each script
    process1 = multiprocessing.Process(target=run_script, args=(script0,))
    process2 = multiprocessing.Process(target=run_script, args=(script1,))
    process3 = multiprocessing.Process(target=run_script, args=(script2,))
    process4 = multiprocessing.Process(target=run_script, args=(script3,))

    # Start both processes
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    process3.join()
    process4.join()

if __name__ == "__main__":
    run_parallel()
