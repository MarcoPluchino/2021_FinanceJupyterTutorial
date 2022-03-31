import os,sys,inspect
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMessageBox
# from pathlib import Path
# import platform,socket,re,uuid,json,logging
# import time
# import pandas as pd
        
class main():
    prj_folder = os.path.abspath("")
    sys.path.append(prj_folder)
    from rbt.py import utilities,excel
    from rbt.gui import gui 
    SWC_file = prj_folder+'\SWC.xlsx'
    print("breakpoint")
    swc = excel.Import(enable=True,SWC_file=SWC_file).readSwc()
    gui.Gui(show=True, dict=swc, user='developer', verbose=False)

def test1():
    main()
def test2():
    print("TODO")


if __name__ == '__main__':
    test1()
    

    