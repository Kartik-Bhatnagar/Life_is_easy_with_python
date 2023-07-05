# pip install pyautogui
import pyautogui
import time
import os

def create_folder(folder):
    
    #print(not os.path.isdir("screenshots"))
    if not os.path.isdir(folder):
        print("Created directory : ",folder)
        os.mkdir(folder)


def one_full_sshot(folder):
    myScreenshot =  pyautogui.screenshot()
    print(myScreenshot)
    t = time.time()
    file_name = ("".join(str(t).split("."))[0:14])+".png"
    file_path = os.path.join(os.curdir,folder,file_name)
    myScreenshot.save(file_path) 

folder = "screenshots"
create_folder(folder)
one_full_sshot(folder)
