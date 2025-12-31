import os
import webbrowser

htmlFile = "C:\\Users\\"+windowsUsername+f"\\Desktop\\LootLoader\\LootLoader_CharlesSchwab\\Testing\\html_linkFile.html"

def DeleteHTMLFile(htmlFile):

    if(os.path.exists(htmlFile)):
        os.remove(htmlFile)


def OpenHTMLFile(htmlFile):
    webbrowser.open_new_tab(htmlFile)



OpenHTMLFile(htmlFile)
DeleteHTMLFile(htmlFile)